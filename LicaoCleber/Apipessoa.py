import fastapi
import uvicorn
from bancoLivros import cursor

app = fastapi.FastAPI()


@app.get("/")
def mensagem():
    pessoas =cursor.execute("SELECT * FROM pessoas").fetchall()
    return {pessoas}

if __name__ == '__main__':
    uvicorn.run(app)