from fastapi import APIRouter
from src.controladores.fastapi.http.requisicoes import *
from src.controladores.fastapi.http.respostas import *


class RotasRota2(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/rota2", responses={404: {"description": "Not found"}})

        @self.post("/rota2", response_model=ResArg)
        async def rota2(myReq: ReqExemplo):
            return _ctrl.metodoControlador2(myReq.arg)
