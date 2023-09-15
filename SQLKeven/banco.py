import sqlite3

banco = sqlite3.connect('Faculdade.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Aluno ( id_aluno INTEGER PRIMARY KEY, nome TEXT NOT NULL, matricula TEXT NOT NULL )')

def apagarTabela(nome):
    cursor.execute(f"DROP TABLE {nome}")
    
cursor.execute('CREATE TABLE IF NOT EXISTS Curso ( id_curso INTEGER PRIMARY KEY, nome TEXT NOT NULL, Turno TEXT NOT NULL, FOREIGN KEY(id_curso) references Aluno(id_aluno)  )')

cursor.execute('CREATE TABLE IF NOT EXISTS Disciplina ( id_disc INTEGER PRIMARY KEY,  nome TEXT NOT NULL, ch TEXT NOT NULL, id_curso integer, FOREIGN KEY(id_curso) REFERENCES Curso(id_curso) )')

def atualizaCurso():
    lista = ['noite', 'noite', 'noite']
    for i in range(len( lista)):
        cursor.execute(f'UPDATE Curso SET Turno = "{lista[i]}" WHERE id_curso = {i+1} ')
    
def adicionarDadosCursos():
    cursos = ['info', 'ELETRO', 'MEC']   
    for i in range(3):
        cursor.execute(F"INSERT INTO Curso VALUES ({i}, '{cursos[i]}', 'tarde')")
    
def adicionarDadosDisciplina():
    disciplina = ['poo', 'bd', 'digital', 'analogica', 'des tec', 'usinagem']
    for i in range(2):
        cursor.execute(f"INSERT INTO Disciplina VALUES ({i+5}, '{disciplina[i+4]}', '20', 3)")

def nomesAlunosCurso():
    nomes = cursor.execute("SELECT Aluno.nome, Disciplina.nome FROM Aluno INNER JOIN Disciplina ON Aluno.id_aluno=Disciplina.id_curso WHERE Disciplina.id_curso=1 ")
    print(nomes.fetchall())
    

def nomesAlunosDisciplina():
    nomes = cursor.execute("SELECT Aluno.nome, Disciplina.nome FROM Aluno INNER JOIN Disciplina ON Aluno.id_aluno=Disciplina.id_curso WHERE Disciplina.id_disc=1 ")
    print(nomes.fetchall())
nomesAlunosCurso()
nomesAlunosDisciplina()
# nome = ['Keven', 'maria', 'cauã', 'tereza', 'paulo', 'antonio']
# matricula = ["aluno1", 'aluno2', 'aluno3', 'aluno4', 'aluno5']
# for i in range(5):
#     cursor.execute(F"INSERT INTO Aluno VALUES ({i+1}, '{nome[i]}', '{matricula[i]}')")

# alunos = cursor.execute('SELECT Aluno.nome, Disciplina.nome, Disciplina.id_curso FROM Aluno INNER JOIN Disciplina ON Disciplina.nome = "POO"  ').fetchall()
# print(alunos)
# print(cursor.execute("SELECT Aluno.nome, Disciplina.id_curso, Disciplina.nome FROM Disciplina INNER JOIN Aluno ON Aluno.id_curso=Disciplina.id_curso WHERE Disciplina.id_curso=1"))

banco.commit()
