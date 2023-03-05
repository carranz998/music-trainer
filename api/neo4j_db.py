from __future__ import annotations

from string import Template
from threading import Lock
from typing import Iterator, Type

from more_itertools import pairwise
from neo4j import GraphDatabase, Transaction


class ThreadSafeSingleton(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs) -> Type:
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class DatabaseConnection(metaclass=ThreadSafeSingleton):
    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        if self.driver:
            self.driver.close()

    def execute_transaction(self, query: str) -> None:
        if self.driver:
            with self.driver.session() as session:
                session.write_transaction(self.__execute_query, query)

    def __execute_query(self, tx: Transaction, query: str) -> None:
        tx.run(query)


class Neo4jQueryCreator:
    def generate_band_connections(self, bands_ids: list[int]) -> Iterator[str]:
        query = "MERGE (band1_id: Band {id: $band1_id}) MERGE (band2_id: Band {id: $band2_id}) MERGE (band1_id)-[:SIMILAR]->(band2_id)"
        template_query = Template(query)

        for band1_id, band2_id in pairwise(bands_ids):
            yield template_query.substitute(band1_id=band1_id, band2_id=band2_id)
            yield template_query.substitute(band1_id=band2_id, band2_id=band1_id)


connection = DatabaseConnection(
    uri='bolt://127.0.0.1:7687',
    user='admin',
    password='admin'
)
