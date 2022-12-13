"""
DataProcess: Data extract, interpolation and derivatives

parameters:
    arg df_log:  Data log from data_prep output (data frame)

    arg df_data: Data set from data_prep output (data frame)

    arg test:    Test entries (list)

    arg run_num: Run numbers correspondign to test entires (list)

return:
    df_log_sub:  Cleaned up test data sets( data frame)

    df_data_sub: Concatinated data logs (data frame)

"""
import numpy as np
import pandas as pd
import scipy as sp

# class DataProcess:

"""
function: data_extract

    Extract data from input test entries with corresponding run numbers

function: data_interp_derivatives

    Truncate data within max min and min max range (no exterpolation)
    Linear interpolate data on with integer pitch (P) or yaw (Y) run
    Compute derivaties with respect to alpha or beta
"""
#     def __init__(self, df_log, df_data, test, run_num):
#         """
#         function:
#             initialization of variables

#         parameters:
#             arg df_log:  Data log from data_prep output (data frame)

#             arg df_data: Data set from data_prep output (data frame)

#             arg test:    Test entries (list)

#             arg run_num: Run numbers correspondign to test entires (list)

#         return:
#             self
#         """

#         self.df_log = df_log
#         self.df_data = df_data
#         self.test = test
#         self.run_num = run_num

def data_extract(df_log, df_data, test, run_num):
    """
    function:
        Data extraction

    parameters:
        arg df_log:  Data log from data_prep output (data frame)

        arg df_data: Data set from data_prep output (data frame)

        arg test:    Test entries (list)

        arg run_num: Run numbers correspondign to test entires (list)

    return:
        df_log_sub:  Extracted data log from test and run numbers (data frame)

        df_data_sub: Extracted data set from test and run numbers (data frame)
    """

#     df_log = self.df_log
#     df_data = self.df_data
#     test = self.test
#     run_num = self.run_num
    # Unit test
    if len(test) != len(run_num):
        raise ValueError("Test entries and run numbers must be consistent!")

    df_data_sub = pd.DataFrame()
    df_log_sub = pd.DataFrame()
    # Unit test
    for i in range(len(test)):
        # Test Entries must be integer
        if not isinstance(test[i], int):
            raise ValueError("Test entries must be integer!")

        # Entries must be not empty
        if not np.any(test[i]) or not np.any(run_num[i]):
            raise ValueError("Test entries and run numbers must be not empty!")

        # Test entries must be valid
        if not any(np.unique(df_log[df_log.columns.tolist()[1]]) == test[i]):
            raise ValueError("Test entries are invalid!")

        # Run number must be a list
        if not isinstance(run_num[i], list):
            raise ValueError("Run numbers are invalid!")

        for j in range(len(run_num[i])):
            # Each run number must be valid
            if run_num[i][j] < 0 or run_num[i][j] > np.max(
                df_log[df_log.columns.tolist()[0]][
                    df_log[df_log.columns.tolist()[1]] == test[i]]):
                raise ValueError("Run numbers are invalid!")

            # Entries must be not weight tare
            if np.any( pd.isna( df_log[df_log.columns.tolist()[2]][
                (df_log[df_log.columns.tolist()[1]] == test[i]) &
                (df_log[df_log.columns.tolist()[0]] == run_num[i][j])
            ])):
                raise ValueError("Test num and corresponding run num is weight tare")

            # Concatinate sub data log
            df_log_sub = pd.concat(
                [df_log_sub,
                 df_log[
                    (df_log[df_log.columns.tolist()[1]] == test[i]) &
                    (df_log[df_log.columns.tolist()[0]] == run_num[i][j]
                    )]], ignore_index=True, axis=0)
            # Concatinate sub data set
            df_data_sub = pd.concat(
                [df_data_sub,
                 df_data[(df_data[df_data.columns.tolist()[1]] == test[i]) &
                         (df_data[df_data.columns.tolist()[0]] == run_num[i][j])]
                ],ignore_index=True, axis=0)

    # Run type must be consistant
    if len(pd.unique(df_log_sub[df_log.columns.tolist()[4]])) > 1:
        raise ValueError("Run type is inconsistant!")
    df_log_sub["RUN NO."] = df_log_sub["RUN NO."].astype(int)

    df_data_sub[["RUN","TEST"]] = df_data_sub[["RUN","TEST"]].astype(int)

    return df_log_sub, df_data_sub

def data_interp_derivative(df_log, df_data, test, run_num):
    """
    function:
        Data inpterolation and derivatives

    parameters:
        arg df_log:  Data log from data_extract output (data frame)

        arg df_data: Data set from data_extract output (data frame)

        arg test:    Test entries (list)

        arg run_num: Run numbers correspondign to test entires (list)

    return:
        df_data_interp:      Interpoalted data sets extracted data sets (data frame)

        df_data_derivative:  Data derivatives from extracted data sets (data frame)
    """

#     df_log = self.df_log
#     df_data = self.df_data
#     test = self.test
#     run_num = self.run_num

    # Check run type
    if pd.unique(df_log[df_log.columns.tolist()[4]]) == 'P6':
        alphabeta = df_data.columns.tolist()[3]
    elif pd.unique(df_log[df_log.columns.tolist()[4]]) == 'Y6':
        alphabeta = df_data.columns.tolist()[4]
    else:
        raise ValueError("Run type error!")

    max_list =[]
    min_list =[]

    # find the max and min among all runs
    for i in range(len(test)):
        for j in range(len(run_num[i])):
            max_list.append(np.max(
                df_data[alphabeta][
                    (df_data[df_data.columns.tolist()[1]] == test[i]) &
                    (df_data[df_data.columns.tolist()[0]] == run_num[i][j])
                ]))
            min_list.append(
                np.min(df_data[alphabeta][
                    (df_data[df_data.columns.tolist()[1]] == test[i]) &
                    (df_data[df_data.columns.tolist()[0]] == run_num[i][j])
                ]))
    # interpolate alpha or beta from min to max
    alphabeta_interp= np.arange(np.ceil(np.max(min_list)), np.floor(np.min(max_list))+1, 1)

    # Check interp data not extrapolate
    if np.min(alphabeta_interp) != np.ceil(np.max(min_list)) or np.max(
        alphabeta_interp) != np.floor(np.min(max_list)):
        raise ValueError("Data range incorrect")

    df_data_interp = pd.DataFrame()
    df_data_derivative = pd.DataFrame()

    # Loop through tests and run numbers
    for i in range(len(test)):
        temp_interp = pd.DataFrame()
        temp_derivative = pd.DataFrame()
        for k in range(len(run_num[i])):
            for j in range(len(df_data.columns.tolist())):
                # Variables do not need to be interpreted
                if j <= 8:
                    if df_data.columns.tolist()[j] == alphabeta:
                        temp_interp[df_data.columns.tolist()[j]] = alphabeta_interp
                        temp_derivative[df_data.columns.tolist()[j]] = alphabeta_interp
                    else:
                        temp_fun = sp.interpolate.interp1d(
                            df_data[alphabeta][(
                                df_data[df_data.columns.tolist()[1]] == test[i]
                            ) & (
                                df_data[df_data.columns.tolist()[0]] == run_num[i][k]
                            )],
                            df_data[df_data.columns.tolist()[j]][
                                (df_data[df_data.columns.tolist()[1]] == test[i]) &
                                (df_data[df_data.columns.tolist()[0]] == run_num[i][k]
                                )], kind = 'nearest')
                        temp_interp[df_data.columns.tolist()[j]] = temp_fun(
                            alphabeta_interp)
                        temp_derivative[df_data.columns.tolist()[j]] = temp_fun(
                            alphabeta_interp)
                else:
                    temp_fun = sp.interpolate.interp1d(
                        df_data[alphabeta][(
                            df_data[df_data.columns.tolist()[1]] == test[i]
                        ) & (
                            df_data[df_data.columns.tolist()[0]] == run_num[i][k]
                        )], df_data[df_data.columns.tolist()[j]][(
                            df_data[df_data.columns.tolist()[1]] == test[i]
                        ) & (
                            df_data[df_data.columns.tolist()[0]] == run_num[i][k]
                        )], kind = 'linear')
                    temp_interp[df_data.columns.tolist()[j]] = temp_fun(
                        alphabeta_interp)
                    temp_derivative[df_data.columns.tolist()[j]] = np.gradient(
                        temp_fun(alphabeta_interp), alphabeta_interp)

            # Concatinate data interpolation
            df_data_interp = pd.concat(
                [df_data_interp, temp_interp]
                , ignore_index = True, axis = 0)

            # Concatinate data derivatives
            df_data_derivative = pd.concat(
                [df_data_derivative, temp_derivative]
                , ignore_index = True, axis = 0)

    return df_data_interp, df_data_derivative
