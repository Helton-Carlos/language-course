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


class UnauthorizedError(AppError):
    status_code = 401
    detail = "Não autenticado"


class InvalidCredentialsError(UnauthorizedError):
    detail = "E-mail ou senha inválidos"


class WrongPasswordError(AppError):
    status_code = 403
    detail = "Senha incorreta"


class InvalidPlacementAnswersError(AppError):
    status_code = 422
    detail = "Respostas inválidas para este nível"


class PlacementTestUnavailableError(NotFoundError):
    detail = "Teste de nível indisponível para este idioma e nível"


class ReadingTextNotFoundError(NotFoundError):
    detail = "Texto de leitura não encontrado"


class LanguageNotFoundError(NotFoundError):
    detail = "Idioma não encontrado"


class UserNotFoundError(NotFoundError):
    detail = "Usuário não encontrado"


class UserEmailAlreadyExistsError(ConflictError):
    detail = "Já existe um usuário com esse e-mail"


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def handle_app_error(_: Request, exc: AppError) -> JSONResponse:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
