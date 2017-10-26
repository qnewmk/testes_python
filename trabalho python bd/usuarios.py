class Ususario:
    def __init__ (self):
        self.r_a = ''
        self.senha = ''


    def altera_ra (self,ra):
        if type (ra) == str:
            self.r_a = ra
            return True
        return False

    def retorna_ra (self):
        return self.r_a

    def altera_senha (self, senha):
        if type(senha) == str:
            self.senha = senha
            return True
        return False


    def retorna_senha (self):
        return self.senha