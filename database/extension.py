from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from config import SQLite_file

Base = declarative_base()

engine = create_engine(SQLite_file)
Session = sessionmaker(bind=engine)
