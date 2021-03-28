from hashlib import sha256

from ..types import EVENT


def _stringify_obj(obj: EVENT, secret: str) -> str:
    """
    Stringify a dictionary
    :param obj: dict object
    :param secret: secret
    :return: str
    """
    ret = ''
    for key in sorted(obj):
        if key == 'signature':
            continue
        ret = f'{ret}{key}{obj[key]}'
    return f'{ret}{secret}'


def generate(obj: EVENT, secret: str) -> str:
    """
    Generate a signature based on passed event
    :param obj: event data
    :param secret: secret
    :return: str
    """
    return sha256(_stringify_obj(obj, secret).encode()).hexdigest()


def validate(obj: EVENT, secret: str) -> bool:
    """
    Validate a signature in passed event
    :param obj: event data
    :param secret: secret
    :return: bool
    """
    return generate(obj, secret) == obj['signature']
