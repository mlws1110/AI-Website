"""Add website field to Tool model

Revision ID: <revision_id>
Revises: 5aa6a93bdf80
Create Date: 2024-XX-XX XX:XX:XX.XXXXXX

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '5aa6a93bdf80'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tool', sa.Column('website', sa.String(length=200), nullable=True))


def downgrade():
    op.drop_column('tool', 'website')