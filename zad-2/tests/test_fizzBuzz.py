import unittest
from parameterized import parameterized, parameterized_class

from modules.fizzBuzz import fizzBuzz

class Test_fizzBuzz(unittest.TestCase):
	@parameterized.expand([
		(0, "FizzBuzz"),
		(1, "1"),
		(2, "2"),
		(3, "Fizz"),
		(4, "4"),
		(5, "Buzz"),
		(6, "Fizz"),
	])
	def test_valid(self, number, expectedOutput):
		self.assertEqual(fizzBuzz(number), expectedOutput)

	@parameterized.expand([
		(set(), TypeError),
		("a", TypeError),
		([], TypeError),
	])
	def test_invalid(self, number, expectedError):
		self.assertRaises(expectedError, fizzBuzz, number)




# Dodatkowe
@parameterized_class(("number", "expectedOutput"), [
	(0, "FizzBuzz"),
	(1, "1"),
	(2, "2"),
	(3, "Fizz"),
	(4, "4"),
	(5, "Buzz"),
	(6, "Fizz"),
])
class Test2_valid_fizzBuzz(unittest.TestCase):
	def test(self):
		self.assertEqual(fizzBuzz(self.number), self.expectedOutput)

@parameterized_class(("number", "expectedError"), [
		(set(), TypeError),
		("a", TypeError),
		([], TypeError),
])
class Test2_valid_fizzBuzz(unittest.TestCase):
	def test(self):
		self.assertRaises(self.expectedError, fizzBuzz, self.number)

