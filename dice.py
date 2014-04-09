import random
def int_input(rnum):
	i = int(raw_input("How many sides do the dice have? "))
	rnum = random.randint(1, i)
	return rnum
print int_input(0)