import csv
from  src.models.people import People

def read_csv_file():
    with open("./data/lista_clientes.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        return list(reader)
