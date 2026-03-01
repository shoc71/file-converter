from pydantic import BaseModel

class ConversionResponse(BaseModel):
    filename: str
    message: str