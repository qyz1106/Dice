import random

def int_input(rnum):
	i = int(raw_input("How many sides do the dice have? "))
	j = int(raw_input("How many dices do you want? "))
	temp = 0
	while temp != j:
		rnum.append(random.randint(1, i))
		temp = temp + 1
	return rnum
print int_input([])