"""edit column status v2

Revision ID: 37ac75f3711c
Revises: 83b05f702277
Create Date: 2022-02-01 12:51:43.638140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from banner_editor.models.banner import MyEnumStatus

revision = '37ac75f3711c'
down_revision = '83b05f702277'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('banner', sa.Column('status', sa.Enum(MyEnumStatus, name='status', server_default=sa.Enum((MyEnumStatus.Disabled.value)))))


def downgrade():
    pass
