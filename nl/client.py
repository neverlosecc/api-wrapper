from fastapi import FastAPI
from uvicorn import run

from .eventbus import Eventbus
from .handlers import Handlers
from .methods import Methods


class Client(Methods, Handlers, Eventbus):

    def __init__(self, secret: str, user_id: int = -1,
                 app_name: str = 'nl-wrapper',
                 host: str = '0.0.0.0', port: int = 4354):
        super().__init__(secret, user_id, app_name, host, port)

        self.web = FastAPI(title=app_name, openapi_url='/api.json',
                           docs_url='/', redoc_url=None)

        self.mount_handlers()

    def run_web(self):
        run(self.web, host=self.web_host, port=self.web_port)
