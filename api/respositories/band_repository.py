from abc import ABC, abstractmethod

from ..models import SQLAlchemyBandModel
from ..postgresql_db import session


class BandRepository(ABC):
    @abstractmethod
    def create_flowchart(self, bands_ids: list[int], **kwargs) -> None:
        pass

    @abstractmethod
    def list_all_bands(self):
        pass


class SQLAlchemyBandRepository(BandRepository):
    def create_flowchart(self, bands_ids: list[int], **kwargs) -> None:
        bands_names = kwargs['bands_names']

        for id, name in zip(bands_ids, bands_names):
            created_band = SQLAlchemyBandModel(id, name)

            try:
                session.add(created_band)
                session.commit()

            except BaseException:
                session.rollback()

    def list_all_bands(self):
        try:
            return session.query(SQLAlchemyBandModel).all()

        except BaseException:
            return None
