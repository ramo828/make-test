class Suallar:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    name = "Ramiz"
    surname = "Mammadli"
    age = 29

personList = []

for i in range(0,5):
   personList.append(Suallar(f"Ramiz {i}",f"Mammadli {i}",f"29 {i}"))

def person(persons):
   for person in persons:
    print(person.name)
    print(person.surname)
    print(person.age)

       
person(personList)