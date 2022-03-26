from typing import List
from sqlalchemy.future import select
from src.external.postgres.db_config_async import AsyncDBConnectionHandler
from src.infra.datasources.datasource_interface import IDataSource
from src.infra.dtos.Schema import *
from src.infra.dtos.Schema.example_dto import ExampleDTO


class PostgresDataSource(IDataSource):

    async def getMethod(self, parameter1: int) -> List[ExampleDTO]:
        pass

    async def setMethod(self, parameter1: int) -> List[ExampleDTO]:
        pass
    
    async def countMethod(self, parameter1: str) -> List[ExampleDTO]:
        pass
