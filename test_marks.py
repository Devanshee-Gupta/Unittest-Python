from typing import List
from unittest import TestCase, expectedFailure, skip, main

# Different types of testcase outcomes (with use of marks)


def sum(a,b):
        return a+b

class TestOkBasic(TestCase):
    """ Basic OK outcome testcase """

    def test_sum_ok(self) -> None:
        """ Test checks if sum of 2 numbers, calculated by function is same as expected """
        a = 5
        b = 7
        expected = a+b
        result_by_func = sum(a,b)
        self.assertEqual(expected,result_by_func)


class TestSkip(TestCase):
    """ Test case outcome with skipped tests """

    @skip('Skip test without any condition')
    def test_sum_ok(self) -> None:
        """ Test checks if sum of 2 numbers, calculated by function is same as expected """
        a = 5
        b = 7
        expected = a+b
        result_by_func = sum(a,b)
        self.assertEqual(expected,result_by_func)



class TestFailBasic(TestCase):
    """ Basic FAIL test case outcome """

    def test_sum_ok(self) -> None:
        """ Test checks if sum of 2 numbers, calculated by function is same as expected """
        result_by_func = sum(7,3)
        expected = 12
        self.assertEqual(expected,result_by_func)


class TestOkExpectedFailures(TestCase):
    """ OK test case outcome with expected failures """

    @expectedFailure
    def test_sum_ok(self) -> None:
        """ Test checks if sum of 2 numbers, calculated by function is same as expected """
        result_by_func = sum(7,3)
        expected = 12
        self.assertEqual(expected,result_by_func)


class TestFailError(TestCase):
    """ FAIL test case outcome with error tests """

    def test_with_missing_one_argument(self) -> None:
        """ this test will throw error """
        self.assertEqual(0) # one argument missing in assertEqual(arg1,arg2) method


class TestFailUnexpectedSuccess(TestCase):
    """ FAIL test case outcome with unexpected success tests """

    @expectedFailure # it expects failure in test
    def test_sum_ok(self) -> None:
        """ Test checks if sum of 2 numbers, calculated by function is same as expected """
        result_by_func = sum(7,3)
        expected = 10
        self.assertEqual(expected,result_by_func) # but outcome is OK of this test -> but expected failure 
        # So, It is case of unexpected success


if __name__ == "__main__":
    main()