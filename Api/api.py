from flask import Flask, jsonify, request, make_response
from fastapi import HTTPException, status
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect('Driver={SQL Server};Server=CA-C-004UQ\SQLEXPRESS;Database=Pessoas;')
cursor = conn.cursor()

pessoas = [
      {
            'id':1,
           'nome':'Keven'  
      },
        {
            'id':2,
           'nome':'Maria'  
      },
        {
            'id':3,
           'nome':'Mario'  
      },
        {
            'id':4,
           'nome':'Rosimeire'  
      },
        {
            'id':5,
           'nome':'Rosana'  
      },
      ]


@app.route('/pessoas', methods=['GET'])
def Json():

  pessoas = cursor.execute("""SELECT * FROM todasPessoas""").fetchall()
  coluna = [i[0] for i in cursor.description]
  results = []
  for linha in pessoas:
    results.append(dict(zip(coluna, linha)))
  return results
  #return(dict(i))
  #t = 0
  #while True:
    #t+=1
    #return f'{i[t]}'
  
    


@app.route('/pessoas/<int:id>', methods=['POST'])
def procurar_pessoas(id):
        try:
              k = cursor.execute("SELECT * FROM todasPessoas WHERE id=", id)
              print(k)
              return k
                
        except KeyError: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
              
    
'''@app.route('/pessoas/<nome>/<int:idade>', methods=['PUT'])'''

   

app.run(port=5000, host='localhost', debug=True, threaded=False)