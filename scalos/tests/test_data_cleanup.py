"""
DataPrep test script - data and run log clean up
"""
import unittest
# import numpy as np
# import sys
# sys.path.append("..")
import pandas as pd

from scalos.src import data_cleanup


# Define a class in which the tests will run
class TestDatacleanup(unittest.TestCase):
    """
    Unit test class

        smoke test    = function working properly
        one shot test = function work as expected
        edge tes      = incorrect input detection
    """
    def test_data_cleanup_smoke(self):
        """
        smoke test - function working properly
        """
#         df_data2298 = self.df_data2298
#         df_data2320 = self.df_data2320
#         df_data2326 = self.df_data2326
#         df_data2331 = self.df_data2331
        df_data2298 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2298.csv')
        df_data2320 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2320.csv')
        df_data2326 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2326.csv')
        df_data2331 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2331.csv')
        data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331)
