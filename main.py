from classes.Animal import Animal
from classes.CaresFor import CaresFor
from classes.Keeper import Keeper
from functions.functions import get_animals_cared_by_keeper

animal1 = Animal(1,"Samo", "Slon"),
animal2 = Animal(2,"Leo", "Lev"),
animal3 = Animal(3,"Oliver", "Opica")
animals = [animal1, animal2, animal3]

keeper1 = Keeper(1, "Tomáš", "2014"),
keeper2 = Keeper(2, "Lukáš", "2016")
zookeepers = [keeper1, keeper2]

relationship1 = CaresFor(1, 1)
relationship2 = CaresFor(1, 2)
relationship3 = CaresFor(2, 3)
relationships = [relationship1, relationship2, relationship3]

get_animals_cared_by_keeper(keeper1, animals, relationships)