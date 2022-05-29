"""edit column password

Revision ID: 0867d329ec8c
Revises: 8f2b37006d32
Create Date: 2022-02-01 10:30:33.169805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0867d329ec8c'
down_revision = '8f2b37006d32'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('users', sa.Column('password', sa.Unicode(72)))

def downgrade():
    pass