from fastapi import APIRouter, Depends

from src.controladores.fastapi.http.requisicoes import *
from src.controladores.fastapi.http.respostas import *
from src.config.proj_config import ProjConfig
from src.init import Init


roteador = APIRouter(prefix="",
                     dependencies=[Depends(Init)],
                     responses={404: {"description": "Not found"}})
(_, _ctrl) = Init()()


@roteador.get("/", response_model=ResRoot)
async def root():
    req = ResRoot(
        deployment=ProjConfig.getDeployment(),
        controlador=ProjConfig.getFastapi())

    print(req)
    return req


@roteador.get("/rota1", response_model=ResPadrao)
async def rota1():
    return _ctrl.metodoControlador1()


@roteador.post("/rota2", response_model=ResArg)
async def rota2(myReq: ReqExemplo):
    return _ctrl.metodoControlador2(myReq.arg)

