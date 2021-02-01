from Solution import Solution

if __name__ == '__main__':
    json = {
        "machine": {
            "outlets": {
            "count_n": 3
            },
            "total_items_quantity": {
            "hot_water": 500,
            "hot_milk": 500,
            "ginger_syrup": 100,
            "sugar_syrup": 100,
            "tea_leaves_syrup": 100
            },
            "beverages": {
                "hot_tea": {
                    "hot_water": 200,
                    "hot_milk": 100,
                    "ginger_syrup": 10,
                    "sugar_syrup": 10,
                    "tea_leaves_syrup": 30
                },
                "hot_coffee": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "hot_milk": 400,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "black_tea": {
                    "hot_water": 300,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "green_tea": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "green_mixture": 30
                },
            }
        }
    }
    
    refill = {
        "hot_water": 500,
        "hot_milk": 500,
        "ginger_syrup": 100,
        "sugar_syrup": 100,
        "tea_leaves_syrup": 100
        }

    #create solution object
    object1 = Solution(json)
    #parse the json and provide solution
    object1.create_objects_from_json()
    #below method can be used to refill the container's ingredients
    object1.refill_beverage_machine_quantity(refill)
    