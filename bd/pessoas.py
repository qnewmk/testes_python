class Pessoa:

    def __init__(self, nome, celular, email):
        self.nome = ''
        self.celular = ''
        self.email = ''
    
    def altera_celular(self, celular):
        if type(celular) == str:
            self.celular = celular
            return True
        return False
    
    def retorno_celular(self):
        return self.celular

    def altera_nome (self,nome):
        if type(nome) == str:
            self.nome = nome
            return True
        return False

    def retorno_nome (self):
        return self.nome
