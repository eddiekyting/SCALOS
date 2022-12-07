import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

class DataPlot:
    
    def __init__(self, plot_type, plot_vars, df_log_sub, df_data_sub, test, runnum):
        """
        function:
            initialization of variables

        parameters:
            arg df_log:  Data log from data_prep output (data frame)

            arg df_data: Data set from data_prep output (data frame)

            arg test:    Test entries (list)

            arg run_num: Run numbers correspondign to test entires (list)

        return:
            self
        """
        self.plot_type = plot_type
        self.plot_var = plot_var
        self.df_log = df_log
        self.df_data = df_data
        self.test = test
        self.run_num = run_num
    
    def plt_data(plot_type, plot_vars, df_log_sub, df_data_sub, test, runnum):
        if pd.unique(df_log_sub[df_log.columns.tolist()[4]]) == 'P6':
            alphabeta = df_data_sub.columns.tolist()[3]
            x_label = "\\alpha"
        elif pd.unique(df_log_sub[df_log.columns.tolist()[4]]) == 'Y6':
            alphabeta = df_data_sub.columns.tolist()[4]
            x_label = "\\beta"
        else:
            raise ValueError("Run type error!")

        for j in range(len(plot_vars)):
            plt.figure()
            for i in range(len(test)):
                for k in range(len(runnum[i])):
                    plt.scatter(
                        df_data_sub[alphabeta][
                            (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                            (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][k])],
                        df_data_sub[plot_vars[j]][
                            (df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                            (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i][k])], 
                        label='UW'+str(test[i])+' Run'+str(runnum[i][k]))
            plt.xlabel(r"$"+x_label+" (^\circ)$")
            if plot_vars[j] == "LOD":
                y_label = "C_L/C_D"
            else:
                y_label = plot_vars[j][0]+"_"+plot_vars[j][1]+"("+plot_vars[j][2:]+") "
            plt.ylabel(r"$"+y_label+ "$")
            if j == 0:
                plt.legend()
            plt.title(r"$"+y_label + " vs. "+ x_label+"$")
            plt.grid(True)
            plt.show()
