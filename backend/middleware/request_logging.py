import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("documind")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        client_ip = request.client.host if request.client else "unknown"

        logger.info(
            "Incoming request: %s %s from %s",
            request.method,
            request.url.path,
            client_ip,
        )

        response = await call_next(request)

        duration_ms = round((time.time() - start_time) * 1000, 2)
        response.headers["X-Process-Time"] = f"{duration_ms:.2f}"
        logger.info(
            "Completed request: %s %s status=%s duration_ms=%.2f",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
        )
        return response
