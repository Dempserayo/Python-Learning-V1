from sqlmodel import Session, create_engine  # pyright: ignore[reportMissingImports]
from typing import Annotated
from fastapi import Depends

sqilite_name = "db.sqlite3"
sqilite_url = f"sqlite:///{sqilite_name}"

engine = create_engine(sqilite_url)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session,Depends(get_session)]