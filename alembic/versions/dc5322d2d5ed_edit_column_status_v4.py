"""edit column status v4

Revision ID: dc5322d2d5ed
Revises: 5777733d98f5
Create Date: 2022-02-01 14:04:17.954544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc5322d2d5ed'
down_revision = '5777733d98f5'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('banner', sa.Column('status', sa.Enum("Enabled", "Disabled", name='status', nullable=False,
                                                          server_default=("Disabled"))))

def downgrade():
    pass
