from datetime import date

class Cardinal:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True