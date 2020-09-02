from sqlalchemy import Column, ForeignKey, Integer, String
from app.db.base_class import Base

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
