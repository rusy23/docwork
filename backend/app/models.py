from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    date_received = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)
    status = Column(String, default="pending")
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization")
