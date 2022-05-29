"""test4

Revision ID: ceab834ca692
Revises: 51ca07595d7c
Create Date: 2022-02-01 16:58:01.434220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceab834ca692'
down_revision = '51ca07595d7c'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('banner', sa.Column('status', sa.Enum("Enabled", "Disabled", name='status', nullable=False,
                                                        server_default=sa.text("Disabled"))))

def downgrade():
    pass
