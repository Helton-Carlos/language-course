from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "d4e6f8a0b2c4"
down_revision: str | None = "c3d5e7f9a1b3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

LEVELS_SQL = "('A1', 'A2', 'B1', 'B2', 'C1', 'C2')"


def upgrade() -> None:
    op.add_column("users", sa.Column("language_id", sa.Uuid(), nullable=True))
    op.add_column("users", sa.Column("level", sa.String(length=2), nullable=True))
    op.create_foreign_key(
        "fk_users_language_id_languages",
        "users",
        "languages",
        ["language_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_check_constraint(
        "ck_users_level_valid",
        "users",
        f"level IS NULL OR level IN {LEVELS_SQL}",
    )

    op.create_table(
        "placement_questions",
        sa.Column("id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("language_id", sa.Uuid(), nullable=False),
        sa.Column("level", sa.String(length=2), nullable=False),
        sa.Column("prompt", sa.Text(), nullable=False),
        sa.Column("options", postgresql.ARRAY(sa.Text()), nullable=False),
        sa.Column("correct_index", sa.SmallInteger(), nullable=False),
        sa.CheckConstraint(f"level IN {LEVELS_SQL}", name="ck_placement_questions_level_valid"),
        sa.CheckConstraint("cardinality(options) = 4", name="ck_placement_questions_four_options"),
        sa.CheckConstraint(
            "correct_index >= 0 AND correct_index < 4",
            name="ck_placement_questions_correct_index_valid",
        ),
        sa.ForeignKeyConstraint(
            ["language_id"],
            ["languages.id"],
            name="fk_placement_questions_language_id_languages",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_placement_questions"),
    )
    op.create_index(
        "ix_placement_questions_language_id_level",
        "placement_questions",
        ["language_id", "level"],
    )


def downgrade() -> None:
    op.drop_index("ix_placement_questions_language_id_level", table_name="placement_questions")
    op.drop_table("placement_questions")
    op.drop_constraint("ck_users_level_valid", "users", type_="check")
    op.drop_constraint("fk_users_language_id_languages", "users", type_="foreignkey")
    op.drop_column("users", "level")
    op.drop_column("users", "language_id")
