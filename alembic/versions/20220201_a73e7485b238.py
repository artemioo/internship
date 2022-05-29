"""test2

Revision ID: a73e7485b238
Revises: beb6247c87a6
Create Date: 2022-02-01 16:39:59.667969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a73e7485b238'
down_revision = 'beb6247c87a6'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('banner', sa.Column('title', server_default="test"))

def downgrade():
    pass
