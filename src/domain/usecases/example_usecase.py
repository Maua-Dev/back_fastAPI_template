from src.domain.errors.errors import *
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.enums.example_enum import ExampleEnum

class ExampleUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, parameter1: str, parameter2: int, parameter3: int) -> int:
        try:

            if parameter1 is None:
                raise Exception('parameter1 is None')

            try:
                evalType = ExampleEnum(parameter2)
            except Exception:
                raise Exception('parameter2 is invalid')

            if parameter3 is None:
                raise Exception('parameter3 is None')

            exampleReturn = await self._subjectRepository.getMethod(parameter1.upper())
            
            if exampleReturn is None:
                raise Exception('parameter1 is invalid')

            return await self._subjectRepository.setMethod(parameter1.upper(), parameter2,
                                                                     parameter3)

        except Exception as error:
            raise UnexpectedError('ExampleUsecase', str(error))
