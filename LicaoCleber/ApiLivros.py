import fastapi as f
import uvicorn
from bancoSqlServer import cursor, banco
import json
from banco_livros import Livros

app = f.FastAPI()

@app.get("/")
def selecionar_todos_livros():
    livros = cursor.execute("SELECT * FROM Livros").fetchall()
    banco.commit()

    coluna = [i[0] for i in cursor.description]

    livrosZip = []
    for linha in livros:
        livrosZip.append(dict(zip(coluna, linha)))

    livrosJson = json.dumps(livrosZip)
    livrosJson = json.loads(livrosJson)

    return livrosJson

@app.post("/livro")  
def selecionar_livro_id(id:int):
    livro = cursor.execute(f"SELECT * FROM Livros WHERE id={id}").fetchall()
    print(livro)
    banco.commit()
    coluna = [i[0] for i in cursor.description]
 
    livroZip = []
    for linha in livro:
        livroZip.append(dict(zip(coluna, linha)))
    
    return {"msg":'tudo certo!'}

@app.put("/livro_editado/{id}")
async def editar_livro(id):
    livro = cursor.execute(f"SELECT * FROM Livros WHERE id={id}").fetchall()
    coluna = [i[0] for i in cursor.description]
 
    livroZip = []
    for linha in livro:
        livroZip.append(dict(zip(coluna, linha)))
       
        return livroZip
    else:
        raise f.HTTPException(status_code=f.HTTP_409_CONFLICT, detail=f'já existe um curso com ess {id} id!')

if __name__ == '__main__':
    uvicorn.run(app)