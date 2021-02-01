from CustomException import IncorrectInput
import multiprocessing 

class MachineIngredients:
    
    def __init__(self,container_items):
        manager = multiprocessing.Manager()
        #creating self.container_items a sharable dictionary with every process from 
        #multiprocessing.Manager()
        self.container_items = manager.dict(container_items)
        #if container's internal ingredient are below 20% of initially filled 
        #ingredients then message will be shown that ingredient is running low 
        #please fill
        self.get_ingredient_percentage(20)
        
        
    @property
    def container_items(self):
        return self.__container_items
    
    @container_items.setter
    def container_items(self, value):
        self.__container_items = value
        
    #check whether to machine's internal ingredients are lower than 20%(20% can be changed) 
    #than the initial value
    def check_availability(self):
        for ingredient in self.container_items:
            if self.container_items[ingredient] <= self.low_percentage[ingredient]:
                    print(ingredient, "is running low please refill")
            
    #get low warning percentage with respect to initial ingredients
    def get_ingredient_percentage(self, percent):
        self.low_percentage = {}
        for ingredient in self.container_items:
            self.low_percentage[ingredient] = self.container_items[ingredient] * (percent / 100)

    # refill the intial ingredients 
    def refill(self, refill_quantity):
        for ingredient in refill_quantity:
            if isinstance(refill_quantity[ingredient],int):
                if ingredient in self.container_items:
                    self.container_items[ingredient] += refill_quantity[ingredient]
                
                else:
                    print(ingredient, 'was not initially present in container')
            else:
                raise IncorrectInput('Input is incorrect')  