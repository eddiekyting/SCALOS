"""
DataProcess - Data Extract test script
"""
import unittest
# import numpy as np
# import sys
# sys.path.append("..")
import pandas as pd

from scalos.src import runlog_cleanup
from scalos.src import data_cleanup
from scalos.src import data_extract

# Define a class in which the tests will run
class TestDataextract(unittest.TestCase):
    """
    Unit test class

        smoke test    = function working properly
        one shot test = function work as expected
        edge tes      = incorrect input detection
    """
    df_log2298 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort_RunLog2298.xlsx')
    df_log2320 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort_RunLog2320.xlsx')
    df_log2326 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort_RunLog2326.xlsx')
    df_log2331 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort_RunLog2331.xlsx')
    df_log = runlog_cleanup(df_log2298, df_log2320, df_log2326, df_log2331)

    df_data2298 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2298.csv')
    df_data2320 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2320.csv')
    df_data2326 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2326.csv')
    df_data2331 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2331.csv')
    df_data = data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331)
    test = [2320]
    run_num = [[50, 51, 37, 56, 57,]]

    def test_data_extract_smoke(self):
        """
        smoke test - function working properly
        """
        data_extract(self.df_log, self.df_data, self.test, self.run_num)

    def test_data_extract_one_shot1(self):
        """
        one shot test - function work as expected
        """
        data_extract(self.df_log, self.df_data, self.test, self.run_num)

    def test_data_extract_one_shot2(self):
        """
        one shot test - function work as expected
        """
        test = [2326]
        run_num = [[17, 24, 10, 31 ,38, 67,]]
        data_extract(self.df_log, self.df_data, test, run_num)

    def test_data_extract_one_shot3(self):
        """
        one shot test - function work as expected
        """
        test = [2331]
        run_num = [[40, 47, 14, 54, 61,]]
        data_extract(self.df_log, self.df_data, test, run_num)

    def test_data_extract_edge_test1(self):
        """
        edge test - incorrect input detection - string input
        """
        with self.assertRaises(ValueError):
            test = ['string']
            data_extract(self.df_log, self.df_data, test, self.run_num)

    def test_data_extract_edge_test2(self):
        """
        edge test - incorrect input detection - run_num non-list input
        """
        with self.assertRaises(ValueError):
            run_num = [50, 51, 37, 56, 57]
            data_extract(self.df_log, self.df_data, self.test, run_num)

    def test_data_extract_edge_test3(self):
        """
        edge test - incorrect input detection - empty list detection
        """
        with self.assertRaises(ValueError):
            run_num = [[50, 51], [], [37, 56, 57]]
            data_extract(self.df_log, self.df_data, self.test, run_num)

    def test_data_extract_edge_test4(self):
        """
        edge test - incorrect input detection - Test number valid
        """
        with self.assertRaises(ValueError):
            test = [2295]
            data_extract(self.df_log, self.df_data, test, self.run_num)

    def test_data_extract_edge_test5(self):
        """
        edge test - incorrect input detection - empty entry
        """
        with self.assertRaises(ValueError):
            run_num = [[50, 51], [37, None, 56, 57]]
            data_extract(self.df_log, self.df_data, self.test, run_num)

    def test_data_extract_edge_test6(self):
        """
        edge test - incorrect input detection - run_num out of range
        """
        with self.assertRaises(ValueError):
            run_num = [[300]]
            data_extract(self.df_log, self.df_data, self.test, run_num)

    def test_data_extract_edge_test7(self):
        """
        edge test - incorrect input detection - Tare run
        """
        with self.assertRaises(ValueError):
            run_num = [[47, 51, 36, 56, 57]]
            data_extract(self.df_log, self.df_data, self.test, run_num)

    def test_data_extract_edge_test8(self):
        """
        edge test - incorrect input detection - Mix run type
        """
        with self.assertRaises(ValueError):
            run_num = [[49, 51, 36, 56, 64]]
            data_extract(self.df_log, self.df_data, self.test, run_num)
