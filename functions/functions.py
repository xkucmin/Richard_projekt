from classes.CaresFor import CaresFor

# táto funkcia priradi zviera osetrovatelovi, pokial dostatok skusenosti
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

# tato funkcia vrati list zvierat daneho osetrovatela
def get_animals_cared_by_keeper(person, animals, vztahy_list):
    person_animal_ids = []
    for vztah in vztahy_list:
        if vztah.id_keeper == person.id:
            id_animal = vztah.id_animal
            person_animal_ids.append(id_animal)
