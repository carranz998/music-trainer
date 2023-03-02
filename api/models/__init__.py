import sqlalchemy

from ..db import engine
from .token_model import TokenModel

try:
    TokenModel.__table__.create(engine)
except sqlalchemy.exc.ProgrammingError:
    pass

__all__ = ['TokenModel']
