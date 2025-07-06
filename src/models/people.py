"""This Module contaim the class People to process clients data
"""
import requests
class People:
    """Represents a person in the system.

    Returns:
        _type_: _description_
    """
    prepositions = ["da", "de", "do", "das", "dos", "e"]

    def __init__(self, full_name):
        self.full_name = self.get_full_name(full_name) 
        self.first_name = self.get_first_name()
        self.second_name = self.get_second_name()
        self.gender = self.get_gender()


    def get_full_name(self, full_name):
        """Format all names in Camel Case and prepositions in lowercase.

        Args:
            full_name (list[string]: Names from the first row of the CSV file

        Returns:
            string: Formated full name as one string
        """
        names = full_name.split()

        new_name = []
        for name in names:
            if name.lower() in People.prepositions:
                new_name.append(name.lower())
            else:
                new_name.append(name.capitalize())

        return ' '.join(new_name)

    def get_first_name(self):
        """Transform the full name in a list and return the first name

        Returns:
            string: first name from the full name
        """
        first_names = self.full_name.split()
        return first_names[0]

    def get_second_name(self):
        """Transfor the full name in a list and check if the list has more than two elements.
        Check if the second element in the name is a preposition to return the correct second name.
            
        Returns:
            string: Second name from the full name
        """
        second_names = self.full_name.split()
        if len(second_names) >= 2:
            if second_names[1] in People.prepositions:
                return second_names[2]
            else:
                return second_names[1]
        else:
            return 'Only the firs name was inserted'

    def get_gender(self):
        """Utilizes genderize.io to get the gender based on a name

        Returns:
            string: gender of a person
        """
        url = f"https://api.genderize.io/?name={self.first_name}"
        answer = requests.get(url)
        data = answer.json()
        return data.get('gender')
