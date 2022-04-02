from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.example import Example
from src.infra.dtos.Schema import *


class IDataSource(ABC):
    
    @abstractmethod
    async def getMethod(self, parameter1: int) -> List[Example]:
        pass
    
    @abstractmethod
    async def setMethod(self, parameter1: int) -> List[Example]:
        pass
    
    @abstractmethod
    async def countMethod(self,parameter1: int) -> List[Example]:
        pass
    
