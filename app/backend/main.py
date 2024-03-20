from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class TravelRequest(BaseModel):
    city: str

with open("../data.json", "r") as f:
    data = json.load(f)['transport']

@app.get("/cities")
def get_cities():
    cities = list(set([obj['city'] for obj in data]))

    return cities

@app.post("/travel")
def get_travel(travel_request: TravelRequest):

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
            "bed": confort['bed'],
            "duration": confort['duration'],
            "price_conf": confort['price_econ'],
        },
        "economic": {
            "name": confort['name'],
            "price_econ": confort['price_econ'],
            "seat": confort['seat'],
            "duration": confort['duration'],
        }
    }

