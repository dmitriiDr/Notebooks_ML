class Animal:
    def __init__(self,nom, poid, taille): # to init the atributes of the class
        
        self.nom = nom
        self._poid = poid              # self is used in instance methods to access attributes and methods of the class
        self.taille = taille

    @property # converts a method into a read-only attribute (getter)
    def poid(self):
        if self._poid < 0:
            raise ValueError('Poid can not be negative')
        return self._poid
    
    @poid.setter #setter for a poid
    def poid(self,value):
        if value < 0:
            raise ValueError('Poid can not be negative')
        self._poid = value

    
    def se_deplacer(self):  # Instance method
        pass

    def __str__(self):
        return f'Type: {self.nom}, Weight: {self.poid}, Height: {self.taille}'


###########################################################
###########################################################

class Serpent(Animal): # child class
    def __init__(self, nom, poid, taille):
        super().__init__(nom, poid, taille) # Call the constructor of the parent class
    
    def se_deplacer(self): # Polymorphism
        return 'je rampe'

###########################################################
###########################################################

class Oiseau(Animal): # child class
    def __init__(self, nom, poid, taille, altitude_max):
        super().__init__(nom, poid, taille) # called the parent construct via super and changed it further by adding another variable
        self.altitude = altitude_max

    def se_deplacer(self):
        return 'je vole'

###########################################################
###########################################################

class Zoo:
    def __init__(self,animals = None):
        if animals is None:
            animals = []
        self._animals = animals

    
    def add_animal(self,animal):
        if not isinstance(animal, Animal):
            raise TypeError('Only animals !')
        self._animals.append(animal)

    
    def list_zoo(self):
        return [f'Type: {animal.nom}, Weight: {animal.poid}, Height: {animal.taille}' for animal in self._animals]
    
    
    def __add__(self,other):

        if (not isinstance(self, Zoo)) | (not isinstance(other, Zoo)):
            raise TypeError('Only animals !')
        
        pair_of_animals = self._animals + other._animals

        return Zoo(pair_of_animals)
