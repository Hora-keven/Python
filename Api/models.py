from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id:[Optional] = None
    nome: str
    aulas:int
    horas:int
    instrutor:str