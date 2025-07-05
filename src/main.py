import csv
from  models.people import People
#def read_csv(file_path):

with open("./data/lista_clientes.csv", newline='', encoding='utf-8') as csvfile: #Opening the file as a csvfile with a utf-8 encoding
    reader = csv.reader(csvfile, delimiter=',', quotechar='"') #using csv.reader to read the file, with "," as a delimiter for data and '"' as a separator for full names, for example, if there is a file in the CSV "JOÃO, 17 years, happy" the reader will consider all in " as one element.
    for idx, row in enumerate(reader): #traversing every column in the csv file and enumerating them
        if idx == 0: #As we don't need the line with id = 0, this line ignore the following print if the condition is attended
            continue
        print(idx, ', '.join(row)) #printing the csv file with a id for each line, join to take every element in the list row, and put them in a single string, separating them with ', '
        people = People(row[0])
        print(people.full_name)
        print(people.first_name)
        print(people.second_name)
        