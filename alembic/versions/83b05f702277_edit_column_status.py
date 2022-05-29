"""edit column status

Revision ID: 83b05f702277
Revises: 0867d329ec8c
Create Date: 2022-02-01 12:13:56.341263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from banner_editor.models.banner import MyEnumStatus

revision = '83b05f702277'
down_revision = '0867d329ec8c'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('banner', sa.Column('status', sa.Enum(MyEnumStatus, name='status'), server_default=MyEnumStatus.Disabled.value))

def downgrade():
    pass
