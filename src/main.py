import uvicorn

from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.requisicoes import *
from src.controladores.fastapi.http.respostas import *
from src.init import Init


(_, ctrl) = Init()()


if __name__ == '__main__':

    @ctrl.app.get('/', response_model=ResRoot)
    async def root():
        req = ResRoot(
            deployment=ProjConfig.getDeployment(),
            controlador=ProjConfig.getFastapi()
        )

        print(req)
        return req


    @ctrl.app.get('/rota1', response_model=ResPadrao)
    async def rota1():
        return ctrl.metodoControlador1()


    @ctrl.app.post('/rota2', response_model=ResArg)
    async def rota2(myReq: ReqExemplo):
        return ctrl.metodoControlador2(myReq.arg)


    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.porta)
