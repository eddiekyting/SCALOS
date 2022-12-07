"""
DataPrep test script
"""
import unittest
# import numpy as np
import pandas as pd
from src import DataPrep

# Define a class in which the tests will run
class TestDataPrep(unittest.TestCase):
    """
    Unit test class

        smoke test    = function working properly
        one shot test = function work as expected
        edge tes      = incorrect input detection
    """
    def __init__(self):
        """
        initialization of data input
        """
        # import data log
        self.df_log2298 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2298.xlsx')
        self.df_log2320 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2320.xlsx')
        self.df_log2326 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2326.xlsx')
        self.df_log2331 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2331.xlsx')
        # import data sets
        self.df_data2298 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2298.csv')
        self.df_data2320 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2320.csv')
        self.df_data2326 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2326.csv')
        self.df_data2331 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2331.csv')

    def test_runlog_cleanup_smoke(self):
        """
        smoke test

        check if the test run through
        """
        DataPrep.runlog_cleanup(self)

    def test_data_cleanup_smoke(self):
        """
        smoke test

        check if the test run through
        """

        DataPrep.data_cleanup(self)
