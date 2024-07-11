from unittest import TestCase, main

class TestAssertion(TestCase):

    x = 4
    def test_sample_assert(self) -> None:
        """ 
        assertsTrue asserts if object/expression is True 
        assertsFalse asserts if object/expression is False 
        """

        self.assertTrue(1)
        self.assertFalse(0)


    def test_assertIs_IsNot(self) -> None:
        """ 
        assertIs - if one object is as an other object 
        assertIsNot - if one object is not as an other object 
        """

        # same class type as well as value 
        self.assertIs(4,4) # int == int and 4 == 4
        self.assertIs('', str()) # str == str and  '' == ''

        # opposite of assertIs 
        self.assertIsNot(4, int()) # int == int but 4 != 0



    def test_assert_logical_operations(self) -> None:
        """ Tests asserts the equality of two objects """

        # Expression1 == Expression2 
        self.assertEqual(2.22, 2.22)

        # Expression1 != Expression2 
        self.assertNotEqual(True, False)

        # Expression1 < Expression2 
        self.assertLess(2.22, 2.23)

        # Expression1 <= Expression2 
        self.assertLessEqual(2.22, 2.22)

        # Expression1 > Expression2 
        self.assertGreater(2.22, 2.21)

        # Expression1 >= Expression2 
        self.assertGreaterEqual(2.22, 2.22)


    def test_assert_contains(self) -> None:
        """ Test asserts for element membership in given container """

        # argument1 -> element and argument2 -> container
        
        self.assertIn(2, range(1, 5)) # 2 in [1,2,3,4]
        self.assertNotIn(6, range(1, 6)) # 6 not in [1,2,3,4,5]



    def test_assert_raise_error(self) -> None:
        """ Test asserts for correct raised exception """

        with self.assertRaises(ZeroDivisionError):
            print(5 / 0)


    def test_assert_nones(self) -> None:
        """ Test asserts for None objects  """

        self.assertIsNone(None)
        self.assertIsNotNone([]) # empty list - not a None object
        

    def test_assert_regex(self) -> None:
        """ Test asserts for correct regular expression functionality """

        # argument1 -> string and argument2 -> regular expression (regex) for it
        self.assertRegex('550', '\d+')
        self.assertNotRegex('500', '\s+')


    def test_assert_instances(self) -> None:
        """ Test asserts for class instances  """

        class ObjectOneClass:
            pass

        class ObjectTwoClass:
            pass

        obj1: ObjectOneClass = ObjectOneClass()
        obj2: ObjectTwoClass = ObjectTwoClass()

        self.assertIsInstance(obj1, ObjectOneClass)
        self.assertNotIsInstance(obj2, ObjectOneClass)


    def test_containers(self) -> None:
        """ Test asserts for  correct containers functionality  """

        self.assertSequenceEqual(range(4), (0, 1, 2, 3))
        self.assertListEqual(list(range(3)), [0, 1, 2])
        self.assertTupleEqual(tuple(range(2)), (0, 1))
        self.assertSetEqual(set([1,3,2,4,3]), {1, 2, 3, 4})
        self.assertDictEqual({2: 'two', 1: 'one'}, {1: 'one', 2: 'two'})


if __name__ == "__main__":
    main()

