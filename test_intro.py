
# Import unittest library 
import unittest

def add(a, b):
    return a+b

# Unit testing works on the model of 
# 1. Arrange 
# 2. Act 
# 3. Assert 

class Test(unittest.TestCase): # inherit the unittest.Testcase class to access its functionalities

    def test_add(self):

        #  Arrange step 
        a = 10
        b = 10
        
        # Act step
        result = add(a,b)
        expected = a + b

        # Assert step
        self.assertEqual(result,expected) # various methods availabe like assertEqual - checks if argument1 is equal to argument2


if __name__ == "__main__":
    unittest.main()