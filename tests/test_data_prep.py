"""
DataPrep test script
"""
import unittest
# import numpy as np
import pandas as pd
from src import runlog_cleanup
from src import data_cleanup

# Define a class in which the tests will run
class TestDataPrep(unittest.TestCase):
    """
    Unit test class

        smoke test    = function working properly
        one shot test = function work as expected
        edge tes      = incorrect input detection
    """
#     def __init__(self):
#         """
#         initialization of data input
#         """
       # import data log
#         self.df_log2298 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2298.xlsx')
#         self.df_log2320 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2320.xlsx')
#         self.df_log2326 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2326.xlsx')
#         self.df_log2331 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2331.xlsx')
        # import data sets
#         self.df_data2298 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2298.csv')
#         self.df_data2320 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2320.csv')
#         self.df_data2326 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2326.csv')
#         self.df_data2331 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2331.csv')

    def test_runlog_cleanup_smoke(self):
        """
        smoke test

        check if the test run through
        """
#         df_log2298 = self.df_log2298
#         df_log2320 = self.df_log2320
#         df_log2326 = self.df_log2326
#         df_log2331 = self.df_log2331
        df_log2298 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2298.xlsx')
        df_log2320 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2320.xlsx')
        df_log2326 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2326.xlsx')
        df_log2331 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2331.xlsx')
        runlog_cleanup(df_log2298, df_log2320, df_log2326, df_log2331)

    def test_data_cleanup_smoke(self):
        """
        smoke test

        check if the test run through
        """
#         df_data2298 = self.df_data2298
#         df_data2320 = self.df_data2320
#         df_data2326 = self.df_data2326
#         df_data2331 = self.df_data2331
        df_data2298 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2298.csv')
        df_data2320 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2320.csv')
        df_data2326 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2326.csv')
        df_data2331 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2331.csv')
        data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331)
