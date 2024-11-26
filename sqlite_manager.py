from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import SQLite_file

Base = declarative_base()


class SQLiteDataManger:
    def __init__(self):
        self.engine = create_engine(SQLite_file)
        self.session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session

    # TODO: add methods for users, routines and jokes
    pass
