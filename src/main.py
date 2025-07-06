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
from src.services.gender_service import set_gender
import json

for idx, row in enumerate(read_csv_file()):
    if idx == 0:
        continue
    if idx == 1:
        print(idx, ', '.join(row)) 
        person = People(row[0])
        email = People(row[1])
        data = {
            'Full name' :person.full_name,
            'First name':person.first_name,
            'Second_name':person.second_name,
            'Gender':person.gender.capitalize()
        }

        json_string = json.dumps(data, indent=4, ensure_ascii=False)

        print(json_string)
        """print(person.full_name)
        print(person.first_name)
        print(person.second_name)"""
