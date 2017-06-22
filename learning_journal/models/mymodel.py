from sqlalchemy import (
    Column,
    Unicode,
    Index,
    Integer,
    Text,
    Date
)

from .meta import Base


class Entry(Base):
    """."""

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    tags = Column(Unicode)
    body = Column(Unicode)
    date = Column(Date)
