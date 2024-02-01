from typing import List, Optional
from db.histogram import histogram
from models.histogram import Histogram
from .base import BaseRepository

from loguru import logger

class HistogramRepository(BaseRepository):
	async def get_all(self, limit: int = 100, skip = 0) -> List[Histogram]:
		limit = limit if limit <= 100 else 100
		query = histogram.select().limit(limit).offset(skip).order_by('steam_id')
		return await self.database.fetch_all(query=query)

	async def get_by_hash_name(self, hash_name: str) -> Optional[Histogram]:
		query = histogram.select().where(histogram.c.hash_name == hash_name)
		logger.info(query)
		return await self.database.fetch_one(query=query)