from src.domain.entities.example import Example
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.infra.datasources.datasource_interface import IDataSource
from typing import List


class ExampleRepositoryImp(ISubjectRepository):
    def __init__(self, datasource: IDataSource) -> None:
        super().__init__()
        self._datasource = datasource

    async def getMethod(self, parameter1: int) -> List[Example]:
        pass

    async def setMethod(self, parameter1: int) -> List[Example]:
        pass

    async def countMethod(self,parameter1: int) -> List[Example]:
        pass
    
