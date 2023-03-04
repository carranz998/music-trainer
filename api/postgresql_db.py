from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgresql_database_uri = 'postgresql://administrator:administrator@127.0.0.1/mbr'
engine = create_engine(postgresql_database_uri)

session = sessionmaker(bind=engine)()
Base = declarative_base()
