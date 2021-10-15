from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo
from .rotas.rotas_rota1 import RotasRota1
from .rotas.rotas_rota2 import RotasRota2



class Roteador(APIRouter):

    def __init__(self, _ctrl):

        super().__init__()

        self.include_router(RotasMssInfo())
        self.include_router(RotasRota1(_ctrl))
        self.include_router(RotasRota2(_ctrl))


