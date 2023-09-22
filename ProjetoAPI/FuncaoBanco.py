from sqlalchemy.orm import Session

import json
import requests



class Funcoes_Banco:
    @staticmethod
    def selecionar_tudo(banco:Session)->list[Livros]:
        return banco.query(Livros).all()
    
    @staticmethod
    def salvar_dados_banco(banco:Session, livro:Livros)->Livros:
        if livro.id:
            banco.merge(livro)
        else:
            banco.add(livro)
        banco.commit()
        return livro
    
    @staticmethod
    def buscar_id(banco:Session, id:int)->Livros:
        return banco.query(Livros).filter(Livros.id == id).first()
    
    @staticmethod
    def existir_id(banco:Session, id:int)-> bool:
           return banco.query(Livros).filter(Livros.id == id).first()
    
    @staticmethod
    def deletar_id(banco:Session, id:int)-> None:
        livro = banco.query(Livros).filter(Livros.id == id).first()
        if livro is not None:
            banco.delete(livro)
            banco.commit()

  
    def buscarDados():
        livros = []
        capitulos = []
        request = requests.get("https://www.abibliadigital.com.br/api/books")
        j = json.loads(request.content)
        print(j)



Funcoes_Banco.buscarDados()
