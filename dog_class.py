class Dog():

    # Class Attributes
    species = 'mammal'

    # initializer / Instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


# Initiate the Dog Object
Rocky = Dog('Rocky', 8, 'German Sheperd')
Rani = Dog('Rani', 10, 'Doberman')
Simba = Dog('Simba', 12, 'Labrador')

# Access the instance attributes
print("{} is a {} and he is {} years old.".format(Rocky.name, Rocky.breed,
                                                  Rocky.age))
print("{} is a {} and she is {} years old".format(Rani.name, Rani.breed,
                                                  Rani.age))

# Checking for mammal
if (Rocky.species == 'mammal'):
    print("{} is a {}".format(Rocky.name, Rocky.species))


# Determine the oldest dog
def get_oldest_dog(*args):
    return max(args)


# Output
print("The oldest dog is {} years old.".format(get_oldest_dog(Rocky.age, Rani.
                                                              age, Simba.age)))
