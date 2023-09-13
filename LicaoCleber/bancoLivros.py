import pyodbc


banco = pyodbc.connect('Driver={SQL Server};Server=CA-C-004UQ\SQLEXPRESS;Database=LivrosBiblicos;')
cursor = banco.cursor()
livros = cursor.execute('select * from Livros').fetchall()
print(livros)

def inserirLivros(id:int, livro:str, qtcap:int):
    cursor.execute(f"INSERT INTO Livros (id, titulo, qtCap) VALUES ({id}, '{livro}', {qtcap})")

inserirLivros(1, 'Genesis', 50)