import uvicorn
from fastapi import FastAPI

from db.base import database
from routes import routes

app = FastAPI(title="kokocuk_SteamDB")
app.include_router(routes)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

