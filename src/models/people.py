class People:
    prepositions = ["da", "de", "do", "das", "dos", "e"]

    def __init__(self, full_name):
        self.full_name = self.get_full_name(full_name)
        self.first_name = self.get_first_name()
        self.second_name = self.get_second_name()
    
    def get_full_name(self, full_name):
        names = full_name.split()
        
        new_name = []
        for name in names:
            if name.lower() in People.prepositions: #If the name is in the list of preposition, we'll continue and do nothing with it
                new_name.append(name.lower())
                continue
            
            new_name.append(name.capitalize())   

        return ' '.join(new_name) 

    def get_first_name(self):
        first_names = self.full_name.split()
        return first_names[0]
        
    
    def get_second_name(self):
        second_names = self.full_name.split()
        if len(second_names) >= 2:
            if second_names[1] in People.prepositions:
                return second_names[2]
            else:
                return second_names[1]
        