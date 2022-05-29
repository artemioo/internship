from banner_editor.models.meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
)
import bcrypt


salt = bcrypt.gensalt()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, unique=True, nullable=False)
    password = Column(Unicode(72), nullable=False)

    def __init__(self, name, password):
        password = password.encode('utf-8')
        self.name = name
        self.password = bcrypt.hashpw(password, salt)

    def validate_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

