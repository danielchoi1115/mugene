from fastapi import FastAPI, APIRouter
from api_v1 import api
from core.config import settings
# 1
app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

root_router = APIRouter()

app.include_router(api.api_router, prefix=settings.API_V1_STR)  # <----- API versioning
app.include_router(root_router)

# 5
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", reload=True)
    