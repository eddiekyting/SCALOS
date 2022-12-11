"""
DataPlot: Data extract, interpolation and derivatives

parameters:
    arg plot_type: Plot type specificaiton (to be complete)

    arg plot_vars: Plot variables from data set variables

    arg df_log:    Data log from data_prep output (data frame)

    arg df_data:   Data set from data_prep output (data frame)

    arg test:      Test entries (list)

    arg run_num:   Run numbers correspondign to test entires (list)

return:
    Plots

"""
import pandas as pd
import matplotlib.pyplot as plt

class DataPlot:

    """
    function: plt_data

        Plot input data for visulization

    """
    def __init__(self, plot_vars, df_log, df_data, test, run_num):
        """
        function:
            initialization of variables

        parameters:
            arg plot_type: Plot type specificaiton (to be complete)

            arg plot_vars: Plot variables from data set variables

            arg df_log:    Data log from data_prep output (data frame)

            arg df_data:   Data set from data_prep output (data frame)

            arg test:      Test entries (list)

            arg run_num:   Run numbers correspondign to test entires (list)

        return:
            self
        """
#         self.plot_type = plot_type
        self.plot_vars = plot_vars
        self.df_log = df_log
        self.df_data = df_data
        self.test = test
        self.run_num = run_num

    def plt_data(self):
        """
        function:
            Plot data

        parameters:
            arg plot_type: Plot type specificaiton (to be complete)

            arg plot_vars: Plot variables from data set variables

            arg df_log:    Data log from data_prep output (data frame)

            arg df_data:   Data set from data_prep output (data frame)

            arg test:      Test entries (list)

            arg run_num:   Run numbers correspondign to test entires (list)

        return:
            plots
        """
#         plot_type = self.plot_type
        plot_vars = self.plot_vars
        df_log = self.df_log
        df_data = self.df_data
        test = self.test
        run_num = self.run_num

        # Run type must be consistant
        if pd.unique(df_log[df_log.columns.tolist()[4]]) == 'P6':
            alphabeta = df_data.columns.tolist()[3]
            x_label = "\\alpha"
        elif pd.unique(df_log[df_log.columns.tolist()[4]]) == 'Y6':
            alphabeta = df_data.columns.tolist()[4]
            x_label = "\\beta"
        else:
            raise ValueError("Run type error!")

        # Plot data
        for j in range(len(plot_vars)):
            plt.figure()
            for i in range(len(test)):
                for k in range(len(run_num[i])):
                    plt.scatter(
                        df_data[alphabeta][
                            (df_data[df_data.columns.tolist()[1]] == test[i]) &
                            (df_data[df_data.columns.tolist()[0]] == run_num[i][k])],
                        df_data[plot_vars[j]][
                            (df_data[df_data.columns.tolist()[1]] == test[i]) &
                            (df_data[df_data.columns.tolist()[0]] == run_num[i][k])],
                        label='UW'+str(test[i])+' Run'+str(run_num[i][k]))
            plt.xlabel(r"$"+x_label+r" (^\circ)$")
            if plot_vars[j] == "LOD":
                y_label = "C_L/C_D"
            else:
                y_label = plot_vars[j][0]+"_"+plot_vars[j][1]+"("+plot_vars[j][2:]+") "
            plt.ylabel(r"$"+y_label+ "$")
            # Obly display legend on first plot
            if j == 0:
                plt.legend()
            plt.title(r"$"+y_label + " vs. "+ x_label+"$")
            plt.grid(True)
            plt.show()
