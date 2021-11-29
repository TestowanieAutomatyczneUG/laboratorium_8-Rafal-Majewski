import math
import re

def fizzBuzz(number: int) -> str:
	try:
		if math.isnan(number) or math.isinf(number):
			return None
		return ("" if number%3 else "Fizz")+("" if number%5 else "Buzz") or re.sub("\.0*$", "", str(number))
	except:
		raise TypeError("Modulo can't be applied to the provided input")