from hashlib import sha256

from ..constants import SECRET_FIELD
from ..types import EVENT


def _stringify_obj(obj: EVENT, secret: str):
    ret = ''
    for key in sorted(obj):
        if key == SECRET_FIELD:
            continue
        ret = f'{ret}{key}{obj[key]}'
    return f'{ret}{secret}'


def generate(obj: EVENT, secret: str):
    return sha256(_stringify_obj(obj, secret).encode()).hexdigest()


def validate(obj: EVENT, secret: str):
    return generate(obj, secret) == obj[SECRET_FIELD]
