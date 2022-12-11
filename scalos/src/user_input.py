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
    examples, and quit.
    """
    stop = False
    while not stop:
        print()
        print(" *** Please enter the configurations you need *** ")

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
        if len(cfs) == 0:
            print("Please enter a valid configuration! Try Again!")
            continue
        test_list, run_num_list = runlog_search.search_configuration(cfs)
        if test_list == [] and stop is False:
            print("Sorry, there is no relevant data! Try other configurations!")
            continue
        if stop is False:
            print(test_list, run_num_list)

#if __name__ == "__main__":
start()
