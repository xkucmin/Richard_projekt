# Bonusová úloha: Funkcia, ktorá priradí zviera ošetrovateľovi na základe jeho skúseností.

# Napíš funkciu assign_animal_to_keeper, ktorá dostane:
# - objekt zvieraťa (animal),
# - objekt ošetrovateľa (keeper),
# - zoznam vzťahov (care_relations).
#
# Ak má ošetrovateľ dostatočné skúsenosti (nastúpil pred rokom 2017), tak:
# - vytvorí nový vzťah (CaresFor),
# - pridá tento vzťah do zoznamu care_relations,
# - vypíše správu, že zviera bolo úspešne priradené.
#
# Ak ošetrovateľ nemá dostatočné skúsenosti, vypíše správu, že zviera nemôže byť priradené.
#
# Na konci vypíš aktuálny zoznam všetkých vzťahov medzi ošetrovateľmi a zvieratami.

class Keeper:
    def __init__(self, id, name, start_year):
        self.id = id
        self.name = name
        self.start_year = start_year

class Animal:
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species

class CaresFor:
    def __init__(self, keeper_id, animal_id):
        self.keeper_id = keeper_id
        self.animal_id = animal_id

def assign_animal_to_keeper(animal, keeper, care_relations):
    if keeper.start_year <= 2017:  # Skontroluje skúsenosti ošetrovateľa
        new_relation = CaresFor(keeper.id, animal.id)  # Vytvorí nový vzťah
        care_relations.append(new_relation)  # Pridá vzťah do zoznamu
        print(f"Zviera {animal.name} bolo úspešne priradené ošetrovateľovi {keeper.name}.")
    else:
        print(f"Zviera {animal.name} nemôže byť priradené ošetrovateľovi {keeper.name} pre nedostatočné skúsenosti.")

    print("\nAktuálny zoznam vzťahov:")
    for relation in care_relations:
        print(f"Ošetrovateľ ID {relation.keeper_id} sa stará o zviera ID {relation.animal_id}.")

keeper1 = Keeper(1, "Adam", 2015)
keeper2 = Keeper(2, "Ema", 2018)

animal1 = Animal(1, "Opica", "Opica")
animal2 = Animal(2, "Lev", "Lev")

care_relations = []


assign_animal_to_keeper(animal1, keeper1, care_relations)
assign_animal_to_keeper(animal2, keeper2, care_relations)