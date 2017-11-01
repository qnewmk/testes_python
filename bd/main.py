from alunos import Aluno
from pessoas import Pessoa
from professores import Professor
from disciplinas import Disciplina
from matriculas import Matricula
#import os

aluno1 = Aluno()
aluno1.altera_celular('999999999')
aluno1.nome = 'jão'


celular_aluno = aluno1.retorno_celular()



professor1 = Professor()
professor1.nome = 'Moacir'
lp2 = Disciplina()
lp2.altera_nome('Linguagem de programação 2')

professor1.adiciona_disciplina(lp2)

lp1 = Disciplina()
lp1.altera_nome('linguagem de programação 1')
professor1.adiciona_disciplina(lp1)
lista_disciplinas = professor1.disciplinas_professor()

disciplina = Disciplina()
disciplina.altera_nome('linguagem de programação 1')
professor1.remove_disciplina(disciplina)
 

  

matricula = Matricula()

matricula.altera_aluno(aluno1)
matricula.altera_disciplina(lp2)

disciplinaAluno = matricula.retorna_disciplina()
print(disciplinaAluno.retorna_nome())
#os.system('cls')