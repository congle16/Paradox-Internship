# Python program to
# demonstrate protected members

# Creating a base1 class
class Base1:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived1(Base1):
	def __init__(self):

		# Calling constructor of
		# Base1 class
		Base1.__init__(self)
		print("Calling protected member of base1 class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived1()

obj2 = Base1()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

# Calling protected member of base class:  2
# Calling modified protected member outside class:  3
# Accessing protected member of obj1:  3
# Accessing protected member of obj2:  2

#=================================================================================

# Python program to
# demonstrate private members

# Creating a Base class


class Base2:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived2(Base2):
	def __init__(self):

		# Calling constructor of
		# Base2 class
		Base2.__init__(self)
		print("Calling private member of base2 class: ")
		print(self.__c)


# Driver code
obj1 = Base2()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived2() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived2 class
