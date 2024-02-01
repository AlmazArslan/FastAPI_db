В проекте использовоал FastAPI для получения данных из базы данных Postgresql
Для подключения к ДБ ислоьзовал databases, так как он работает асинхронно
Для создания SQL запросов использовал SQLAlchemy

База данных представляет из себя информацию о ценах на игровые скины торговой площадки Steam
app_id - id игры
hash_name - имя предмета
buy_price - минимальная цена моментальной покупки
sell_price - максимальная цена моментальной продажи
steam_id - "внутренний" steam'овский id предмета
updated - timestamp последнего обновления цены

GET /histogram/steam_ids - возвращает данные об предметах(отсортированных по steam_id)

/histogram/steam_ids?limit=2&offset=0

[
  {
    "app_id": 730,
    "hash_name": "Operation Payback Pass",
    "buy_price": 24311,
    "sell_price": 31668,
    "steam_id": 231888,
    "updated": "2024-01-05T18:05:05.017080Z"
  },
  {
    "app_id": 730,
    "hash_name": "eSports 2013 Case",
    "buy_price": 4246,
    "sell_price": 4375,
    "steam_id": 1269049,
    "updated": "2024-01-05T18:05:05.060165Z"
  }
]

GET /histogram/hash_name - возвращает данные об предмете, по hash_name

/histogram/hash_name?hash_name=MAC-10%20%7C%20Tornado%20%28Field-Tested%29

{
  "app_id": 730,
  "hash_name": "MAC-10 | Tornado (Field-Tested)",
  "buy_price": 181,
  "sell_price": 189,
  "steam_id": 1321314,
  "updated": "2024-01-05T18:05:16.226609Z"
}
