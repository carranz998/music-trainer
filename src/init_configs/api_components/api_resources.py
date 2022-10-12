from flask_restful import Resource
from utils.module import Module


class ApiResources:
    @classmethod
    def instantiate(cls, module_name: str, endpoint_name: str) -> Resource:
        class_name = endpoint_name[1].capitalize() + endpoint_name[2:]
        class_object = Module.instantiate_class(module_name, class_name)

        return class_object
