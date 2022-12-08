"""
This module implements a series of test cases to confirm the
validity of the function runlog_search written in runlog_search.py
"""
import unittest
import sys
sys.path.append("..")
from src.runlog_search import search_configuration

class TestRunlogSearch(unittest.TestCase):
    """
    This class manages the tests for the function search_configuration.
    Includes one smoke tests, two one-shot tests and four edge tests.
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure the function runs.
        """
        INPUT = "A15"
        search_configuration(INPUT)

    def test_one_shot_1(self):
        """
        One-shot test to make sure the function returns
        the correct value.
        """
        INPUT = ["F15","A15","W20","N20.B","V15","H20.L", "C15.F"]
        result_test_list, result_run_num_list = \
            search_configuration(INPUT)
        correct_test_list, correct_run_num_list = \
            [2298,2298,2298], [[25.0, 26.0, 27.0, 28.0, 29.0, 30.0,
                                31.0, 32.0, 33.0, 34.0, 35.0, 55.0,
                                56.0, 57.0, 58.0, 59.0, 60.0, 61.0,
                                62.0, 63.0, 64.0, 65.0], [73.0, 74.0,
                                78.0, 79.0], [37.0, 38.0, 39.0, 40.0, 41.0]]
        assert result_test_list.sort() == correct_test_list.sort()
        assert result_run_num_list.sort() == correct_run_num_list.sort()


    def test_one_shot_2(self):
        """
        Another one-shot test to double make sure the function returns
        the correct value.
        """
        INPUT = ["F15","A15","W15", "N20.B", "V15.1","DF.1", "VF.1", "H20.L", "C18.F"]
        result_test_list, result_run_num_list = \
            search_configuration(INPUT)
        correct_test_list, correct_run_num_list = [2326], [[223.0, 225.0]]
        assert result_test_list.sort() == correct_test_list.sort()
        assert result_run_num_list.sort() == correct_run_num_list.sort()

    def test_edge_null_input(self):
        """
        An edge test to make sure the function throws ValueError when
        the input is a null list.
        """
        with self.assertRaises(ValueError):
            INPUT = []
            search_configuration(INPUT)


