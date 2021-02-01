class Beverage:
    
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value):
        self.__ingredients = value