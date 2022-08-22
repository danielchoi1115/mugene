import time
from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware


class BaseMiddleware(BaseHTTPMiddleware):
    def __init__(
            self,
            app
    ):
        super().__init__(app)

    async def __call__(self, request: Request, call_next):
        try:
            start_time = time.time()
            response = await call_next(request)

        # except InvalidId as ex:
        #     response = JSONResponse(
        #         content=jsonable_encoder({
        #             "result": "failed",
        #             "error": str(ex)
        #         }),
        #         status_code=400
        #     )
        except Exception as ex:
            print(ex)
        finally:
            process_time = time.time() - start_time
            response.headers["X-Process-Time"] = str(process_time)
            return response
