import fastapi as f
import uvicorn
import json
from LivrosB import FuncaoBanco
app = f.FastAPI()

livros = []
capitulos = []
FuncaoBanco.buscarDados(livros, capitulos)
dicionario_livros ={}

print(len(livros))

@app.get("/")
def selecionar_todos_livros():
    '''livros = cursor.execute("SELECT * FROM Livros").fetchall()
    banco.commit()'''

    for i in range(66):
        dicionario_livros[i] = livros[i], capitulos[i]

    livrosJson = json.dumps(dicionario_livros)
    livrosJson = json.loads(livrosJson)

    return livrosJson

@app.post("/livro", tags=['livros'])  
def selecionar_livro_id() -> dict:
    """
    livro = cursor.execute(f"SELECT * FROM Livros WHERE id={id}").fetchall()
    print(livro)
    banco.commit()
    coluna = [i[0] for i in cursor.description]

    livroZip = []
    for linha in livro:
        livroZip.append(dict(zip(coluna, linha)))"""
    
    # livro = livro.dict()
    
    
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