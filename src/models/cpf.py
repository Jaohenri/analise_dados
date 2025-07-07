class Cpf:

    def __init__(self, cpf):
        self.cpf = cpf

    #def clean_cpf(self):
        

    def validate_cpf(self):
        cpf = self.cpf = self.cpf.replace(' ', '').replace('-', '').replace('.','')
        soma_num1 = 0
        soma_num2 = 0
        num1 = 10
        num2 = 11
        if len(cpf) != 11:
            return 'CPF INVÁLIDO'
        for i in range(9):
            soma_num1 += int(cpf[i]) * num1
            num1 -= 1
        resto_num1 = (soma_num1*10)%11

        if resto_num1 == 10 :
            resto_num1 == 0      

        if resto_num1 == int(cpf[9]): 
            for i in range(10):
                soma_num2 += int(cpf[i]) * num2
                num2 -= 1
            resto_num2 = (soma_num2*10)%11

            if resto_num2 == 10:
                    resto_num2 == 0
                    
            if resto_num2 == int(cpf[10]):
                return self.cpf
            else:
                return 'CPF inválido'
                
if __name__ == '__main__':
    cpf = Cpf('64064689453')

    print(cpf.validate_cpf())
    print(type(cpf.validate_cpf()))
    


