
import pyodbc


conn = pyodbc.connect('Driver={SQL Server};Server=CA-C-004UQ\SQLEXPRESS;Database=Pessoas;')
cursor = conn.cursor()
# comando = """INSERT INTO todasPessoas (id, nome, idade) VALUES (3,'Grasielly', 19);"""
comando = """SELECT * FROM todasPessoas"""
t = cursor.execute(comando).fetchall()
print(t)
conn.commit()
