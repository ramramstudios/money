from fastapi import FastAPI
from shared.models import UserProfile, SimulationRequest, SimulationResult
from .market import get_market_data

app = FastAPI(title="Retirement Planner")

@app.post("/api/user/profile")
async def save_profile(profile: UserProfile):
    # Placeholder for saving to database
    return {"status": "saved", "profile": profile}

@app.get("/api/market/{symbol}")
async def market(symbol: str):
    data = await get_market_data(symbol)
    return {"symbol": symbol, "data": data}

@app.post("/api/simulate", response_model=SimulationResult)
async def simulate(req: SimulationRequest):
    # Placeholder Monte Carlo simulation
    projections = [req.starting_balance * (1 + req.annual_return) ** year for year in range(req.years + 1)]
    return SimulationResult(projections=projections)

@app.get("/api/recommendations")
async def recommendations():
    # Placeholder for optimization logic
    return {"actions": []}

