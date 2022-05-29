"""edit column status v3

Revision ID: 5777733d98f5
Revises: 37ac75f3711c
Create Date: 2022-02-01 13:55:36.176577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from banner_editor.models.banner import MyEnumStatus

revision = '5777733d98f5'
down_revision = '37ac75f3711c'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('banner', sa.Column('status', sa.Enum(MyEnumStatus, name='status', nullable=False,
                                                          server_default=("Disabled"))))


def downgrade():
    pass
