"""rebase

Revision ID: beb6247c87a6
Revises: 94eb7fa89013
Create Date: 2022-02-01 16:28:59.512027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beb6247c87a6'
down_revision = '94eb7fa89013'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('banner', sa.Column('status', sa.Enum("Enabled", "Disabled", name='status', nullable=False,
                                                        server_default=("Disabled"))))

def downgrade():
    pass
