from flask import Flask, jsonify, request, make_response
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=CA-C-0057K\SQLEXPRESS (BR\CT67CA);DATABASE=pessoas;UID=ct67ca;PWD=s25INDUSTRIAconectada')
conn.cursor("INSER INTO pessoas (nome, idade) VALUES ('BEATRIZ', '15')")

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


@app.route('/pessoas', methods=['POST'])
def Json():
  
      return make_response(
        jsonify(pessoas))


@app.route('/pessoas/<int:id>', methods=['GET'])
def procurar_pessoas(id):

        for pessoa in pessoas:
            if id == pessoa.get('id'):
                pessoa.get('id')
                return f'O nome do id é: {pessoa.get("nome")}'
              
    
'''@app.route('/pessoas/<nome>/<int:idade>', methods=['PUT'])'''

   

app.run(port=5000, host='localhost', debug=True, threaded=False)