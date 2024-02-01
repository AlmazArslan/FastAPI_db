from fastapi import APIRouter
from endpoints import histogram

routes = APIRouter()

routes.include_router(histogram.router, prefix='/histogram', tags=['histogram'])
