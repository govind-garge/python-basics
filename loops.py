######################### Loops in Python ############################

# While Loop

# simple counter loop
count = 1
while count <=5:
    print("while loop:", count)
    count+=1

# loop with list
my_list = [5,85,5,6,4]
i=0
while i<len(my_list):
    print("while loop with list:",my_list[i])
    i=i+1

# loop with break (break will terminate loop iteration)
count=1
while count <=5:
    print("while loop with break:", count)
    if(count==3):
        break
    count+=1

# loop with continue (continue will terminate current iteration)
count=1
while count <= 5:
    if(count==3):
        count+=1
        continue #skip from here
    print("while loop with coutinue:", count)
    count+=1

# For Loop

# for loop with list
my_list = [5,85,5,6,4]

for el in my_list:
    print("for loop with list:",el)

# for with else

for el in my_list:
    print("for loop with list:",el)
else:
    print("for loop with list and else, it will execute after loop end")
