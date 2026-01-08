################ Range in Python ####################

# Parameters of range function: range(start,stop,step) e.g. range(1,10,1), it will give 1 to 10 with step 1

counter = range(5)

for el in counter:
    print("for loop range with stop:",el)

for el in range(1,10):
    print("for loop range start and stop:",el)

for el in range(2,11,2):
    print("for loop range start and stop and step:",el)

for el in range(10,0,-1):
    print("for loop range Reverse:",el)
