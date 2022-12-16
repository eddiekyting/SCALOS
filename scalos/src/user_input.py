"""
This module contains the user-interaction command-line interface.
Our target users are students and researchers. They are comfortable
using the command-line interface. In the future, if willing to use
GUI instead of command-line interface, all of the application logic
would remain the same.
"""
import runlog_search
def start():
    """
    Interact with users through command-line interface. User can choose
    among entering the configurations, seeing some configuration
    examples, and quit.After entering the configuration, the function
    can see whether we have this configuration in our dataset. If yes,
    the function will also print the number of runs we have.
    """
    stop = False
    while not stop:
        print()
        print(" *** Please enter the configurations you need *** ")
        print(" *** Enter 'See Examples' to see some configuration examples *** ")
        print(" *** Enter 'QUIT' to  quit the tool *** ")
        print()
        response = ""
        print("> Enter: ", end='')

        try:
            response = str(input())
        except ValueError:
            print("Type in a valid configuration!")
            continue

        response = response.upper()
        if response == "QUIT":
            print("Thank you for using this SCALOS tool. Goodbye!")
            stop = True
        cfs = response.split(" ")
        while " " in cfs:
            cfs.remove(" ")
        while "" in cfs:
            cfs.remove("")
        if cfs == ["SEE","EXAMPLES"]:
            print("W15 A15 F15 V15 H15A.1 VF1 DF1")
            print("F15 A20 W20 N20.T V20 H20.T C15.F")
            print("F15 A15 W15 N20.B V15.1 DF.1 VF.1 H20.L C15.F")
            continue
        if len(cfs) == 0:
            print("Please enter a valid configuration! Try Again!")
            continue
        test_list, run_num_list = runlog_search.search_configuration(cfs)
        if test_list == [] and stop is False:
            print("Sorry, there is no relevant data! Try other configurations!")
            continue
        if stop is False:
            n_of_run = sum(len(i) for i in run_num_list)
            print("Great! There are "+str(n_of_run)+" runs with the configuration "
                                               "you entered in our dataset!")


