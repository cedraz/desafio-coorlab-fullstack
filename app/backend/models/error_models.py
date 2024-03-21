from pydantic import BaseModel, Field

class Error400(BaseModel):
    detail: str = Field(..., example="Bad request.")

class Error404(BaseModel):
    detail: str = Field(..., example="City not found.")