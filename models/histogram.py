
from datetime import datetime
from pydantic import BaseModel

class Histogram(BaseModel):
	app_id: int
	hash_name: str
	buy_price: int
	sell_price: int
	steam_id: int
	updated: datetime
