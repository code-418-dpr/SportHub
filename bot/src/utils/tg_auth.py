import base64


def ids_to_token(user_id: int, msg_id: int) -> str:
    bytes_token = f'{user_id}|{msg_id}'.encode()
    return base64.b64encode(bytes_token).decode()


def token_to_ids(token: str) -> tuple[int, int]:
    bytes_token = base64.b64decode(token)
    user_id, msg_id = bytes_token.split(b'|')
    return int(user_id), int(msg_id)
