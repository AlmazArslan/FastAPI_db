from reps.histogram import HistogramRepository

from db.base import database

def get_histogram_repository() -> HistogramRepository:
	return HistogramRepository(database)