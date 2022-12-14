# This is the module/function documentation 
The modules and fucntions are in `src` directory.

      ── src
          ├── data_plot.py
          ├── data_prep.py
          ├── data_process.py
          ├── runlog_search.py
          └── user_input.py
      
## function: search_configuration

Get the run numbers and test ids corresponding to the specific configuration
Only the runs whose configuration is a superset of the input configuration
:param input: User input, the configuration they interested in, a list
:return: the run numbers we need, a list

## function runlog_search


## function: runlog_cleanup
This function clean up run logs from year to year. Make all the columns consistent. 
User should avoid to modified this. 

    runlog_cleanup(df_log2298, df_log2320, df_log2326, df_log2331):
      parameters: 
        arg df_logxxxx: Data log with entry numbers (.xlsx file)
      return: 
        var df_log    : Concatinated data log from inputs in data frame format


## fucntion: data_cleanup
This function concatinate data sets from year to year. 
It checks all data sets have cosnstent entries and concatinate them at the end. 
User should avoid to modified this. 


    data_cleanup(df_data2298, df_data2320, df_data2326, df_data2331):
      parameters: df_data
        arg df_data: Data set with entry numbers (.xlsx file)
      return: df_set
        var df_set : Concatinated data sets from inputs in data frame format



## function: data_extract:
The data extract function allows user to input test entires and run number from search and look up and extract corresponding sub data set in data frame. 


    data_extract(df_log, df_data, test, run_num):
      parameters: df_log, df_data, test, run_num
        arg df_log:      Data log from data_prep output (data frame)
        arg df_data:     Data set from data_prep output (data frame)
        arg test:        Test entries (list)
        arg run_num:     Run numbers correspondign to test entires (list)
      return: df_log_sub, df_data_sub
        var df_log_sub:  Extracted data log from test and run numbers (data frame)
        var df_data_sub: Extracted data set from test and run numbers (data frame)

    
## function: data_interp_der:
The data process clean up the data for alignment, trucntion and intperolation. This function allows two different set of data with different length and with respect to different location to be manipulated for data process, i.e., subtraction, addition, derivatives, etc. The derivative function computes the data derivaties with respect to longitudinal or lateral direction.


    data_interp_der(df_log, df_data, test, run_num):
      parameters: df_log, df_data, test, run_num
        arg df_log:  Data log from data_extract output (data frame)
        arg df_data: Data set from data_extract output (data frame)
        arg test:    Test entries (list)
        arg run_num: Run numbers correspondign to test entires (list)
      return: df_data_interp, df_data_derivative
        var df_data_interp:      Interpoalted data sets extracted data sets (data frame)
        var df_data_derivative:  Data derivatives from extracted data sets (data frame)

    
## function: data_plt
The visulization allows user to visual the data and compare different set of data.


    data_plt(plot_vars, df_log, df_data, test, run_num):
      parameters:
          arg plot_type: Plot type specificaiton (to be complete)
          arg plot_vars: Plot variables from data set variables
          arg df_log:    Data log from data_prep output (data frame)
          arg df_data:   Data set from data_prep output (data frame)
          arg test:      Test entries (list)
          arg run_num:   Run numbers correspondign to test entires (list)
      return:
          plots
