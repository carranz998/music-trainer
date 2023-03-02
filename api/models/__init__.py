import sqlalchemy

from ..db import engine, Base
from .token_model import TokenModel


def create_all_tables():
    for subclass in Base.__subclasses__():
        try:
            subclass.__table__.create(engine)

        except sqlalchemy.exc.ProgrammingError as e:
            pass


create_all_tables()


__all__ = ['TokenModel']
