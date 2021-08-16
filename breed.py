import Pokemon as p
import random as rand


egg = p.Pokemon(None, None, None, None, None, None)


#TODO ---- add other item interactions (power items)
def passDownIV(p1, p2):
    p1IV = p1.IV
    p2IV = p2.IV
    rIV = 5 if p1.heldItem == 'Destiny Knot' or p2.heldItem == 'Destiny Knot' else 3
    whichIV = rand.sample(range(0,6), rIV)
    finalIV = [0,0,0,0,0,0]
    for i in whichIV:
        x = rand.randint(1,2)
        if x == 1:
            finalIV[i] = p1.IV[i]
        else: finalIV[i] = p2.IV[i]
    for i in range(0,6):
        if finalIV[i] == 0:
            finalIV[i] += rand.randint(1,31)
    egg.IV = finalIV

parent1 = p.Pokemon(None, None, 'Destiny Knot', [1,2,3,4,5,6], None, None)
parent2 = p.Pokemon(None, None, None, [7,8,9,10,11,12], None, None)


def passDownNature(p1, p2):
    return

passDownIV(parent1, parent2)






