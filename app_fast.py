import uvicorn

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from src.presentation.container.ioc_container import Container
from src.presentation.controllers.login_controller_fast import token_router
from src.presentation.controllers.users_controller_fast import users_router


container = Container()
container.config.from_yaml('src/presentation/config/config.yaml')


app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


app.include_router(token_router)
app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
