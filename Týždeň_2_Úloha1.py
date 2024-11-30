#Úloha 1
class Animal:
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species

#Úloha 2
animal1 = Animal(1,"Samo", "Slon"),
animal2 = Animal(2,"Leo", "Lev"),
animal3 = Animal(3,"Oliver", "Opica")
animals = [animal1, animal2, animal3]

#Úloha 3
class ZooKeeper:
    def __init__(self, id, name, year_started):
        self.id = id
        self.name = name
        self.year_started = year_started

#Úloha 4
keeper1 = ZooKeeper(1, "Tomáš", "2014"),
keeper2 = ZooKeeper(2, "Lukáš", "2016")
zookeepers = [keeper1, keeper2]

#Úloha 5
class CaresFor:
    def __init__(self, id_keeper, id_animal):
        self.id_keeper = id_keeper
        self.id_animal = id_animal

#Úloha 6
def get_animals_cared_by_keeper(person, animals, vztahy_list):
    person_animal_ids = []
    for vztah in vztahy_list:
        if vztah.id_keeper == person.id:
            id_animal = vztah.id_animal
            person_animal_ids.append(id_animal)
    print(person_animal_ids)
relationship1 = CaresFor(1, 1)
relationship2 = CaresFor(1, 2)
relationship3 = CaresFor(2, 3)
relationships = [relationship1, relationship2, relationship3]
get_animals_cared_by_keeper(keeper1, animals, relationships)
get_animals_cared_by_keeper(keeper2, animals, relationships)