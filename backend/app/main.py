from fastapi import FastAPI, APIRouter
from app.api.api_v1 import api
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

root_router = APIRouter()

app.include_router(api.api_router, prefix=settings.API_V1_STR)  # <----- API versioning
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

# 5
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", reload=True)
