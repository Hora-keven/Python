from typing import Optional
from pydantic import BaseModel


class Livros(BaseModel):
    id:Optional[int] = None
    nome_livro:str
    qt_cap:int
    
  


