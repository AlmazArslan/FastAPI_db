from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/steam_market"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)