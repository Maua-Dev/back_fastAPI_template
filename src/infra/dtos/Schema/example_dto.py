from sqlalchemy import *
from src.domain.entities.example import Example
from src.infra.dtos.db_base import Base
from sqlalchemy.orm import relationship

class ExampleDTO(Base):
    __tablename__ = 'Subjects'

    id = Column(Integer, primary_key=True)
    culumnNumber1 = Column(String, nullable=False)
    culumnNumber2 = Column(Integer, nullable=False)
    relation1 = relationship('NameDTO1',
                            cascade="all, delete",
                            passive_deletes=True,
                            backref="Subjects")
    relation2 = relationship('NameDTO2',
                              cascade="all, delete",
                              passive_deletes=True,
                              backref="Subjects"
                              )

    def exapleMethod(self) -> Subject:
        return Example(exAttribute1=self.culumnNumber1,
                       exAttribute2=self.culumnNumber2)

    def getId(self) -> int:
        return self.id

    def getculumnNumber1(self) -> str:
        return self.culumnNumber1

    def getculumnNumber2(self) -> int:
        return self.culumnNumber2