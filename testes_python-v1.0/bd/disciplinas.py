class Disciplina:
    
    def __init__(self):
        self.nome = ''
        self.carga_horaria = None
        self.teoria = None
        self.pratica = None
        self.ementa = ''
        self.competencias = ''
        self.habilidades = ''
        self.conteudo = ''
        self.bibliografia_basica = ''
        self.bibliografia_complementar = ''


    def altera_nome(self,nome):
        if type(nome)== str:
            self.nome = nome
            return True
        return False

    def retorna_nome(self):
        return self.nome

    def altera_carga_horaria(self,carga_horaria):
        if type(carga_horaria) == int:
            self.carga_horaria = carga_horaria
            return True
        return False

    def altera_teoria (self,teoria):
        if type(teoria) == int :
            self.teoria = teoria
            return True
        return False

    def altera_pratica(self,pratica):
        if type(pratica)==int:
            self.pratica = pratica
            return True
        return False
    def altera_ementa(self,ementa):
        if type(ementa) == str:
            self.ementa=ementa
            return True
        return False
    def altera_competencias(self,competencias):
        if (competencias) == str:
            self.competencias = competencias
            return True
        return False

    def altera_habilidades(self,habilidades):
        if (habilidades) == str:
            self.habilidades = habilidades
            return True
        return False
    def altera_conteudo(self,conteudo):
        if (conteudo) == str:
            self.conteudo = conteudo
            return  True
        return False

    def altera_bibliografia_basica(self,bibliografia_basica):
        if(bibliografia_basica) == str:
            self.bibliografia_basica =  bibliografia_basica
            return True
        return False
    def altera_bibliografia_complementar(self,bibliografia_complementar):
        if(bibliografia_complementar) == str:
            self.bibliografia_complementar = bibliografia_complementar
            return True
        return False

    def retorna_carga_horaria(self):
        return self.carga_horaria

    def retorna_teoria(self):
        return self.teoria
    def retorna_pratica(self):
        return self.pratica
    def retorna_ementa(self):
        return self.ementa
    def retorna_competencias(self):
        return self.competencias
    def retorna_habilidades(self):
        return self.habilidades
    def retorna_conteudo(self):
        return self.conteudo
    def retorna_bibliografia_basica(self):
        return self.bibliografia_basica
    def retorna_bibliografia_complementar(self):
        return self.bibliografia_complementar