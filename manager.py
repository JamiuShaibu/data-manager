# Gerentes de los viñedos
managers = [
{"id": 1, "tax_number": "132254524", "name": "Miguel Torres"},
{"id": 2, "tax_number": "143618668", "name": "Ana Martín"},
{"id": 3, "tax_number": "78903228", "name": "Carlos Ruiz"},
]

# Variedades de uva
grapes = [
{"id": 1, "name": "Tempranillo"},
{"id": 2, "name": "Albariño"},
{"id": 3, "name": "Garnacha"},
]

# Parcelas de los viñedos
vineyards = [
{"manager_id": 1, "vineyard_id": 1, "grape_id": 1, "year_planted": 2019, "area": 1500},
{"manager_id": 2, "vineyard_id": 2, "grape_id": 2, "year_planted": 2021, "area": 9000},
{"manager_id": 3, "vineyard_id": 1, "grape_id": 3, "year_planted": 2020, "area": 3000},
{"manager_id": 1, "vineyard_id": 2, "grape_id": 1, "year_planted": 2020, "area": 2000},
{"manager_id": 3, "vineyard_id": 2, "grape_id": 3, "year_planted": 2021, "area": 1000},
]
# Viñedos
vineyards_info = [
{"id": 1, "name": "Viña Esmeralda"},
{"id": 2, "name": "Bodegas Bilbaínas"},
]

"""
Developer: Jamiu Shaibu
Date: 04/26/2024

NOTE:
I prefer initializing parameters to the methods if they depend on external resources.
Also I prefer using "verb-noun" naming convention for my methods, I think it make the code more readable.
"""

def get_list_managers_ids(managers):
    # Extract and return a list of all managers identifiers
    return [manager["id"] for manager in managers]
    

def sorted_tax_numbers_by_manager_name(managers):
    # Sort managers by name
    sorted_managers = sorted(managers, key=lambda manager: manager["name"])
    # Extract and return list of all tax numbers from sorted managers
    return [manager["tax_number"] for manager in sorted_managers]


def get_total_area_per_grape(grapes, vineyards):
    # Here I first create a mapping of grape IDs to names
    grape_names = {grape["id"]: grape["name"] for grape in grapes}
    area_per_grape = {}
    
    for vineyard in vineyards:
        grape_id = vineyard["grape_id"]
        area = vineyard["area"]
        
        # Fetch the grape name from grape_names using the get method
        grape_name = grape_names.get(grape_id)
        
        if grape_name:
            # Update the area_per_grape dictionary with the grape area
            area_per_grape[grape_name] = area_per_grape.get(grape_name, 0) + area
            
    return area_per_grape


def get_total_area_per_manager(vineyards):
    area_per_manager = {}
    
    for vineyard in vineyards:
        manager_id = vineyard["manager_id"]
        area = vineyard["area"]
        # Update the area_per_manager dictionary
        area_per_manager[manager_id] = area_per_manager.get(manager_id, 0) + area
            
    return area_per_manager


def get_vineyards_and_managers(vineyards_info, vineyards):
    # Here I first create a mapping of vineyard IDs to names
    vineyard_names = {vineyard["id"]: vineyard["name"] for vineyard in vineyards_info}
    
    vineyards_dict = {}
    
    for vineyard in vineyards:
        vineyard_name = vineyard_names.get(vineyard["vineyard_id"])
        
        if vineyard_name:
            """
            The setdefault method handles the creation of new lists for
            vineyards that haven't been added to the dictionary yet
            """
            vineyards_dict.setdefault(vineyard_name, []).append(vineyard["manager_id"])

    # Return a sorted dictionary
    return dict(sorted(vineyards_dict.items()))
    

# Execution: \n (new line) are added just to keep the output clean and readable    
print(f"List of managers identifiers:\n{get_list_managers_ids(managers)}\n")  
print(f"List of tax numbers sorted by managers name:\n{sorted_tax_numbers_by_manager_name(managers)}\n")

# Get total area per grape
area_per_grape = get_total_area_per_grape(grapes, vineyards)
print(f"Total Area per Grape Variety:\n{area_per_grape}\n")

# Get total area per grape
area_per_manager = get_total_area_per_manager(vineyards)
print(f"Total Area Managed by Manager:\n{area_per_manager}\n")

# Get Vineyards and Their Managers
vineyards_with_managers = get_vineyards_and_managers(vineyards_info, vineyards)
print(f"Vineyards and Their Managers:\n{vineyards_with_managers}")

