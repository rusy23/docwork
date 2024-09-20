from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/documents/", response_model=schemas.Document)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(database.get_db)):
    return crud.create_document(db=db, document=document)

@app.get("/documents/", response_model=list[schemas.Document])
def read_documents(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_documents_with_status(db, skip=skip, limit=limit)
