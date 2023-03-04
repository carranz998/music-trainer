import sqlalchemy

from ..postgresql_db import Base, engine
from .sqlalchemy_band_model import SQLAlchemyBandModel
from .sqlalchemy_preference_model import SQLAlchemyPreferencesModel
from .sqlalchemy_token_model import SQLAlchemyTokenModel


def create_all_tables():
    for subclass in Base.__subclasses__():
        try:
            subclass.__table__.create(engine)

        except sqlalchemy.exc.ProgrammingError:
            pass


create_all_tables()


__all__ = [
    'SQLAlchemyBandModel',
    'SQLAlchemyPreferencesModel',
    'SQLAlchemyTokenModel'
]
