from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def check_document_status(document: models.Document):
    current_date = datetime.utcnow()
    if document.status == "completed":
        return "green"
    elif current_date > document.due_date:
        return "red"
    else:
        return "yellow"

def get_documents_with_status(db: Session, skip: int = 0, limit: int = 10):
    documents = db.query(models.Document).offset(skip).limit(limit).all()
    for document in documents:
        document.status_color = check_document_status(document)
    return documents
