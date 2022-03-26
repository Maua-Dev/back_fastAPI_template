from pydantic import validator, BaseModel
from src.domain.errors.errors import EntityError


class Example(BaseModel):    
    exAttribute1: str
    exAttribute2: int

    @validator('exAttribute1')
    def exAttribute1_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('exAttribute1')
        return v.title()

    @validator('exAttribute2')
    def exAttribute2_is_not_negative(cls,v: str)-> str:
        if v < 0:
            raise EntityError('exAttribute2')
        return v