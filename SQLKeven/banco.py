import sqlite3

banco = sqlite3.connect('Faculdade.db')
cursor = banco.cursor()

'''cursor.execute('CREATE TABLE Aluno ( id_aluno INTEGER PRIMARY KEY, nome TEXT NOT NULL, matricula TEXT NOT NULL )')


cursor.execute('CREATE TABLE Curso ( id_curso INTEGER PRIMARY KEY, nome TEXT NOT NULL, Turno TEXT NOT NULL, FOREIGN KEY(id_curso) references Aluno(id_aluno),  )')'''

'''cursor.execute('CREATE TABLE Disciplina ( id_disc INTEGER PRIMARY KEY, ch TEXT NOT NULL, id_curso integer, FOREIGN KEY(id_curso) REFERENCES Curso(id_curso) )')'''


'''
lista = ['noite', 'noite', 'noite']
for i in range(len( lista)):
    cursor.execute(f'UPDATE Curso SET Turno = "{lista[i]}" WHERE id_curso = {i+1} ')'''

"""nomes = cursor.execute('SELECT * FROM Aluno WHERE id_curso = 1').fetchall()
print(nomes)"""
alunos = cursor.execute('SELECT Aluno.nome, Disciplina.nome, Disciplina.id_curso FROM Aluno INNER JOIN Disciplina ON Disciplina.nome = "POO"  ').fetchall()
print(alunos)

banco.commit()
