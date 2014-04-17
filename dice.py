import random

def int_input(rnum):
	num = int(raw_input("How many dices do you want? "))
	for i in range(1, num):
		d[i] = raw_input("How many sides for the", i, "dice? ")
	for i in range(1, num):
		for j in range(1, d[i]):
			rnum[i][j] = random.randint(1, j)
	return rnum
print int_input([][])

#Ask user how many dices
#Ask them how many sides
#Randomize each dice
#Tell users the result