import base64


def encode_to_base64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()
