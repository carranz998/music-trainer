from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..postgresql_db import Base


class SQLAlchemyPreferencesModel(Base):
    __tablename__ = 'preferences'

    token_id = Column(Integer, ForeignKey('tokens.id'), primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'), primary_key=True)
    preference_level = Column(Integer, nullable=False)

    token = relationship('SQLAlchemyTokenModel', foreign_keys=[token_id])
    band = relationship('SQLAlchemyBandModel', foreign_keys=[band_id])

    def __init__(self, token_id: int, band_id: int, preference_level: int) -> None:
        self.token_id = token_id
        self.band_id = band_id
        self.preference_level = preference_level
