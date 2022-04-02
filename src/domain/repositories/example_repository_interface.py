from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.example import Example


class IExampleRepository(ABC):

    @abstractmethod
    async def getMethod(self, parameter1: int) -> Example:    
        pass
    
    @abstractmethod
    async def setMethod(self, parameter1: int) -> None:    
        pass
    
    @abstractmethod
    async def countMethod(self, parameter1: str) -> int:    
        pass
