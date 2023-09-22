from pydantic import BaseModel

class LivroBase(BaseModel):
    nome_livro:str
    quantidade_cap:int

class LivroRequisicao(BaseModel):
    ...
class LivroResposta(BaseModel):
    id:int
    class Config:
        orm_mode =True