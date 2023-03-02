import json
from datetime import datetime
from typing import Any

from ...db import Base


class SqlAlchemyModelEncoder(json.JSONEncoder):
    def default(self, obj) -> dict[str, Any]:
        if type(obj) in Base.__subclasses__():
            data = {}

            for column in obj.__table__.columns:
                name, attribute = column.name, getattr(obj, column.name)

                if type(attribute) == datetime:
                    attribute = str(attribute)

                data[name] = attribute

            return data

        return json.JSONEncoder.default(self, obj)
