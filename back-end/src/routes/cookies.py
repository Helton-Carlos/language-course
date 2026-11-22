from fastapi import Request, Response

from core.config import get_auth_settings

COOKIE_SAMESITE = "lax"
COOKIE_PATH = "/"


def read_auth_token(request: Request) -> str | None:
    return request.cookies.get(get_auth_settings().cookie_name)


def set_auth_cookie(response: Response, token: str) -> None:
    settings = get_auth_settings()
    response.set_cookie(
        key=settings.cookie_name,
        value=token,
        max_age=settings.access_token_minutes * 60,
        httponly=True,
        secure=settings.cookie_secure,
        samesite=COOKIE_SAMESITE,
        path=COOKIE_PATH,
    )


def clear_auth_cookie(response: Response) -> None:
    settings = get_auth_settings()
    response.delete_cookie(
        key=settings.cookie_name,
        httponly=True,
        secure=settings.cookie_secure,
        samesite=COOKIE_SAMESITE,
        path=COOKIE_PATH,
    )
