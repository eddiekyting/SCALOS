"""
DataPrep: Data pre-process and preperation for manipulation and process

parameters:
    arg df_logXXXX:  data log with entry numbers (.xlsx file)

    arg df_dataXXXX: data set with entry numbers (.xlsx file)

return:
    df_logXXXX:  Cleaned up test data sets( data frame)

    df_log:      Concatinated data logs (data frame)

    df_data:     Concatinated data sets (data frame)
"""

import numpy as np
import pandas as pd

# class DataPrep:

#     """
#     function: runlog_cleanup

#         clean up and align variables

#     function: data_cleanup

#         check data sets and concatinate them into single data set
#     """
#     def __init__(self):
#         """
#         function:
#             initialization of variables

#         parameters:
#             arg df_log:  Data log from data_prep output (data frame)

#             arg df_data: Data set from data_prep output (data frame)

#             arg test:    Test entries (list)

#             arg run_num: Run numbers correspondign to test entires (list)

#         return:
#             data logs and sets
#         """
#         # import data log
#         self.df_log2298 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2298.xlsx')
#         self.df_log2320 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2320.xlsx')
#         self.df_log2326 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2326.xlsx')
#         self.df_log2331 = pd.read_excel(r'~/SCALOS/project/runlogs/Autosort Run Log 2331.xlsx')
#         # import data sets
#         self.df_data2298 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2298.csv')
#         self.df_data2320 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2320.csv')
#         self.df_data2326 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2326.csv')
#         self.df_data2331 = pd.read_csv(r'~/SCALOS/project/data/finaldata_uw2331.csv')


def runlog_cleanup(df_log2298, df_log2320, df_log2326, df_log2331):
    """
    function:
        runlog_cleanup

    parameters:
        arg df_logXXXX = data log with entry numbers (.xlsx file)

    return:
        df_log:     Concatinate data log from inputs

        df_logXXXX: Clean up individual data logs
    """
#         df_log2298 = self.df_log2298
#         df_log2320 = self.df_log2320
#         df_log2326 = self.df_log2326
#         df_log2331 = self.df_log2331
# clean up uw2298
    # delete unncessary column
    del df_log2298["Riley's Stress Level"]
    # rename entries titles
    df_log2298.rename(columns = {'FLAP L/R':'IB FLAP L/R'}, inplace = True)
    df_log2298.rename(columns = {'AIL L/R':'OB AIL L/R'}, inplace = True)
    df_log2298.rename(columns = {'LE DEF':'LE IB/OB'}, inplace = True)
    df_log2298.rename(columns = {'TRIP DEF':'TRIP DOTS'}, inplace = True)
    # add enties
    df_log2298.insert(1,'TEST', 2298)
    df_log2298['Nacelle Blockage L/R']= np.nan
    df_log2298['Spoiler L/R']= np.nan
    temp = df_log2298['DATE']
    del df_log2298['DATE']
    df_log2298['DATE']= temp
    df_log2298.columns.tolist()

# clean up uw2320
    # rename entries titles
    df_log2320.rename(columns = {'FLAP L/R':'IB FLAP L/R'}, inplace = True)
    df_log2320.rename(columns = {'AIL L/R':'OB AIL L/R'}, inplace = True)
    df_log2320.rename(columns = {'TRIP DEF':'TRIP DOTS'}, inplace = True)
    # add enties
    df_log2320.insert(1,'TEST', 2320)
    df_log2320['Nacelle Blockage L/R']= np.nan
    df_log2320['Spoiler L/R']= np.nan
    temp = df_log2320['DATE']
    del df_log2320['DATE']
    df_log2320['DATE']= temp

# clean up uw2326
    # add enties
    df_log2326.insert(1,'TEST', 2326)
    df_log2326['Nacelle Blockage L/R']= np.nan
    df_log2326['Spoiler L/R']= np.nan
    temp = df_log2326['DATE']
    del df_log2326['DATE']
    df_log2326['DATE']= temp

# clean up uw2331
    df_log2331.insert(1,'TEST', 2331)

    # column title are consistant
    if df_log2298.columns.tolist() !=  df_log2320.columns.tolist():
        raise ValueError("Either 2298 or 2320 data is not right!")

    if df_log2298.columns.tolist() !=  df_log2326.columns.tolist():
        raise ValueError("Either 2298 or 2326 data is not right!")

    if df_log2298.columns.tolist() !=  df_log2331.columns.tolist():
        raise ValueError("Either 2298 or 2331 data is not right!")

    # Concatinate all run logs into single data frame
    df_log = pd.concat([df_log2298,
                        df_log2320,
                        df_log2326,
                        df_log2331],
                       ignore_index=True,axis=0)

    return df_log

def data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331):
    """
    function:
        data_cleanup

    parameters:
        arg df_dataXXXX = data set with entry numbers (.xlsx file)

    return:
        df_set:     Concatinate data sets from inputs
    """
#         df_data2298 = self.df_data2298
#         df_data2320 = self.df_data2320
#         df_data2326 = self.df_data2326
#         df_data2331 = self.df_data2331

    if df_data2298.columns.tolist() !=  df_data2320.columns.tolist():
        raise ValueError("Either 2298 or 2320 data is not right!")

    if df_data2298.columns.tolist() !=  df_data2326.columns.tolist():
        raise ValueError("Either 2298 or 2326 data is not right!")

    if df_data2298.columns.tolist() !=  df_data2331.columns.tolist():
        raise ValueError("Either 2298 or 2331 data is not right!")

    #  Concatinate all data into single data frame
    df_data = pd.concat([df_data2298,
                         df_data2320,
                         df_data2326,
                         df_data2331],
                        ignore_index=True,axis=0)

    return df_data
