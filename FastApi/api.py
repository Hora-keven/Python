from flask import Flask, jsonify


app = Flask(__name__)

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

@app.route('/pessoas')
def Json():
      return jsonify(pessoas)


@app.route('/pessoas/<int:id>', methods=['GET'])
def procurar_pessoas(id):
        for pessoa in pessoas:
            if id == pessoa.get('id'):
                pessoa.get('id')
                return f'O nome do id é: {pessoa.get("nome")}'
        

app.run(port=5000, host='localhost', debug=True)