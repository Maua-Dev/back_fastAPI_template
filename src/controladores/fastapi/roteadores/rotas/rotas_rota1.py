from fastapi import APIRouter
from src.controladores.fastapi.http.respostas import *


class RotasRota1(APIRouter):

    def __init__(self, _ctrl):

        super().__init__(prefix="/rota1", responses={404: {"description": "Not found"}})

        @self.get("/rota1", response_model=ResPadrao)
        async def rota1():
            return _ctrl.metodoControlador1()
