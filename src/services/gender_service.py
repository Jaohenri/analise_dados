from src.repo.csv_repo import read_csv_file
from  src.models.people import People

def set_gender():
    for idx, row in enumerate(read_csv_file()):
        if idx == 0:
            continue
        if idx == 4:
            person = People(row[0])
            return person.gender.capitalize()
