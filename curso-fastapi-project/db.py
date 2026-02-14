from sqlmodel import Session, create_engine, SQLmodel  # pyright: ignore[reportMissingImports]
from typing import Annotated
from fastapi import Depends, FastAPI

sqilite_name = "db.sqlite3"
sqilite_url = f"sqlite:///{sqilite_name}"

engine = create_engine(sqilite_url)

def create_all_table(app: FastAPI):
    SQLmodel.metada.create_all(engine)    
    yield

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session,Depends(get_session)]