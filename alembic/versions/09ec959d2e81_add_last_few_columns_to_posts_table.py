"""add last few columns to posts table

Revision ID: 09ec959d2e81
Revises: 52cfa56707b9
Create Date: 2022-05-26 15:19:16.091302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "09ec959d2e81"
down_revision = "52cfa56707b9"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
