from fastapi.testclient import TestClient

from src.controladores.fastapi.http.respostas import ResRoot
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import *
from src.main import ctrl


client = TestClient(ctrl.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ResRoot(deployment=ProjConfig.getDeployment(), controlador=ProjConfig.getFastapi())
