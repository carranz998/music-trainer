import json

from sqlalchemy import DateTime, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgresql_database_uri = 'postgresql://administrator:administrator@127.0.0.1/mbr'


def _default(val):
    if isinstance(val, DateTime):
        return str(val)
    if isinstance(val, Integer):
        return val
    raise TypeError()


def dumps(d):
    return json.dumps(d, default=_default)


engine = create_engine(postgresql_database_uri, json_serializer=dumps)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
