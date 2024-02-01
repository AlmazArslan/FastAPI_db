from fastapi import APIRouter, Depends
from typing import Optional, List
from urllib.parse import unquote

from models.histogram import Histogram
from reps.histogram import HistogramRepository
from .depends import get_histogram_repository

from loguru import logger

router = APIRouter()
 
@router.get('/steam_ids', response_model=List[Histogram])
async def read_by_steam_ids(
	limit: int = 10,
	offset: int = 0,
	Histograms: HistogramRepository = Depends(get_histogram_repository)) -> List[Histogram]:
	return await Histograms.get_all(limit, offset)

@router.get('/hash_name')
async def read_by_hash_name(
	hash_name: str = '',
	Histograms: HistogramRepository = Depends(get_histogram_repository)) -> Optional[Histogram]:
	return await Histograms.get_by_hash_name( unquote(hash_name) )
