# kvadrat 0.0.1

import random

kvad = []

def randomizer(a,b):
    x = random.randrange(a,b)
    #print x
    return x

def builder():
    for j in range(1,10):
        kvad.append(j)
    print kvad
    return kvad


def blockify(k):
    for i in range(1,10):
        r = randomizer(0,10)
        if i % 3 == 0:
            print " | " + str(k[r]) + " | "
        else:
            print " | " + str(k[r]) + " | ",

builder()
blockify(kvad)
