from typing import List

from src.domain.entities.example import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class ExampleRepositoryMock(ISubjectRepository):
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


