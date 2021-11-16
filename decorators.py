# function inpython are first-class objects
# meaning, you can send them to other functions,
# or return them from other funtions

# decoratos are ways to extends a function behaviour

def my_decorator(func):
	def wrapper():
		print(".. before hi ..")
		func()
		print(".. after hi ..")
	return wrapper

@my_decorator
def say_hi():
	print("hi")

say_hi()