from class_animal import Animal, Oiseau, Serpent, Zoo

try:

    pet = Animal('pet',-5, 50) # create a variable to put a class elemnt in
    print(f'Weight of the animal: {pet.poid} kg')
    print(f'Height of the animal: {pet.taille} cm')
    #pet.poid = -10

except ValueError as error:
    print(error)

#####################################################
#####################################################

pet_bird = Oiseau('bird',5, 10, 100) # same for a child class

print(f'Weight of the bird: {pet_bird.poid} kg')
print(f'Height of the bird: {pet_bird.taille} cm')
print(f'The Bird says: {pet_bird.se_deplacer()} à {pet_bird.altitude} m')

######################################################
######################################################

pet_serpent = Serpent('snake', 3, 5)

print(f'Weight of the snake: {pet_serpent.poid} kg')
print(f'Height of the snake: {pet_serpent.taille} cm')
print(f'The Snake says: {pet_serpent.se_deplacer()}')

#######################################################
#######################################################

cat = Animal('cat',4,15)
dog = Animal('dog',20,50)
mouse = Animal('mouse',0.5,4)

try:

    zoo = Zoo()

    zoo.add_animal(cat)
    zoo.add_animal(dog)
    zoo.add_animal(mouse)

    full_zoo = zoo.list_zoo()

except ValueError as error:
    print(error)

print(full_zoo)

print(str(full_zoo[0]))

full_zoo = Zoo(full_zoo)

full_zoo_2 = Zoo(['tiger',500,70])

pets = full_zoo + full_zoo_2

print(type(pets))