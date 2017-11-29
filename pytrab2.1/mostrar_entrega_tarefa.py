from alunos import Aluno

lista = []
x = 's'
while x == 's':
    nome = input('digite seu nome \n')
    celular = int(input('digite seu celular \n'))
    email = input('digite e-mail \n')
    ra = int(input('digite o seu R.A \n'))
    aluno = Aluno(nome,celular,email,ra)
    aluno.mostra_quem_fez(aluno.ra,lista)