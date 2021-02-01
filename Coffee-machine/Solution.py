from MachineIngredients import MachineIngredients
from BeverageMachine import BeverageMachine
from Beverage import Beverage
from CustomException import IncorrectInput

class Solution:
    
    def __init__(self, JSONObject):
        self.JSONDictionary = JSONObject
        self.__beverages = []

        
    @property
    def JSONDictionary(self):
        return self.__JSONDictionary
    
    @JSONDictionary.setter
    def JSONDictionary(self, value):
        self.__JSONDictionary = value

    @property
    def refill_quantity(self):
        return self.__refill_quantity
    
    @refill_quantity.setter
    def refill_quantity(self, value):
        self.__refill_quantity = value
        
    #get the number of machine outlets
    def get_machine_outlets(self):
        outlets = self.JSONDictionary["machine"]["outlets"]["count_n"]
        return outlets
        
    #get the machine's internal container's ingredients
    def get_container_items(self):
        container_items = self.JSONDictionary["machine"]["total_items_quantity"]
        return container_items
    
    # get beverages from json
    def get_beverages(self):
        beverages = self.JSONDictionary["machine"]["beverages"]
        return beverages
        
    #create objects of classes from json
    def create_objects_from_json(self):
        outlets = self.get_machine_outlets()
        
        container_items = self.get_container_items()
        
        #check whether the value of machine's internal ingredients are int or not  
        for ingredient in container_items:
            if not isinstance(container_items[ingredient],int):
                raise IncorrectInput('Input is incorrect')
        
        beverages = self.get_beverages()
        
        #creating machine ingredients object
        self.machine_ingredients = MachineIngredients(container_items)
        
        #creating Beverage Machine object
        machine = BeverageMachine(outlets, self.machine_ingredients)

        for beverage in beverages:
            for beverage_ingredient in beverages[beverage]:
                #check whether the value of beverage's ingredients are int or not  
                if not isinstance(beverages[beverage][beverage_ingredient], int):
                    raise IncorrectInput('Input is incorrect')
                
            #creating diffrent beverages objects 
            beverage = Beverage(beverage, beverages[beverage])
            self.__beverages.append(beverage)

        #creating beverages from the machine
        machine.create_beverages_from_outlets(self.__beverages)

    def refill_beverage_machine_quantity(self,refill_quantity):
        self.machine_ingredients.refill(refill_quantity)