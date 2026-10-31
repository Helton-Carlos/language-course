from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "a1f3c5d7e9b1"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
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


def downgrade() -> None:
    op.drop_table("languages")
