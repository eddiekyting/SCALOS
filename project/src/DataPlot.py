class DataPlot:
    
    def plt_data(plotvars, df_log_sub, df_data_sub, test, runnum):
        if pd.unique(df_log_sub[df_log.columns.tolist()[4]]) == 'P6':
            alphabeta = df_data_sub.columns.tolist()[3]
            x_label = "\\alpha"
        elif pd.unique(df_log_sub[df_log.columns.tolist()[4]]) == 'Y6':
            alphabeta = df_data_sub.columns.tolist()[4]
            x_label = "\\beta"
        else:
            raise ValueError("Run type error!")

        for j in range(len(plotvars)):
            plt.figure()
            for i in range(len(test)):
                plt.scatter(df_data_sub[alphabeta][(df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                                                   (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i])],
                                                    df_data_sub[plotvars[j]]
                                                    [(df_data_sub[df_data_sub.columns.tolist()[1]] == test[i]) & 
                                                     (df_data_sub[df_data_sub.columns.tolist()[0]] == runnum[i])], 
                                                     label='UW'+str(test[i])+' Run'+str(runnum[i]))
            plt.xlabel(r"$"+x_label+" (^\circ)$")
            if plotvars[j] == "LOD":
                y_label = "C_L/C_D"
            else:
                y_label = plotvars[j][0]+"_"+plotvars[j][1]+"("+plotvars[j][2:]+") "
            plt.ylabel(r"$"+y_label+ "$")
            if j == 0:
                plt.legend()
            plt.title(r"$"+y_label + " vs. "+ x_label+"$")
            plt.grid(True)
            plt.show()