from flask import Flask, request, jsonify

app = Flask(__name__)

# Príklad dát pre osoby, autá a vzťahy
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Car:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class OwnsCar:
    def __init__(self, id_person, id_car):
        self.id_person = id_person
        self.id_car = id_car

# Vzory pre dáta
people = [Person(1, "Adam"), Person(2, "Eva")]
cars = [Car(1, "Toyota"), Car(2, "Honda"), Car(3, "Mazda")]
vztahy_list = [OwnsCar(1, 1), OwnsCar(1, 2), OwnsCar(2, 2)]


# Funkcia na získanie áut osoby
def get_person_car(person_id, cars, vztahy_list):
    person_cars_ids = []
    for vztah in vztahy_list:
        if vztah.id_person == person_id:
            person_cars_ids.append(vztah.id_car)
    person_cars = [car.name for car in cars if car.id in person_cars_ids]
    return person_cars


# Endpoint na volanie funkcie
@app.route('/get-person-car', methods=['POST'])
def get_person_car_endpoint():
    data = request.json  # Načítanie JSON z requestu
    person_id = data.get('person_id')

    if not person_id:
        return jsonify({"error": "Missing 'person_id' in request body"}), 400

    # Vyhľadanie osoby podľa ID
    person = next((p for p in people if p.id == person_id), None)
    if not person:
        return jsonify({"error": "Person not found"}), 404

    # Volanie funkcie a získanie výsledku
    result = get_person_car(person.id, cars, vztahy_list)
    return jsonify({"person": person.name, "cars": result})


# Endpoint na získanie všetkých áut
@app.route('/get-all-cars', methods=['GET'])
def get_all_cars():
    car_list = [{"id": car.id, "name": car.name} for car in cars]
    return jsonify({"cars": car_list})


if __name__ == '__main__':
    app.run(debug=True)