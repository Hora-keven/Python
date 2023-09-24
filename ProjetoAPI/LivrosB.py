from sqlalchemy import Integer, String, create_engine, update, delete, select, bindparam
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase, Session
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import json
import requests
from sqlalchemy.dialects.sqlite import insert

engine = create_engine("sqlite:///Livros.db", echo=True)
cursor = engine.connect()
session = Session(engine)

class LivroBase(BaseModel):
   id:Optional[int]=None
   nome_livro:str
   quantidade_livro:int
   ...

class Atualiza_livro(BaseModel):
    id:Optional[int]=None
    nome_livro: Optional[str] = None
    quantidade_livro: Optional[int] = None

class Base(DeclarativeBase):
  ...
class Livros(Base):
    __tablename__ = 'Livros'
    id:Mapped[int] = mapped_column(primary_key=True, nullable=True)
    nome_livro:Mapped[str]=mapped_column(String(100))
    quantidade_livro:Mapped[int]=mapped_column(Integer)
    

    
class FuncaoBanco:
   
    @staticmethod
    def adicionar_dados_banco(livro:Livros) -> None:
        cursor.execute(insert(Livros),[
          { 'id':livro.id, 'nome_livro':livro.nome_livro, 'quantidade_livro':livro.quantidade_livro}
        ])
        cursor.commit()
      
      
    @staticmethod
    def selecionar_tudo(livro:Livros)->list:
        # cursor.execute(select(Livros).where(livro.id==1))
        # cursor.commit()
        selecionando = cursor.execute(select(Livros), [{'nome_livro':livro.nome_livro}])
        livroZip = []

        coluna = ['Id', 'nome_livro', 'quantidade_capitulos']
       

        for linha in selecionando:
            livroZip.append(dict(zip(coluna, linha)))
         
        return livroZip

    @staticmethod
    def selecionar_por_id(id:int)->str:
       
        dados = cursor.execute(select(Livros).filter(Livros.id == id)).all()
        print(dados)

        dados = [{"id":dados[0][0],
                  "nome":dados[0][1], 
                  "quantidade capitulos":dados[0][2]}]
        
    
        
        return f'{dados}'
    

    @staticmethod
    def atualizar(livro:LivroBase)->str:
     
         
        dados_atualizando = cursor.execute(update(Livros).where(Livros.id == livro.id),
                  [{ "nome_livro": livro.nome_livro, "quantidade_livro":livro.quantidade_livro},
        ])

        
        print(dados_atualizando)
        
        
        return f'{dados_atualizando}'



    def buscarDados(livros:list, capitulos:list):
      #BUscando de uma api e populando o banco de dados
      request = requests.get("https://www.abibliadigital.com.br/api/books")
      j = json.loads(request.content)
      
      for i in range(66):
        livros.append(j[i]['name'])
        capitulos.append(j[i]['chapters'])
      
      return livros, capitulos
    
Base.metadata.create_all(engine) 


l = Livros()

l = LivroBase(id=67, nome_livro="o amanhã", quantidade_livro=25)

FuncaoBanco.atualizar(l)

