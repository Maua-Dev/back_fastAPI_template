from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from src.adapters.controllers.example_controller import ExampleController
from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest
from src.main.subjects.module import Modular
from src.main.helpers.status import status as st

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HttpException)
async def internal_exception_handler(request: Request, exc: HttpException):

    return PlainTextResponse(exc.body, status_code=exc.status_code)

@app.get("/example/{parameter1}")
async def getMethod(response: Response):

    exampleController = Modular.getInject(ExampleController)
    req = HttpRequest(query={"parameter1": parameter1})
    result = await exampleController(req)
    response.status_code = st.get(result.status_code)
    return result

