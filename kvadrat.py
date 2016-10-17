# kvadrat 0.0.1

import random

def randomizer():
        x = random.randrange(0,100)
	print x
        return x

randomizer()

def rowbuilder():
	for i in range(1,99):
		if i % 3 == 0:
			print str(i) + "\n"
		else:
			print i,
	return

rowbuilder()

