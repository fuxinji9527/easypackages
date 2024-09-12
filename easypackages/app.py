from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from easypackages.api.router import router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="easypackages server",
        description="FastAPI Starter Project",
        version="1.0",
        docs_url="/api/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=router, prefix="/api")

    return app
