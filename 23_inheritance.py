class Parent():

	def print_last_name(self):
		print('Srinivasa')

class Child(Parent):

	def print_first_name(self):
		print('Vivek')

	#def print_last_name(self):
	#	print('Darshan')

vivek = Child()
vivek.print_first_name()
vivek.print_last_name()