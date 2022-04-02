from pydantic import BaseModel
from typing import List, Optional

class ExampleModel1(BaseModel):
    attribute1: int
    attribute2: Optional[float]

class ExampleModel2(BaseModel):
    attribute1: str
    attribute2: float
    attribute3: bool
    attribute4: List[ExampleModel1]
    attribute5: List[ExampleModel1]
    attribute6: List[ExampleModel1]