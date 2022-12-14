"""
Data Process -  data_interp_derivative test script (omitted)
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
from scalos.src import data_plt

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
    run_num = [[49, 51, 37, 56, 57, 26]]
    df_log_sub, df_data_sub = data_extract(df_log, df_data, test, run_num)
    df_data_sub_interp, df_data_sub_der = data_interp_der(df_log_sub, df_data_sub, test, run_num)
    plot_vars = ["CLSA", "CDSA", "CYSA", "CMSA25", "CNSA25", "CRSA25", "LOD"]

#     def test_data_plt_smoke1(self):
#         """
#         smoke test

#         check if the test run through
#         """
#         data_plt(self.plot_vars, self.df_log_sub, self.df_data_sub, self.test, self.run_num)

#     def test_data_plt_smoke2(self):
#         """
#         smoke test

#         check if the test run through
#         """
#         data_plt(self.plot_vars, self.df_log_sub, self.df_data_sub_interp, self.test, self.run_num)

#     def test_data_plt_smoke3(self):
#         """
#         smoke test

#         check if the test run through
#         """
#         data_plt(self.plot_vars, self.df_log_sub, self.df_data_sub_der, self.test, self.run_num)