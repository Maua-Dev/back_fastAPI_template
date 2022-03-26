

from typing import Any

from src.adapters.controllers.example_controller import ExampleController
from src.domain.usecases.example_usecase import ExampleUsecase
from src.envs import Envs
from src.external.postgres.datasources.postgres_datasource import PostgresDataSource
from src.infra.repositories.example_repository_imp import ExampleRepositoryImp
from src.infra.repositories.example_repository_mock import ExampleRepositoryMock


class Modular:   
    @staticmethod
    def getInject(args: Any):
        for i in Module.getBinds():
            if(i == args or issubclass(i, args)):
                try:
                    inject = (args if i == args else i).__init__.__annotations__
                except AttributeError:
                    return i()

                if len(inject) <= 1:
                    return i()
                else:   
                    params = {}
                    for j in range(0, len(inject)-1):
                        instance = Modular.getInject(list(inject.values())[j])
                        param = list(inject.keys())[j]
                        params[param] = instance
                    return i(**params)
        return None;


class Module:
    
    @staticmethod
    def getBinds():
        return [
            ExampleRepositoryMock if Envs.IsMock() else ExampleRepositoryImp,
            PostgresDataSource,
            ExampleController,
            ExampleUsecase
        ]




    
        
