from fastapi import Depends
from app.services.conversion_service import ConversionService
from app.infrastructure.storage.local import LocalStorage

def get_storage():
    return LocalStorage()

def get_conversion_service():
    return ConversionService()