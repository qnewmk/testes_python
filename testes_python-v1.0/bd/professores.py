from pessoas import Pessoa
from usuarios import Usuario

class Professor(Pessoa,Usuario):

    def __init__(self):
        self.apalido = ''
        self.disciplinas = []

    def adiciona_disciplina(self,disciplinas):
        self.disciplinas.append(disciplinas)  
    

    def disciplinas_professor(self):
        return  self.disciplinas

    def remove_disciplina(self, disciplina):
        for d in self.disciplinas:
            if d.retorna_nome() == disciplina.retorna_nome():
                self.disciplinas.remove(d)
                break
    