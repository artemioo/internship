"""test3

Revision ID: 51ca07595d7c
Revises: a73e7485b238
Create Date: 2022-02-01 16:43:06.238971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51ca07595d7c'
down_revision = 'a73e7485b238'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('banner', sa.Column('title', server_default="test"))

def downgrade():
    pass
