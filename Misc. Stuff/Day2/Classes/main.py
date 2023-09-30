#A method is a function within a class
#Attributes is data like a variable within a class
# THE SHIT METHOD:
'''class Employee:
	pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)'''



class Employee:
	#This is like the constructor, you can call self anything, but convention says self, its like the this in Java
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"
	
	#We're defining a method here
	def full_name(self):
		#The '{} {}' makes an ordered place of placeholders, we will place the first thing in format() in the first {} and so on
		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000 )
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

''' NOW USELESS
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000
'''

print(emp_1.email)
print(emp_2.email)

#This takes the object emp_1 and runs the full_name method within it, using the emp_1 attributes
print(emp_1.full_name())

#This takes the Employee CLASS method, and, treating it like a function, runs in emp_2 and its attributes
print(Employee.full_name(emp_2))

#Must leave out the .py, I could have also just imported the entire file with import example_class, but I chose to only import one function
from example_class import Cat

#Works like a normal class and object and shit!!!
cat_1 = Cat('White', 6, 'Owner')

print("Cat 1 is " + cat_1.color + " and " + str(cat_1.age) + " years old!")
print("Cat 1 says: " + Cat.say_meow(cat_1) + "!")