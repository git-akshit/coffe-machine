import multiprocessing 
#using multi processing instead of multi tthreading because in python multi threaded code does not run in parallel
#because of GIL
from MachineIngredients import MachineIngredients
from Beverage import Beverage

class BeverageMachine:
    
    def __init__(self, outlets, machine_ingredients):
        self.outlets = outlets
        self.container_items = machine_ingredients.container_items #to store quantity of raw material
        self.machine_ingredients = machine_ingredients
        
    @property
    def outlets(self):
        return self.__outlets
    
    @outlets.setter
    def outlets(self, value):
        self.__outlets = value
        
    @property
    def container_items(self):
        return self.__container_items
    
    @container_items.setter
    def container_items(self, value):
        self.__container_items = value

    @property
    def machine_ingredients(self):
        return self.__machine_ingredients
    
    @machine_ingredients.setter
    def machine_ingredients(self, value):
        self.__machine_ingredients = value
    

    def create_beverages_from_outlets(self, beverages):
        if not isinstance(self.machine_ingredients, MachineIngredients):
            raise ValueError("machine_ingredients is not of type MachineIngredients")

        #creating a lock to synchronize the processes
        l = multiprocessing.Lock()
        
        outlets = self.outlets
        
        #getting total cores of the computer
        total_cores = multiprocessing.cpu_count()
        
        # using min to find min of total cpu cores present in computer or outlets in beverage machine
        #as total processes should not be greater than the total cpu cores
        cores = min(outlets, total_cores)
        
        #creating a pool to run process
        p = multiprocessing.Pool(cores, initializer=self.initLock, initargs=(l,))
        
        p.map(self.create_beverage, beverages)
        p.close()
        p.join()
        
        #self.machine_ingredients.container_items = self.container_items
        
        self.machine_ingredients.check_availability()
        
    def create_beverage(self, beverage):
        
        if not isinstance(beverage, Beverage):
            raise ValueError("beverage is not of type Beverage")
        
        ingredients_used = 0
        total_ingedients_required = len(beverage.ingredients)

        lock.acquire()
        #check whether the ingredients of beverage are present in machine's container
        for ingredient in beverage.ingredients:
            if ingredient not in self.container_items:
                print(beverage.name, "cannot be prepared because", ingredient, "is not available")
                lock.release()
                return 
    
        #check whether all ingredient's quantity of the beverage is present in machine's container
        for ingredient in beverage.ingredients:
            if self.container_items[ingredient] >= beverage.ingredients[ingredient]:
                ingredients_used += 1
                self.container_items[ingredient] = self.container_items[ingredient] - beverage.ingredients[ingredient]           
            else:
                print(beverage.name, "cannot be prepared because", ingredient, "is not sufficient")
                lock.release()
                return 
        
        if ingredients_used == total_ingedients_required:
            print(beverage.name, "is prepared")
        lock.release()
         
    def initLock(self,l):
        #creating a global lock which will be shared by processes
        global lock
        lock = l