import re


def camel_case(string: str) -> str:
    string = re.sub(r"(_|-)+", " ", string).title().replace(" ", "")
    return string[0].lower() + string[1:]
