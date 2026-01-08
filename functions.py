######################## Functions in Python ###############################################

# Define the function using def keyword e.g. sum(param1, param2):

def sum(a, b):
    return a+b

print("Function output:",sum(10,5))


#Function with default values
def default_sum(a=1, b=1):
    return a+b

print("Function output:",default_sum())

#factorial number
def cal_factorial(n=1):
    i=1
    factorial=1
    while i <= n:
        factorial = factorial*i
        i += 1
    return factorial

n=5
print("Factorial Function output:",cal_factorial(n))

# function recursion
def my_recursion(n):
    #base case condition to stop the recursion
    if(n==0):
        return
    print("Recursion function:",n)
    my_recursion(n-1)

my_recursion(5)

# factorial with recursion (it use the call stack memory so it will go till 1 and return the value and multiple with n )
def my_recursion(n):
    #base case condition to stop the recursion
    if(n==0 or n== 1):
        return 1
    return my_recursion(n-1) * n

print("Factorial with Recursion function final output:", my_recursion(5))
