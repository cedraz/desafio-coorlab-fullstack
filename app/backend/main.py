from typing import Union
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ValidationError
from models.error_models import Error404, Error400
from models.data_models import TravelRequest, TravelResponse
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("../data.json", "r") as f:
    data = json.load(f)['transport']

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Validation error."},
    )

@app.get("/cities")
def get_cities():
    cities = list(set([obj['city'] for obj in data]))

    return cities

@app.post("/travel", response_model=TravelResponse, responses={
    404: {"model": Error404, "description": "City not found"}, 
    400: {"model": Error400, "description": "Invalid data"}}
    )
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
        print(type(float(travel['price_econ'].replace('R$', '').strip())))
        if price_econ < float(economic['price_econ'].replace('R$', '').strip()):
            economic = travel


    confort = travels[0]

    for travel in travels:
        if int(travel['duration'].replace('h', '')) < int(confort['duration'].replace('h', '')):
            confort = travel

    return {
        "confort": {
            "name": confort['name'],
            "price_conf": int(float(confort['price_confort'].replace('R$', '').strip()) * 100),
            "bed": confort['bed'],
            "duration": confort['duration'],
        },
        "economic": {
            "name": economic['name'],
            "price_econ": int(float(economic['price_econ'].replace('R$', '').strip()) * 100),
            "seat": economic['seat'],
            "duration": economic['duration'],
        }
    }

