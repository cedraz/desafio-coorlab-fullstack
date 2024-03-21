from pydantic import BaseModel, Field

class Confort(BaseModel):
    name: str = Field(..., example="Expresso Oriente")
    price_conf: int = Field(..., example="R$ 311.30")
    bed: str = Field(..., example="7C")
    duration: str = Field(..., example="12h")

class Economic(BaseModel):
    name: str = Field(..., example="Expresso Oriente")
    price_econ: int = Field(..., example="R$ 270.95")
    seat: str = Field(..., example="16A")
    duration: str = Field(..., example="12h")

class TravelRequest(BaseModel):
    city: str = Field(..., example="São Paulo")

class TravelResponse(BaseModel):
    confort: Confort
    economic: Economic