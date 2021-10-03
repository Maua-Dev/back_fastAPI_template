import uvicorn

from src.cli import Cli
from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.requisicoes import *
from src.controladores.fastapi.http.respostas import *
from src.controladores.fastapi.start import Start
from src.init import Init


def main(repo:str, ctrl:str):
    (_, _ctrl) = Init()(tipo_repo=repo,tipo_ctrl=ctrl)

    @_ctrl.app.get('/', response_model=ResRoot)
    async def root():
        req = ResRoot(
            deployment=ProjConfig.getDeployment(),
            controlador=ProjConfig.getFastapi()
        )

        print(req)
        return req

    @_ctrl.app.get('/rota1', response_model=ResPadrao)
    async def rota1():
        return _ctrl.metodoControlador1()

    @_ctrl.app.post('/rota2', response_model=ResArg)
    async def rota2(myReq: ReqExemplo):
        return _ctrl.metodoControlador2(myReq.arg)

    return _, _ctrl


if __name__ == '__main__':
    cli = Cli()
    (_, ctrl) = main(repo=cli.getRepo(), ctrl=cli.getCtrl())
    Start()(app=ctrl.app, host=ctrl.host, porta=cli.getPorta())

