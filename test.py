import unittest
import calculator

class TestCalculator(unittest.TestCase):
	def test_simple_addition(self):
		self.assertEqual(calculator.calc("5 + 5"), 10)

	def test_simple_subtraction(self):
		self.assertEqual(calculator.calc("10 - 5"), 5)

	def test_simple_multiplication(self):
		self.assertEqual(calculator.calc("5 * 5"), 25)

	def test_simple_division(self):
		self.assertEqual(calculator.calc("6 / 3"), 2)

	def test_multiple_simple_additions(self):
		self.assertEqual(calculator.calc("5 + 5 + 5"), 15)

	def test_multiple_simple_subtractions(self):
		self.assertEqual(calculator.calc("20 - 3 - 5"), 12)

	def test_multiple_simple_multiplications(self):
		self.assertEqual(calculator.calc("2 * 3 * 4"), 24)

	def test_multiple_simple_divisions(self):
		self.assertEqual(calculator.calc("20 / 2 / 5"), 2)

if __name__ == "__main__":
	unittest.main()