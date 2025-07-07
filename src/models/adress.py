#import brazilcep
import json
import requests
from src.repo.csv_repo import read_csv_file
from src.models.people import People

class Address:

    def __init__(self, cep):
        self.cep = cep
        self.cep_consultado = False
        self.observacoes = self.validate_cep()
        if self.observacoes is None:
            self.observacoes == '.'
            self.consult_by_cep()
        else:
            self.bairro = None
            self.cidade = None
            self.estado = None
            self.ddd = None
    
    def clean_cep(self):
        self.cep = self.cep.replace('-', '').replace(' ', '')

    def validate_cep(self):
        self.clean_cep()
        if len(self.cep) != 8:
            return 'CEP inválido, deve possuir 8 dígitos.'
        if not self.cep.isdigit():
            return 'CEP inválido, deve possuir apenas números.'
        return None
        

    def consult_by_cep(self):
        #cep = self.cep#
        if not self.cep_consultado:

            if self.observacoes == None:
                cep = self.cep
                url = f'https://viacep.com.br/ws/{cep}/json/'
                answer = requests.get(url)
                data = answer.json()
                self.bairro = data.get('bairro')
                self.cidade = data.get('localidade')
                self.estado = data.get('uf')
                self.ddd = data.get('ddd')

                self.cep_consultado = True

                return self.bairro, self.cidade, self.estado, self.ddd
            else:
                return self.observacoes
            
        return self.bairro, self.cidade, self.estado, self.ddd  

        

    def get_ddd(self):
        self.consult_by_cep()
        if self.observacoes == None:
            ddd = self.ddd
            return ddd
        else:
            return 'DDD não disponível, CEP inválido'
        
"""• Formato final: apenas dígitos (XXXXXXXXXXX).
• Valide dígitos verificadores; CPF inválido → nota em observacoes."""