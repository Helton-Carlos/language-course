from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "d1f3a5c7e9b2"
down_revision: str | None = "c9d1e3f5a7b9"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "vocabulary_items",
        sa.Column("id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("term", sa.String(length=100), nullable=False),
        sa.Column("meaning", sa.String(length=300), server_default="", nullable=False),
        sa.Column("context", sa.Text(), nullable=True),
        sa.Column("status", sa.SmallInteger(), server_default="1", nullable=False),
        sa.Column("review_count", sa.SmallInteger(), server_default="0", nullable=False),
        sa.Column("next_review_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("status BETWEEN 1 AND 5", name="ck_vocabulary_items_status_valid"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="fk_vocabulary_items_user_id_users",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_vocabulary_items"),
        sa.UniqueConstraint("user_id", "term", name="uq_vocabulary_items_user_id_term"),
    )
    op.create_index("ix_vocabulary_items_user_id_status", "vocabulary_items", ["user_id", "status"])
    op.create_index(
        "ix_vocabulary_items_user_id_next_review_at",
        "vocabulary_items",
        ["user_id", "next_review_at"],
    )
    op.create_table(
        "lessons",
        sa.Column("id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="fk_lessons_user_id_users",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_lessons"),
    )
    op.create_index("ix_lessons_user_id_created_at", "lessons", ["user_id", "created_at"])
    op.create_table(
        "daily_activities",
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("day", sa.Date(), nullable=False),
        sa.Column("words_saved", sa.Integer(), server_default="0", nullable=False),
        sa.Column("reviews", sa.Integer(), server_default="0", nullable=False),
        sa.Column("words_read", sa.Integer(), server_default="0", nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="fk_daily_activities_user_id_users",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("user_id", "day", name="pk_daily_activities"),
    )


def downgrade() -> None:
    op.drop_table("daily_activities")
    op.drop_index("ix_lessons_user_id_created_at", table_name="lessons")
    op.drop_table("lessons")
    op.drop_index("ix_vocabulary_items_user_id_next_review_at", table_name="vocabulary_items")
    op.drop_index("ix_vocabulary_items_user_id_status", table_name="vocabulary_items")
    op.drop_table("vocabulary_items")
