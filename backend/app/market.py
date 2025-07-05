import aiohttp
import aioredis
import json
import yfinance as yf
from .config import settings

ALPHAVANTAGE_URL = "https://www.alphavantage.co/query"

async def get_redis():
    return await aioredis.from_url(settings.REDIS_URL)

async def fetch_alpha_vantage(symbol: str):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": settings.MARKET_API_KEY,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(ALPHAVANTAGE_URL, params=params) as resp:
            if resp.status == 200:
                return await resp.json()
            return None

async def fetch_yfinance(symbol: str):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if not data.empty:
        return {
            "price": data["Close"].iloc[-1]
        }
    return None

async def get_market_data(symbol: str):
    redis = await get_redis()
    cache_key = f"market:{symbol}"
    cached = await redis.get(cache_key)
    if cached:
        try:
            return json.loads(cached.decode())
        except Exception:
            return cached

    data = await fetch_alpha_vantage(symbol)
    if not data:
        data = await fetch_yfinance(symbol)

    if data:
        await redis.set(cache_key, json.dumps(data), ex=300)
    return data
