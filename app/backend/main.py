from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TravelRequest(BaseModel):
    city: str

class Confort(BaseModel):
    name: str
    bed: str
    duration: str
    price_conf: str

class Economic(BaseModel):
    name: str
    price_econ: str
    seat: str
    duration: str
class TravelResponse(BaseModel):
    confort: Confort
    economic: Economic

with open("../data.json", "r") as f:
    data = json.load(f)['transport']

@app.get("/cities")
def get_cities():
    cities = list(set([obj['city'] for obj in data]))

    return cities

@app.post("/travel", response_model=TravelResponse)
def get_travel(travel_request: TravelRequest):
    print(travel_request)
    if not travel_request.city:
        raise HTTPException(status_code=400, detail="Bad request")

    travels = [obj for obj in data if obj['city'] == travel_request.city]

    if not travels:
        raise HTTPException(status_code=404, detail="City not found")

    economic = travels[0]

    for travel in travels:
        price_econ = float(travel['price_econ'].replace('R$', '').strip())
        if price_econ < float(economic['price_econ'].replace('R$', '').strip()):
            economic = travel
    
    confort = travels[0]

    for travel in travels:
        if travel['duration'] < confort['duration']:
            confort = travel

    return {
        "confort": {
            "name": confort['name'],
            "price_conf": confort['price_confort'],
            "bed": confort['bed'],
            "duration": confort['duration'],
        },
        "economic": {
            "name": confort['name'],
            "price_econ": confort['price_econ'],
            "seat": confort['seat'],
            "duration": confort['duration'],
        }
    }

