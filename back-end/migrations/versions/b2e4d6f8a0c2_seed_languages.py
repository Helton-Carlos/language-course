from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "b2e4d6f8a0c2"
down_revision: str | None = "a1f3c5d7e9b1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

LANGUAGES = [
    {
        "code": "en-US",
        "name": "English",
        "name_pt": "inglês",
        "prefix": "US",
        "description": "Idioma mais usado nos negócios, na ciência, no turismo e na internet. É a principal língua de comunicação entre pessoas de países diferentes.",
        "countries": ["Estados Unidos", "Reino Unido", "Canadá", "Austrália", "Nova Zelândia", "Irlanda"],
    },
    {
        "code": "es-ES",
        "name": "Español",
        "name_pt": "espanhol",
        "prefix": "ES",
        "description": "Tem mais de 480 milhões de falantes nativos e é muito próximo do português, o que facilita o aprendizado para brasileiros.",
        "countries": ["Espanha", "México", "Argentina", "Colômbia", "Chile", "Peru"],
    },
    {
        "code": "fr-FR",
        "name": "Français",
        "name_pt": "francês",
        "prefix": "FR",
        "description": "Idioma oficial em países de vários continentes e muito usado em diplomacia, culinária, moda e artes.",
        "countries": ["França", "Canadá", "Bélgica", "Suíça", "Senegal", "Costa do Marfim"],
    },
    {
        "code": "de-DE",
        "name": "Deutsch",
        "name_pt": "alemão",
        "prefix": "DE",
        "description": "É a língua materna mais falada na União Europeia e tem grande importância na indústria, na engenharia e na pesquisa acadêmica.",
        "countries": ["Alemanha", "Áustria", "Suíça", "Liechtenstein", "Luxemburgo"],
    },
    {
        "code": "zh-CN",
        "name": "中文",
        "name_pt": "chinês",
        "prefix": "CN",
        "description": "O mandarim é o idioma com mais falantes nativos do mundo e é escrito com caracteres, não com alfabeto.",
        "countries": ["China", "Taiwan", "Singapura"],
    },
    {
        "code": "ja-JP",
        "name": "日本語",
        "name_pt": "japonês",
        "prefix": "JP",
        "description": "Usa três sistemas de escrita, hiragana, katakana e kanji, e é falado quase exclusivamente no Japão.",
        "countries": ["Japão"],
    },
]

languages_table = sa.table(
    "languages",
    sa.column("code", sa.String),
    sa.column("name", sa.String),
    sa.column("name_pt", sa.String),
    sa.column("prefix", sa.String),
    sa.column("description", sa.Text),
    sa.column("countries", postgresql.ARRAY(sa.String)),
)


def upgrade() -> None:
    op.bulk_insert(languages_table, LANGUAGES)


def downgrade() -> None:
    codes = [language["code"] for language in LANGUAGES]
    op.execute(languages_table.delete().where(languages_table.c.code.in_(codes)))
