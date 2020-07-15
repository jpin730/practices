import unittest

def add(num_1, num_2):
  return abs(num_1) + num_2

class blackBoxTest(unittest.TestCase):
  def test_add_two_positives_numbers(self):
    num_1 = 10
    num_2 = 5
    result = add(num_1, num_2)
    self.assertEqual(result, 15)
  
  def test_add_two_negatives_numbers(self):
    num_1 = -9
    num_2 = -8
    result = add(num_1, num_2)
    self.assertEqual(result, -17)

if __name__ == '__main__':
  unittest.main()