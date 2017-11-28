from alunos import Aluno
x = 's'
lista = []
while x == 's':
    nome = input('digite seu nome \n')
    celular = int(input('digite seu celular \n'))
    email = input('digite e-mail \n')
    ra = int(input('digite o seu R.A \n'))
    aluno = Aluno(nome,celular,email,ra)
    aluno.confirma_teste(ra,lista)
    lista.append(aluno.ra)
    x = input('deseja fazer denovo ? \n')
    x.lower()