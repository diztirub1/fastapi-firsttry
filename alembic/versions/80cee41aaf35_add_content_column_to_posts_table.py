"""add content column to posts table

Revision ID: 80cee41aaf35
Revises: e4c727dc8276
Create Date: 2022-05-26 15:03:57.277103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "80cee41aaf35"
down_revision = "e4c727dc8276"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass


# alembic current visar nuvarande revision
# alembic heads visar nyare revision om det finns
# alembic upgrade head uppgraderar till nyaste revision
# alembic downgrade -1 nedgraderar till förra revisionen
# alembic revision -m "create posts table" skapar en ny revision
