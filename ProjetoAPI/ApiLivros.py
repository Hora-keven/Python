import fastapi as f
from fastapi import Depends, HTTPException, status, Response
import uvicorn
import json
import requests
import LivrosB
from LivrosB import FuncaoBanco, Livros, LivroBase, Atualiza_livro
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session, sessionmaker
app = f.FastAPI()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=LivrosB.engine)
session = LivrosB.session
cursor = LivrosB.cursor

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/livros", response_model=None, status_code=status.HTTP_201_CREATED)
async def selecionar() -> dict:
    livros = FuncaoBanco.selecionar_tudo(Livros)
    return livros


@app.get("/livros/{id}")  
def selecionar_livro_id(id) -> str:
    buscando = FuncaoBanco.selecionar_por_id(id)
    return buscando

@app.post("/cadastra_livro", tags=['Livro'])
def cadastrar_livro(livro:LivroBase) -> dict:
    
    livro_dic = {
        'nome_livro':livro.nome_livro,
        'quantidade_livro':livro.quantidade_livro
    }
    FuncaoBanco.adicionar_dados_banco(livro)
    return livro_dic

@app.put("/atualiza_livro/{id}", response_model=None, status_code=status.HTTP_201_CREATED)
async def cadastrar_livro(id:int, atualiza:Atualiza_livro = None) -> dict:
    
    livros = FuncaoBanco.selecionar_por_id(id)
    atualizando = FuncaoBanco.atualizar(atualiza)

    return atualizando



if __name__ == '__main__':
    uvicorn.run(app)