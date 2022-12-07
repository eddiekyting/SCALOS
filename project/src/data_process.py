import numpy as np
import pandas as pd
import scipy as sp

class DataProcess:

    def data_extract(df_log, df_data, test, runnum):
        # Unit test
        if type(test) != type(runnum):
            raise ValueError("Test entries and run numbers must be consistent!")

        df_data_sub = pd.DataFrame()
        df_log_sub = pd.DataFrame()
        # Unit test
        for i in range(len(test)):
            # Test Entries must be integer
            if not isinstance(test[i], int):
                raise ValueError("Test entries must be integer!")

            # Entries must be not empty
            if not np.any(test[i]) or not np.any(runnum[i]):
                raise ValueError("Test entries and run numbers must be not empty!")

            # Test entries must be valid
            if not any(np.unique(df_log[df_log.columns.tolist()[1]]) == test[i]):
                raise ValueError("Test entries are invalid!")

            # Run number must be a list
            if not isinstance(runnum[i], list):
                raise ValueError("Run numbers are invalid!")


            for j in range(len(runnum[i])):
                # Each run number must be valid
                if runnum[i][j] < 0 or runnum[i][j] > np.max(df_log[df_log.columns.tolist()[0]][df_log[df_log.columns.tolist()[1]] == test[i]]):
                    raise ValueError("Run numbers are invalid!")

                # Entries must be not weight tare
                if np.any( pd.isna( df_log[df_log.columns.tolist()[2]][
                    (df_log[df_log.columns.tolist()[1]] == test[i]) & 
                    (df_log[df_log.columns.tolist()[0]] == runnum[i][j])
                ])):
                    raise ValueError("Test num and corresponding run num is weight tare")

                # 
                df_log_sub = pd.concat(
                    [df_log_sub, 
                     df_log[
                        (df_log[df_log.columns.tolist()[1]] == test[i]) & 
                        (df_log[df_log.columns.tolist()[0]] == runnum[i][j]
                        )]], ignore_index=True, axis=0)
                
                df_data_sub = pd.concat(
                    [df_data_sub, 
                     df_data[(df_data[df_data.columns.tolist()[1]] == test[i]) & 
                             (df_data[df_data.columns.tolist()[0]] == runnum[i][j])]
                    ],ignore_index=True, axis=0)

        # Run type must be consistant
        if len(pd.unique(df_log_sub[df_log.columns.tolist()[4]])) > 1:
            raise ValueError("Run type is inconsistant!")
        df_log_sub["RUN NO."] = df_log_sub["RUN NO."].astype(int)

        df_data_sub[["RUN","TEST"]] = df_data_sub[["RUN","TEST"]].astype(int)
        
        return df_log_sub, df_data_sub

    def data_interp_derivative(df_log_sub, df_data_sub, test, runnum):
        
        if pd.unique(df_log_sub[df_log.columns.tolist()[4]]) == 'P6':
            alphabeta = df_data_sub.columns.tolist()[3]
        elif pd.unique(df_log_sub[df_log.columns.tolist()[4]]) == 'Y6':
            alphabeta = df_data_sub.columns.tolist()[4]
        else:
            raise ValueError("Run type error!")

        max_list =[]
        min_list =[]

        for i in range(len(test)):
            for j in range(len(runnum[i])):
                max_list.append(np.max(
                    df_data_sub[alphabeta][
                        (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                        (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][j])
                    ]))
                min_list.append(
                    np.min(df_data_sub[alphabeta][
                        (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                        (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][j])
                    ]))

        alphabeta_interp= np.arange(np.ceil(np.max(min_list)), np.floor(np.min(max_list))+1, 1)

        if np.min(alphabeta_interp) != np.ceil(np.max(min_list)) or np.max(alphabeta_interp) != np.floor(np.min(max_list)):
            raise ValueError("Data range incorrect")

        df_data_sub_interp = pd.DataFrame()
        df_data_sub_derivative = pd.DataFrame()
        
        for i in range(len(test)):
            temp_interp = pd.DataFrame()
            temp_derivative = pd.DataFrame()
            for k in range(len(runnum[i])):
                for j in range(len(df_data_sub.columns.tolist())):
                    if j <= 8:
                        if df_data_sub.columns.tolist()[j] == alphabeta: 
                            temp_interp[df_data_sub.columns.tolist()[j]] = alphabeta_interp
                            temp_derivative[df_data_sub.columns.tolist()[j]] = alphabeta_interp
                        else:
                            temp_fun = sp.interpolate.interp1d(
                                df_data_sub[alphabeta][
                                    (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                                    (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][k])],
                                df_data_sub[df_data_sub.columns.tolist()[j]][
                                    (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                                    (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][k])],
                                kind = 'nearest')
                            temp_interp[df_data_sub.columns.tolist()[j]] = temp_fun(alphabeta_interp)
                            temp_derivative[df_data_sub.columns.tolist()[j]] = temp_fun(alphabeta_interp)
                    else:
                        temp_fun = sp.interpolate.interp1d(
                            df_data_sub[alphabeta][
                                (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                                (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][k])],
                            df_data_sub[df_data_sub.columns.tolist()[j]][
                                (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                                (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][k])],
                            kind = 'linear')
                        temp_interp[df_data_sub.columns.tolist()[j]] = temp_fun(alphabeta_interp)
                        temp_derivative[df_data_sub.columns.tolist()[j]] = np.gradient(temp_fun(alphabeta_interp), alphabeta_interp)


                df_data_sub_interp = pd.concat([df_data_sub_interp, temp_interp], ignore_index = True, axis = 0) 
                df_data_sub_derivative = pd.concat([df_data_sub_derivative, temp_derivative], ignore_index = True, axis = 0) 
                
        return df_data_sub_interp, df_data_sub_derivative 
    