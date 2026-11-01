from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "f6a8b0c2d4e6"
down_revision: str | None = "e5f7a9b1c3d5"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "podcast_episodes",
        sa.Column("id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("language_id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("youtube_id", sa.String(length=11), nullable=False),
        sa.Column("position", sa.SmallInteger(), server_default="0", nullable=False),
        sa.CheckConstraint(
            "youtube_id ~ '^[A-Za-z0-9_-]{11}$'",
            name="ck_podcast_episodes_youtube_id_valid",
        ),
        sa.ForeignKeyConstraint(
            ["language_id"],
            ["languages.id"],
            name="fk_podcast_episodes_language_id_languages",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_podcast_episodes"),
    )
    op.create_index(
        "ix_podcast_episodes_language_id_position",
        "podcast_episodes",
        ["language_id", "position"],
    )

    op.create_table(
        "phrases",
        sa.Column("id", sa.Uuid(), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("language_id", sa.Uuid(), nullable=False),
        sa.Column("kind", sa.String(length=10), nullable=False),
        sa.Column("text", sa.String(length=300), nullable=False),
        sa.Column("translation", sa.String(length=300), nullable=False),
        sa.Column("position", sa.SmallInteger(), server_default="0", nullable=False),
        sa.CheckConstraint("kind IN ('phrase', 'slang')", name="ck_phrases_kind_valid"),
        sa.ForeignKeyConstraint(
            ["language_id"],
            ["languages.id"],
            name="fk_phrases_language_id_languages",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_phrases"),
    )
    op.create_index("ix_phrases_language_id_position", "phrases", ["language_id", "position"])


def downgrade() -> None:
    op.drop_index("ix_phrases_language_id_position", table_name="phrases")
    op.drop_table("phrases")
    op.drop_index("ix_podcast_episodes_language_id_position", table_name="podcast_episodes")
    op.drop_table("podcast_episodes")
