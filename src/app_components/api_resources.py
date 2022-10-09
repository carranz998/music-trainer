from flask_restful import Api
from utils.module import Module


class ApiResources:
    @classmethod
    def add(cls, api: Api, module_name: str, endpoint_name: str) -> None:
        class_name = endpoint_name[1].capitalize() + endpoint_name[2:]
        class_object = Module.instantiate_class(module_name, class_name)

        api.add_resource(class_object, endpoint_name)
