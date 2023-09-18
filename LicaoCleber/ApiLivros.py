import fastapi as f
import uvicorn
#from bancoSqlServer import cursor, banco
import json
from banco_livros import Livros
from funcao_banco import buscarDados


app = f.FastAPI()

livros = []
capitulos = []
dicionario_livros = []
buscarDados(livros, capitulos)

@app.get("/")
def selecionar_todos_livros():
    '''livros = cursor.execute("SELECT * FROM Livros").fetchall()
    banco.commit()'''
    for i in range(66):
        dicionario_livros[livros[i]] = capitulos[i]
    livrosZip = []
    index=0
    for linha in dicionario_livros:
        livrosZip.append(dict(zip(index, linha)))
        index+=1

    livrosJson = json.dumps(livrosZip)
    livrosJson = json.loads(livrosJson)

    return livrosJson

@app.post("/livro", tags=['livros'])  
def selecionar_livro_id(livro:Livros) -> dict:
    """
    livro = cursor.execute(f"SELECT * FROM Livros WHERE id={id}").fetchall()
    print(livro)
    banco.commit()
    coluna = [i[0] for i in cursor.description]

    livroZip = []
    for linha in livro:
        livroZip.append(dict(zip(coluna, linha)))"""
    
    livro = livro.dict()
    
    
    return 'keven'

@app.put("/livro_editado/{id}")
async def editar_livro(id):
  """  livro = cursor.execute(f"SELECT * FROM Livros WHERE id={id}").fetchall()
    coluna = [i[0] for i in cursor.description]
 
    livroZip = []
    for linha in livro:
        livroZip.append(dict(zip(coluna, linha)))
       
        return livroZip
    else:
        raise f.HTTPException(status_code=f.HTTP_409_CONFLICT, detail=f'já existe um curso com ess {id} id!')"""

if __name__ == '__main__':
    uvicorn.run(app)