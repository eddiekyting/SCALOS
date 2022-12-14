"""
Data Process -  data_interp_derivative test script
"""
import unittest
# import numpy as np
# import sys
# sys.path.append("..")
import pandas as pd

from scalos.src import runlog_cleanup
from scalos.src import data_cleanup
from scalos.src import data_extract
from scalos.src import data_interp_der

# Define a class in which the tests will run
class TestDataprocess(unittest.TestCase):
    """
    Unit test class

        smoke test    = function working properly
        one shot test = function work as expected
        edge tes      = incorrect input detection
    """
    df_log2298 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort Run Log 2298.xlsx')
    df_log2320 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort Run Log 2320.xlsx')
    df_log2326 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort Run Log 2326.xlsx')
    df_log2331 = pd.read_excel(r'~/SCALOS/data/runlogs/Autosort Run Log 2331.xlsx')
    df_log = runlog_cleanup(df_log2298, df_log2320, df_log2326, df_log2331)

    df_data2298 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2298.csv')
    df_data2320 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2320.csv')
    df_data2326 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2326.csv')
    df_data2331 = pd.read_csv(r'~/SCALOS/data/finaldata_uw2331.csv')
    df_data = data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331)
    test = [2298]
    runnum = [[49, 51, 37, 56, 57, 26]]
    df_log_sub, df_data_sub = data_extract(df_log, df_data, test, runnum)

    def test_data_interp_der_smoke1(self):
        """
        smoke test

        check if the test run through
        """
        data_interp_der(self.df_log_sub, self.df_data_sub, self.test, self.runnum)

#     def test_data_interp_derivative_smoke2(self):
#         """
#         smoke test

#         check if the test run through
#         """
#         test = [2298]
#         runnum = [[49, 51, 37, 56, 57, 26]]
#         df_log_sub, df_data_sub = data_extract(self.df_log_sub, self.df_data_sub_interp, test, runnum)

#     def test_data_interp_derivative_smoke2(self):
#         """
#         smoke test

#         check if the test run through
#         """
#         test = [2298]
#         runnum = [[49, 51, 37, 56, 57, 26]]
#         df_log_sub, df_data_sub = data_extract(self.df_log_sub, self.df_data_sub_der, test, runnum)
