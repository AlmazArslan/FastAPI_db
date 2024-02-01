import sqlalchemy
from .base import metadata
import datetime

histogram = sqlalchemy.Table(
	"market",
	metadata,
	sqlalchemy.Column('app_id', sqlalchemy.Integer),
	sqlalchemy.Column('hash_name', sqlalchemy.String(length=256)),
	sqlalchemy.Column('buy_price', sqlalchemy.Integer),
	sqlalchemy.Column('sell_price', sqlalchemy.Integer),
	sqlalchemy.Column('updated', sqlalchemy.DateTime(timezone=True)),
	sqlalchemy.Column('steam_id', sqlalchemy.Integer, primary_key=True),
)
