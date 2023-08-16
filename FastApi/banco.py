import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
cursor.execute('create table IF NOT EXISTS pessoas (id integer primary key AUTOINCREMENT, nome text, idade integer)')

def pessoaEscolhida(id):
    pessoaEscolhida = ""  
    for pessoa in cursor.execute(f'SELECT * FROM pessoas WHERE id LIKE "%{id}%" '):
        pessoaEscolhida = pessoa

    return pessoaEscolhida


