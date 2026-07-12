from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging

logger = logging.getLogger("documind")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


def _serialize_validation_errors(errors: list) -> list:
    serialized = []
    for err in errors:
        serialized.append({
            "loc": list(err.get("loc", [])),
            "msg": err.get("msg"),
            "type": err.get("type"),
            "input": err.get("input"),
        })
    return serialized


async def global_exception_handler(request: Request, exc: Exception):
    """Return a consistent JSON response for unexpected server errors."""
    logger.exception("Unhandled exception for %s", request.url.path)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "Something went wrong",
            "status_code": 500,
        },
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors with a friendly JSON payload."""
    logger.warning("Validation error for %s: %s", request.url.path, exc.errors())
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Validation failed",
            "detail": _serialize_validation_errors(exc.errors()),
            "status_code": 422,
        },
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    """Return a consistent JSON response for route-level HTTP errors."""
    logger.warning("HTTP error for %s: %s", request.url.path, exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": str(exc.detail),
            "status_code": exc.status_code,
        },
    )
