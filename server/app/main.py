from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.config import settings
from app.core.middleware import logging_middleware
from app.core.exceptions import ConversionError

app = FastAPI(title=settings.APP_NAME)

app.middleware("http")(logging_middleware)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.exception_handler(ConversionError)
async def conversion_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={"error": exc.message})

app = FastAPI(title="File Converter API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)

# @app.get("/")
# def root():
#     return {"status": "API running"}