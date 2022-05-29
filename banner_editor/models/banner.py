import enum

from ..models.meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    Enum,
    String, Index,
)


class BannerStatus(enum.Enum):
    Enabled = 'Enabled'
    Disabled = 'Disabled'


class Banner(Base):
    __tablename__ = 'banner'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    image = Column(Unicode)
    url = Column(Unicode)
    status = Column(Enum(BannerStatus, name='status'),  nullable=False,  server_default='Disabled')
    position = Column(Integer, nullable=False, server_default='0')


# banner_status_index = Index('ix_banner_status', 'status')
