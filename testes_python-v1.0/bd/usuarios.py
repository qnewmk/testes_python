class Usuario:
    def __init__(self):
        self.ra = ''
        self.senha =''
    
    def altera_ra(self,ra):
        if type(ra) == str:
            self.ra = ra
            return True
        return False

    def altera_senha(self, senha):
        if type(senha) == str:
            self.senha  = senha
            return True
        return False

    def retorna_ra(self):
        return self.ra

    def retorna_senha(self):
        return self.senha