from sqlmodel import Session, create_engine

sqilite_name = "db.sqlite3"
sqilite_url = f"sqlite:///{sqilite_name}"

engine = create_engine(sqilite_url)