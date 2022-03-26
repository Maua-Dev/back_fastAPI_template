from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.example_usecase import ExampleUsecase
from src.adapters.helpers.http_models import *
from src.adapters.errors.http_exception import *
from src.domain.errors.errors import *


class ExampleController:
    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._exampleUsecase = ExampleUsecase(subjectRepository)

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['parameter1'] is None or req.query['parameter1'] <= 0:
                return BadRequest(f"parameter1 is invalid. (parameter1 = {req.query['parameter1']})")

            if type(req.query['parameter1']) is not int:
                return BadRequest('parameter1 must be int.')

            parameter1 = req.query['parameter1']

            exampleReturn = await self._exampleUsecase(parameter1)

            return Ok(exampleReturn)

        except NoItemsFound as e:
            return NotFound('(ExampleController) No example found -> ' + e.message)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)