import uuid
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "b8c0d2e4f6a8"
down_revision: str | None = "a7b9c1d3e5f7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

ENGLISH_ID = uuid.UUID("6f1c2d3e-4a5b-4c6d-8e7f-9a0b1c2d3e4f")
CONTENT_TABLES = ("placement_questions", "podcast_episodes", "phrases")
ENGLISH_ROW = {
    "id": ENGLISH_ID,
    "code": "en-US",
    "name": "English",
    "name_pt": "inglês",
    "prefix": "US",
    "description": "Idioma mais usado nos negócios, na ciência, no turismo e na internet. É a principal língua de comunicação entre pessoas de países diferentes.",
    "countries": ["Estados Unidos", "Reino Unido", "Canadá", "Austrália", "Nova Zelândia", "Irlanda"],
}


def upgrade() -> None:
    connection = op.get_bind()
    old_id = connection.execute(sa.text("SELECT id FROM languages WHERE code = 'en-US'")).scalar_one()

    op.drop_constraint("fk_users_language_id_languages", "users", type_="foreignkey")
    for table in CONTENT_TABLES:
        op.drop_constraint(f"fk_{table}_language_id_languages", table, type_="foreignkey")

    for table in CONTENT_TABLES:
        connection.execute(
            sa.text(f"DELETE FROM {table} WHERE language_id <> :old"),
            {"old": old_id},
        )
        connection.execute(
            sa.text(f"UPDATE {table} SET language_id = :new WHERE language_id = :old"),
            {"new": ENGLISH_ID, "old": old_id},
        )

    connection.execute(
        sa.text("UPDATE users SET language_id = :new WHERE language_id IS NOT NULL"),
        {"new": ENGLISH_ID},
    )

    op.drop_table("languages")


def downgrade() -> None:
    languages_table = op.create_table(
        "languages",
        sa.Column("id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("name_pt", sa.String(length=100), nullable=False),
        sa.Column("prefix", sa.String(length=2), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column(
            "countries",
            postgresql.ARRAY(sa.String(length=100)),
            server_default=sa.text("'{}'"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="pk_languages"),
        sa.UniqueConstraint("code", name="uq_languages_code"),
    )
    op.bulk_insert(languages_table, [ENGLISH_ROW])

    op.create_foreign_key(
        "fk_users_language_id_languages",
        "users",
        "languages",
        ["language_id"],
        ["id"],
        ondelete="SET NULL",
    )
    for table in CONTENT_TABLES:
        op.create_foreign_key(
            f"fk_{table}_language_id_languages",
            table,
            "languages",
            ["language_id"],
            ["id"],
            ondelete="CASCADE",
        )
