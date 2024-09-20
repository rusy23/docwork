from pydantic import BaseModel
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    content: str
    due_date: datetime

class DocumentCreate(DocumentBase):
    organization_id: int

class Document(DocumentBase):
    id: int
    date_received: datetime
    status: str

    class Config:
        orm_mode = True
