from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase, Session
from sqlalchemy.orm import Session
import json
import requests
from sqlalchemy.dialects.sqlite import insert

engine = create_engine("sqlite:///Livros.db", echo=True)
cursor = engine.connect()
print(engine)

class Base(DeclarativeBase):
  ...
class Livros(Base):
    __tablename__ = 'Livros'
    id:Mapped[int] = mapped_column(primary_key=True, nullable=True)
    nome_livro:Mapped[str]=mapped_column(String(100))
    quantidade_livro:Mapped[int]=mapped_column(Integer)
    
    
    
class FuncaoBanco:
    @staticmethod
    def adicionar_dados_banco(banco:Session, livro:Livros) -> None:
        cursor.execute(insert(Livros),[
          { 'nome_livro':livro.nome_livro, 'quantidade_livro':livro.quantidade_livro}
        ])
        cursor.commit()
      
      
    @staticmethod
    def selecionar_tudo(livro:Livros)->None:
        cursor.execute(select(Livros).where(livro.id==1))
        cursor.commit()
   
    
  
  
    def buscarDados(livros:list, capitulos:list):
       
      request = requests.get("https://www.abibliadigital.com.br/api/books")
      j = json.loads(request.content)
      
      for i in range(66):
        livros.append(j[i]['name'])
        capitulos.append(j[i]['chapters'])
        print(livros[i])
        
      return livros, capitulos
    
Base.metadata.create_all(engine) 

livros= []
capitulos =[] 
FuncaoBanco.buscarDados(livros, capitulos)
l = Livros()
for i in range(66):
  l.nome_livro=livros[i]
  l.quantidade_livro=capitulos[i]
  
 
  FuncaoBanco.adicionar_dados_banco(engine, l)
  FuncaoBanco.selecionar_tudo(l)

