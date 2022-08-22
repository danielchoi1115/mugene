from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi import FastAPI, APIRouter, Request
import time
from app.api.api_v1 import api
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware import BaseMiddleware
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
# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#         try:
#             start_time = time.time()
#             response = await call_next(request)

#         # except InvalidId as ex:
#         #     response = JSONResponse(
#         #         content=jsonable_encoder({
#         #             "result": "failed",
#         #             "error": str(ex)
#         #         }),
#         #         status_code=400
#         #     )
#         except Exception as ex:
#             print(ex)
#         finally:
#             process_time = time.time() - start_time
#             response.headers["X-Process-Time"] = str(process_time)
#             return response


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", reload=True)
