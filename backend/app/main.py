from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi import FastAPI, APIRouter, Request, Depends
import time
from app.api.api_v1 import api
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware import BaseMiddleware
from app.core import get_settings, Settings

def get_application(settings: Settings = get_settings()) -> FastAPI:
    app = FastAPI(
        title="MuGene API", openapi_url="/openapi.json"
    )
    root_router = APIRouter()

    app.include_router(api.api_router, prefix=settings.API_V1_STR)
    app.include_router(root_router)
    
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    return app

app = get_application()

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", reload=True)
