"""
DataPrep: Data pre-process and preperation for manipulation and process

parameters:
    arg df_logXXXX:   
    
    arg df_dataXXXX: 

return:
    arg df_log 
"""

import numpy as np

class DataPrep:
    """
    function: runlog_cleanup
        clean up run log vairables and 
        
    function: data_cleanup
    return:
        mean of closest n_neighors
    """
    # Make sure inputs are correct

    def runlog_cleanup(df_log2298, df_log2320, df_log2326, df_log2331):
        """
        parameters:
            arg n_neightbors = number of neightbors
            arg data         = 2 dimensional numpy array of shape (m, n+1)). m denotes the number of
                            samples and n is the number of variables in each sample. +1 is for the
                            labels in each sample.
            arg query        = 1 dimensional numpy array, shape (n,)

        return:
            mean of closest n_neighors
        """
        # clean up uw2298
        del df_log2298["Riley's Stress Level"]                                    # delete unncessary column 
        df_log2298.rename(columns = {'FLAP L/R':'IB FLAP L/R'}, inplace = True)   # Rename inconsistant column
        df_log2298.rename(columns = {'AIL L/R':'OB AIL L/R'}, inplace = True)     # Rename inconsistant column
        df_log2298.rename(columns = {'LE DEF':'LE IB/OB'}, inplace = True)        # Rename inconsistant column
        df_log2298.rename(columns = {'TRIP DEF':'TRIP DOTS'}, inplace = True)     # Rename inconsistant column
        df_log2298.insert(1,'TEST', 2298)                                         # add entry number 
        df_log2298['Nacelle Blockage L/R']= np.nan
        df_log2298['Spoiler L/R']= np.nan
        temp = df_log2298['DATE']
        del df_log2298['DATE']
        df_log2298['DATE']= temp
        df_log2298.columns.tolist() 
        # clean up uw2320
        df_log2320.rename(columns = {'FLAP L/R':'IB FLAP L/R'}, inplace = True)
        df_log2320.rename(columns = {'AIL L/R':'OB AIL L/R'}, inplace = True)
        df_log2320.rename(columns = {'TRIP DEF':'TRIP DOTS'}, inplace = True)
        df_log2320.insert(1,'TEST', 2320)
        df_log2320['Nacelle Blockage L/R']= np.nan
        df_log2320['Spoiler L/R']= np.nan
        temp = df_log2320['DATE']
        del df_log2320['DATE']
        df_log2320['DATE']= temp
        # clean up uw2326
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
        df_log = pd.concat([df_log2298, df_log2320, df_log2326, df_log2331], ignore_index=True,axis=0)
    #     # Exclude weight tare runs
    #     df_log[np.isnan(df_log['WT.\nTARE\nRUN']) == False]
        return df_log, df_log2298, df_log2320, df_log2326, df_log2331
    
    def data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331):
        
        if df_data2298.columns.tolist() !=  df_data2320.columns.tolist():
            raise ValueError("Either 2298 or 2320 data is not right!")

        if df_data2298.columns.tolist() !=  df_data2326.columns.tolist():
            raise ValueError("Either 2298 or 2326 data is not right!")

        if df_data2298.columns.tolist() !=  df_data2331.columns.tolist():
            raise ValueError("Either 2298 or 2331 data is not right!")

        df_data = pd.concat([df_data2298, df_data2320, df_data2326, df_data2331], ignore_index=True,axis=0)
        return df_data