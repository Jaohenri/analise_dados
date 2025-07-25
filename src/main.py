
from src.repo.csv_repo import read_csv_file
from src.models.people import People
from src.models.adress import Address
from src.models.phone import Phone
from src.services.gender_service import set_gender
from src.models.cpf import Cpf
import json

for idx, row in enumerate(read_csv_file()):
    if idx == 0:
        continue
    if idx == 4:
        print(idx, ', '.join(row)) 
        person = People(row[0])
        email = row[1]
        phone = Phone(row[4],row[2])
        interest = row[5]
        cpf = Cpf(row[3])
        cpf.validate_cpf()
        adress = Address(row[4])
        adress.consult_by_cep()
        if adress.observacoes == None:
            obs = ''
        else:
            obs = adress.observacoes
        data = {
            'Full name' :person.full_name,
            'First name':person.first_name,
            'Second_name':person.second_name,
            'Gender':person.gender.capitalize(),
            'E-mail':email,
            'Telephone':phone.phone,
            'Interest':interest,
            'Cpf':cpf.cpf,
            'Bairro':adress.bairro,
            'Cidade':adress.cidade,
            'Estado':adress.estado,
            'Observations':obs
        }

        json_string = json.dumps(data, indent=4, ensure_ascii=False)

        print(json_string)
