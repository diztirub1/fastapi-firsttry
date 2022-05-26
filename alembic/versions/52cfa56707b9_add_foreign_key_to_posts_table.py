"""add foreign key to posts table

Revision ID: 52cfa56707b9
Revises: 3c5a2d9e5a1e
Create Date: 2022-05-26 15:14:56.285064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "52cfa56707b9"
down_revision = "3c5a2d9e5a1e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
