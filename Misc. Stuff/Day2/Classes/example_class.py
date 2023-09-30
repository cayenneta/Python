#I will import this into another file!
class Cat:
	def __init__(self, color, age, owner):
		self.color = color
		self.age = age
		self.owner = owner
	def say_meow(self):
		return 'Meow {} meow'.format(self.owner)