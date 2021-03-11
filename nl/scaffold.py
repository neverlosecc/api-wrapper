from fastapi import FastAPI
from requests import Session  # TODO: Httpx?


class Scaffold:
    session: Session = Session()
    web: FastAPI

    web_host: str
    web_port: int

    def __init__(self, secret: str, app_name: str = 'nl-wrapper',
                 host: str = '0.0.0.0', port: int = 1337):
        self.secret = secret

    def run_web(self):
        pass
