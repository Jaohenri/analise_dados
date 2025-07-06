"""import csv
from  models.people import People

with open("./data/lista_clientes.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for idx, row in enumerate(reader):
        if idx == 0:
            continue
        print(idx, ', '.join(row)) 
        person = People(row[0])
        print(person.full_name)
        print(person.first_name)
        print(person.second_name)"""
from src.repo.csv_repo import read_csv_file
from src.models.people import People
from src.models.adress import Address
from src.services.gender_service import set_gender
import json

for idx, row in enumerate(read_csv_file()):
    if idx == 0:
        continue
    if idx == 3:
        print(idx, ', '.join(row)) 
        person = People(row[0])
        email = row[1]
        adress = Address(row[4])
        adress.consult_by_cep()
        data = {
            'Full name' :person.full_name,
            'First name':person.first_name,
            'Second_name':person.second_name,
            'Gender':person.gender.capitalize(),
            'E-mail':email,
            'Bairro':adress.bairro,
            'Cidade':adress.cidade,
            'Estado':adress.estado,
        }

        json_string = json.dumps(data, indent=4, ensure_ascii=False)

        print(json_string)
        """print(person.full_name)
        print(person.first_name)
        print(person.second_name)"""
