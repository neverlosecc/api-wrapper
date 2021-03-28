from random import randint
from typing import TypeVar, Type

from pydantic import parse_obj_as
from requests import Session

from .exceptions import ApiException
from .models.base import BaseResponse
from .models.responses import Failed
from .scaffold import Scaffold
from .utils import signature

T = TypeVar('T')


class Requests(Scaffold):
    BASE_API_URL: str = 'https://neverlose.cc/api/'
    session: Session = Session()

    def _build_url(self, endpoint: str) -> str:
        return f'{self.BASE_API_URL}' \
               f'{"" if self.BASE_API_URL.endswith("/") else "/"}{endpoint}'

    def _generate_payload(self, data: dict) -> dict:
        data['user_id'] = self.user_id
        data['id'] = randint(111111, 999999)
        data['signature'] = signature.generate(data, self.secret)
        return data

    @staticmethod
    def _deserialize_response(data: dict, t: Type[T] = BaseResponse) -> T:
        return parse_obj_as(t, data)

    @classmethod
    def _raise_for_response(cls, raw: dict) -> bool:
        base: BaseResponse = cls._deserialize_response(raw)
        if base.success:
            return True
        err: Failed = cls._deserialize_response(raw, Failed)
        raise ApiException(str(err.error))

    def _api_request(self,
                     endpoint: str,
                     http_method: str = 'POST',
                     **data) -> bool:
        url = self._build_url(endpoint)

        data = self._generate_payload(data)
        kwargs = {('json' if http_method == 'POST' else 'params'): data}

        request = self.session.request(http_method, url, **kwargs)

        return self._raise_for_response(request.json())
