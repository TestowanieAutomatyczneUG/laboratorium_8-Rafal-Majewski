# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import json

from modules.fizzBuzz import fizzBuzz





class Test_fizzBuzz(unittest.TestCase):
	def test_from_file(self):
		file = open("./tests/fizzBuzz.json")
		testsData = json.load(file)
		file.close()
		for [input, expectedOutput] in testsData:
			self.assertEqual(fizzBuzz(input), expectedOutput)


if __name__ == "__main__":
	unittest.main()
