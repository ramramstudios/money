from pydantic import BaseModel, Field
from typing import List, Optional

class Account(BaseModel):
    name: str
    balance: float

class Debt(BaseModel):
    name: str
    amount: float
    interest_rate: float

class UserProfile(BaseModel):
    username: Optional[str] = None
    age: int
    employment_status: str
    accounts: List[Account] = []
    debts: List[Debt] = []
    goals: Optional[str] = None
    risk_tolerance: Optional[str] = None

class SimulationRequest(BaseModel):
    starting_balance: float
    years: int = Field(..., gt=0)
    annual_return: float = 0.05
    annual_volatility: float = 0.1

class SimulationResult(BaseModel):
    projections: List[float]

