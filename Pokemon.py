import math
import random as rand
import uuid

natures = {'Hardy': [1,1,1,1,1,1],
           'Lonely': [1,1.1,0.9,1,1,1],
           'Brave': [1,1.1,1,1,1,0.9],
           'Adamant': [1,1.1,1,0.9,1,1],
           'Naughty': [1,1.1,1,1,0.9,1],
           'Bold': [1,0.9,1.1,1,1,1],
           'Relaxed': [1,1,1.1,1,1,0.9],
           'Impish': [1,1,1.1,0.9,1,1],
           'Lax': [1,1,1.1,1,0.9,1],
           'Timid': [1,0.9,1,1,1,1.1],
           'Hasty': [1,1,0.9,1,1,1.1],
           'Serious': [1,1,1,1,1,1],
           'Jolly': [1,1,1,0.9,1,1.1],
           'Naive': [1,1,1,1,0.9,1.1],
           'Modest': [1,0.9,1,1.1,1,1],
           'Mild': [1,1,0.9,1.1,1,1],
           'Quiet': [1,1,1,1.1,1,0.9],
           'Bashful': [1,1,1,1,1,1],
           'Rash': [1,1,1,1.1,0.9,1],
           'Calm': [1,0.9,1,1,1.1,1],
           'Gentle': [1,1,0.9,1,1.1,1],
           'Sassy': [1,1,1,1,1.1,0.9],
           'Careful': [1,1,1,0.9,1.1,1],
           'Quirky': [1,1,1,1,1,1]}


class Pokemon:
    species = None
    speciesID = None
    uniqueID = None
    name = ''
    eggGroup = None
    gender = None
    heldItem = None
    IV = [0,0,0,0,0,0]
    nature = None
    moves = []
    baseStats = [1,1,1,1,1,1]
    stats = [0,0,0,0,0,0]
    EV = [0,0,0,0,0,0]
    level = 1


    def __init__(self, species, speciesID, eggGroup, baseStats) -> None:
        global natures
        self.species = species
        self.speciesID = speciesID
        self.baseStats = baseStats
        self.eggGroup = eggGroup
        self.uniqueID = uuid.uuid4()
        self.gender = rand.choice(['Male', 'Female'])
        for i in range(6):
            self.IV[i] = rand.randint(0,31)
        self.nature = rand.choice(list(natures.keys()))
        self.calculateStats()

#TODO --- add in the nature calculation
    def calculateStats(self):
        print('Calculating Stats')
        global natures
        calcNature = natures[self.nature]
        self.stats[0] = math.floor((((2 * self.baseStats[0]) + self.IV[0] + (self.EV[0]/4)) * self.level)/100 + self.level + 10)
        for i in range(1,6):
            self.stats[i] = math.floor(((((2 * self.baseStats[i]) + self.IV[i] + (self.EV[i]/4)) * self.level)/100 + 5) * calcNature[i])


    def printPokemon(self):
        print('Species: ' + self.species)
        print('Nickname: ' + self.name)
        print('Egg group: ' + self.eggGroup)
        print('Gender: ' + self.gender)
        if self.heldItem:
            print('Held item: ' + self.heldItem)
        else:
            print('Held item: None') 
        print('IV\'s: ')
        print('HP: ' + str(self.IV[0]))
        print('Atk: ' + str(self.IV[1]))
        print('Def: ' + str(self.IV[2]))
        print('SpA: ' + str(self.IV[3]))
        print('SpD: ' + str(self.IV[4]))
        print('Spe: ' + str(self.IV[5]))
        print('Nature: ' + self.nature)
        if self.moves:
            print('Known moves: ' + self.moves)
        else:
            print('This pokemon doesn\'t know any moves.')


    def printStats(self):
        print(str(self.stats))
    
