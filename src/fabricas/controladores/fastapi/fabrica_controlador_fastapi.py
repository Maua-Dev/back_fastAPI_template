from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from src.config.proj_config import ProjConfig
from src.config.enums.fastapi import *
from src.controladores.fastapi.c_fastapi_1 import CFastapi1
from src.controladores.fastapi.c_fastapi_2 import CFastapi2
from src.controladores.fastapi.start import Start
from src.interfaces.IRepo import IRepo
from src.controladores.fastapi.roteadores.roteador import Roteador

from src.controladores.fastapi.middleware.middleware import add_redirect_auth


class FabricaControladorFastapi:
    repo: IRepo

    __config__: dict

    protocolo: str
    host: str
    porta: str
    root: str
    url: str

    app: FastAPI

    def __init__(self, repo: IRepo):
        self.repo = repo

        self.__config__ = ProjConfig.getFastapi()

        self.protocolo = self.__config__[KEY.PROTOCOLO.value]
        self.host = self.__config__[KEY.HOST.value]
        self.porta = self.__config__[KEY.PORTA.value]
        self.root = self.__config__[KEY.ROOT.value]
        self.url = f'{self.protocolo}://{self.host}:{self.porta}{self.root}'

        self.app = FastAPI()
        self.app.add_middleware(BaseHTTPMiddleware, dispatch=add_redirect_auth)
        self.app.include_router(Roteador(self))

    def metodoControlador1(self) -> object:
        return CFastapi1(self.repo)()

    def metodoControlador2(self, arg: object) -> object:
        return CFastapi2(self.repo)(arg)

    def start(self):
        return Start()
