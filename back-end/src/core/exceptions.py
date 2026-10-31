from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    status_code = 500
    detail = "Erro interno"

    def __init__(self, detail: str | None = None) -> None:
        super().__init__(detail or self.detail)
        self.detail = detail or self.detail


class NotFoundError(AppError):
    status_code = 404
    detail = "Recurso não encontrado"


class ConflictError(AppError):
    status_code = 409
    detail = "Conflito com um recurso existente"


class LanguageNotFoundError(NotFoundError):
    detail = "Idioma não encontrado"


class LanguageCodeAlreadyExistsError(ConflictError):
    detail = "Já existe um idioma com esse código"


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def handle_app_error(_: Request, exc: AppError) -> JSONResponse:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
