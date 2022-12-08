"""
This module first does some data processing(change the configurations
from strings to lists, get the unique configurations) to speed up
the following search. Then it can search among all the runlogs and
collect those with the specific configurations that the user needs.
"""
import pandas as pd

# Pre-process
df_runlog = pd.read_csv(r'~/SCALOS/project/runlogs/runlogs.csv')
config = df_runlog["CONFIGURATION"]
config_list = []
for cf in config:
    cf = cf.split("(")[0]
    config_list.append(cf)
df_runlog["CONFIGURATION_SIMPLE"] = config_list
# get the unique configurations
config_unique_str = list(set(config_list))
config_unique = [c.split("+") for c in config_unique_str]
# for each configuration, get the corresponding run numbers
run_numbers = []
for cf_u in config_unique_str:
    run_numbers.append(df_runlog.loc[df_runlog['CONFIGURATION_SIMPLE'] == cf_u][["RUN NO.","TEST"]])

def search_configuration(input):
    """
    # Get the run numbers and test ids corresponding to the specific configuration
    Only the runs whose configuration is a superset of the input configuration
    :param input: User input, the configuration they interested in, a list
    :return: the run numbers we need, a list
    """
    if input == []:
        raise ValueError("The input is null!")
    output_config = []
    run_num = []
    for cf in config_unique:
        if set(input).issubset(set(cf)):
            cf_position = config_unique.index(cf)
            output_config.append(config_unique_str[cf_position])
            run_num.append(run_numbers[cf_position])
    test_list = []
    run_num_list = []
    for run_n in run_num:
        test_list.append(run_n["TEST"].tolist()[0])
        run_num_list.append(run_n["RUN NO."].tolist())
    return test_list, run_num_list
