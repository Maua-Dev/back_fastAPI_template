from typing import List

from src.domain.entities.example import Example
from src.domain.repositories.example_repository_interface import IExampleRepository


class ExampleRepositoryMock(IExampleRepository):
    def __init__(self) -> None:
        super().__init__()
        self._repoMock1 = [
            {
                "column1": 9.2
                "column2": "XYZ"
                "column3": False
            },
            {
                "column1": 9.2
                "column2": "XYZ"
                "column3": False
            }
        ]
            

    async def getMethod(self, parameter1: int) -> List[Example]:
        pass

    async def setMethod(self, parameter1: int) -> List[Example]:
        pass

    async def countMethod(self,parameter1: int) -> List[Example]:
        pass


