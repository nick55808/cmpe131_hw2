import time


def calculate_time(t):
	def wrapper():
		print("Total time", t())
	return wrapper

@calculate_time
def t():
	return time.time()

t()
