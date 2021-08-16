from typing import ChainMap
import Pokemon as p
import random as rand

pokeList = {'Squirtle': ['Squirtle', '0007', 'Water 1', [44, 48, 65, 50, 64, 43]],      
            'Charmander': ['Charmander', '0004', 'Dragon', [39, 52, 43, 60, 50, 65]],
            'Bulbasaur': ['Bulbasaur', '0001', 'Grass', [45, 49, 49, 65, 65, 45]]}


def spawnMon():
    pokemon = rand.choice(list(pokeList.values()))
    return p.Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[3])


spawnMon()
