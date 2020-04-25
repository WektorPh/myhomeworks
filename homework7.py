# Task14

# l = [str(x) + str(x+1) for x in range(100)]
# print(l)
# # Task2
# l = [str(x) + str(x*7) for x in range(20)]
# print(l)
# 
# Task3
# import random
# import time
# l = []
# while(1):
# 	el = random.randint(0, 1000)
# 	l.append(el)
# 	m = [x * 0.621 for x in l]
# 	print(m)
# 	time.sleep(1)


# Task4
file = open('numbers.txt', 'w')


while True:
	a = int(input())
	if a != 0:
		file.write(str(a))
		print(a*2)
	if a == 0:
		break

file.close()
