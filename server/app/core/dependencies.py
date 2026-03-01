from fastapi import Depends
from app.services.conversion_service import ConversionService

def get_conversion_service():
    return ConversionService()