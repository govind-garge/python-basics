# 
############# Following is the demo of private and public attributes and methods #########################

class Students:

    #Constructor function/method(self is the default parameter to refer to the object(this))
    def __init__(self, acc_no, password):
        
        # we can declare public variable/attribute as follows
        self.acc_no=acc_no

        #we can declare private variable/attribute using 2 underscore
        self.__password=password

    # Following is the private function/method
    def __show_msg_private(self):
        msg = "this msg is from private method"
        return msg

    # Following is the public method which we can access publically
    def show_msg_public(self):
        # call internal private method
        message = self.__show_msg_private()
        return message
    
# create object of students class
student_obj = Students("223452534", "govi@#$%")

# access global variable/attribute, private variables/attributes are not accessible outside the class
print("Student pulic variable:",student_obj.acc_no)

# access global method, private methods are not accessible outside the class
print("Student pulic variable:",student_obj.show_msg_public())

######### Following is the example of attributes, methods and static method #####################################################

class Operations:
    #Constructor function/method(self is the default parameter to refer to the object(this))
    def __init__(self, a, b):
        self.a=a
        self.b=b

    # method/member function (self is same as this in other language we have to define self as a first parameter)
    def add_val(self):
        return self.a + self.b
    
    # method to get argument
    def substract_val(self, val1, val2):
        return val1 - val2
    
    # Static method - static method will not accept self parameter, it is not work as object level it will consider as class level
    @staticmethod # this is called decorator, it tells pythod that following method is static mathod
    def showmsg():
        print("this is static method output")

    @staticmethod
    def multiply(x, y):
        return x * y

object1 = Operations(10,5)
result = object1.add_val()
print("Add Result : ", result)

result = object1.substract_val(10, 2)
print("Substract Result : ", result)

object1.showmsg()

result = object1.multiply(5, 5)
print("Static methon where you dont want self paramter : ", result)

# we can delete the veriable or object using following

del object1.a

del object1

######################### inheritance in python ############################

# 1. Single inheritance
# 2. Multi-level inheritance
# 3. Multiple inheritance

# 1. Single inheritance

class Car:
    color = "black"
    def __init__(self,name):
        self.name=name

    def start(self):
        print("Single inheritance", self.name, "is started")

    
    def stop(self):
        print("Single inheritance", self.name, "is stoped")

class Tata(Car):
    def __init__(self, name):
        super().__init__(name)

carObj1 = Tata("Punch")
carObj2 = Tata("Naxon")

carObj1.start()
carObj1.stop()
carObj2.start()
carObj2.stop()

# 2. Multi-level inheritance

class Car:
    color = "black"
    def __init__(self,name):
        self.name=name

    def start(self):
        print("Multi-level inheritance", self.name, "is started")

    
    def stop(self):
        print("Multi-level inheritance", self.name, "is stoped")

class Tata(Car):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def car_type(self):
        print("Multi-level inheritance", "type of the car is:",self.type)

class Punch(Tata):
    def __init__(self, name,type):
        super().__init__(name,type)

carObj1 = Punch("Punch","CNG")
carObj2 = Punch("Naxon","Electric")

carObj1.car_type()
carObj1.start()
carObj1.stop()
carObj2.car_type()
carObj2.start()
carObj2.stop()

# 2. Multiple inheritance

class Car:
    def __init__(self, name):
        self.name = name

    def start(self):
        print("Multiple inheritance", self.name, "is started")

    def stop(self):
        print("Multiple inheritance", self.name, "is stoped")

class Tata:
    def __init__(self, type):
        # NOTE: self.type is correctly set here
        self.type = type

    def car_type(self):
        # This method now correctly accesses self.type
        print("Multiple inheritance", "type of the car is:", self.type)

class Punch(Car, Tata):
    def __init__(self, name, type):
        # 1. Explicitly call the initializer for the Car class
        Car.__init__(self, name) 
        # 2. Explicitly call the initializer for the Tata class
        Tata.__init__(self, type) 
        # Note: You can also use super() if only calling one parent, but
        # explicit calls are clearer when overriding and calling multiple parents directly.

carObj1 = Punch("Punch", "CNG")
carObj2 = Punch("Naxon", "Electric")

carObj1.car_type()
carObj1.start()
carObj1.stop()
carObj2.car_type()
carObj2.start()
carObj2.stop()

############################### Class method #################

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Govind")
print("Class method object scope Name", p1.name)
print("Class method class scope Name", Person.name)

########################### Propery ########################

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property #this method will convert percentage method to percentage attribute(variable)
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
        
stud1 = Student(98,95,99)
print("Property method result", stud1.percentage)
stud1.phy = 55
print("Property method after change result", stud1.percentage)

############################# Polymorphisam #########################

#oprator overloading

print("oprator overloading", 1 + 1)
print("oprator overloading", "string1 " + "string2")
print("oprator overloading", [1, 2, 3] + [4, 5, 6])

########################## Demo project ########################

class Bank_Account:

    def __init__(self, account_no, account_balance):
        self.account_no=account_no
        self.account_balance=account_balance

    def debit(self, amount):
        self.account_balance -= amount
        print("Rs.", amount, "has been debited from", self.account_no)
        self.total_balance()

    def credit(self, amount):
        self.account_balance += amount
        print("Rs.", amount, "has been credited to", self.account_no)
        self.total_balance()

    def total_balance(self):
        print("Total balance is:", self.account_balance)

account_obj = Bank_Account("12354751", 500)
account_obj.debit(100)
account_obj.credit(2000)
account_obj.debit(500)
account_obj.credit(1000)

