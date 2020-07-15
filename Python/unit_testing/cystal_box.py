import unittest

def isAdult(age):
  if age >= 18:
    return True
  else:
    return False

class crytalBoxTest(unittest.TestCase):
  def test_is_adult(self):
    age = 20
    result = isAdult(age)
    self.assertEqual(result, True)
  
  def test_is_not_adult(self):
    age = 15
    result = isAdult(age)
    self.assertEqual(result, False)

if __name__ == '__main__':
  unittest.main()