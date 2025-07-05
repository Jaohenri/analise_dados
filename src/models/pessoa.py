class Pessoa:
    def __init__(self, nome_completo):
        self.nome_completo = self.get_nome_completo(nome_completo)
        self.primeiro_nome = self.get_primeiro_nome()
        self.segundo_nome = self.get_segundo_nome()
    
    def get_nome_completo(self, nome_completo):
        return 0

    def get_primeiro_nome(self):
        return 0
    
    def get_segundo_nome(self):
        return 0