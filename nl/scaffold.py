from fastapi import FastAPI


class Scaffold:
    web: FastAPI

    web_host: str
    web_port: int

    def __init__(self, secret: str, user_id: int = -1,
                 app_name: str = 'nl-wrapper',
                 host: str = '0.0.0.0', port: int = 4354):
        self.secret = secret
        self.web_host = host
        self.web_port = port
        self.app_name = app_name
        self.user_id = user_id

    def run_web(self):
        pass
