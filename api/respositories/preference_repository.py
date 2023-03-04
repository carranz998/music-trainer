from abc import ABC, abstractmethod

from ..models.sqlalchemy_preference_model import SQLAlchemyPreferencesModel
from ..postgresql_db import session


class PreferenceRepository(ABC):
    @abstractmethod
    def create_preference(self, token_id: int, band_id: int, preference_level_int):
        pass

    @abstractmethod
    def list_all_preferences(self):
        pass


class SQLAlchemyPreferencesRepository(PreferenceRepository):
    def create_preference(self, token_id: int, band_id: int, preference_level: int):
        created_preference = SQLAlchemyPreferencesModel(
            token_id, band_id, preference_level
        )

        try:
            session.add(created_preference)
            session.commit()

        except BaseException:
            session.rollback()

    def list_all_preferences(self):
        try:
            return session.query(SQLAlchemyPreferencesModel).all()

        except BaseException:
            return None
