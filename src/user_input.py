import runlog_search
def start():
    """
    Interact with users through command-line interface. Our target
    users are students and researchers. They are comfortable using
    the command-line interface. In the future, if willing to use
    GUI instead of command-line interface, all of the application
    logic would remain the same.
    """
    stop = False
    while not stop:
        print()
        print(" *** Please enter the configurations you need *** ")
        print(" *** Enter 'QUIT' to quit the tool *** ")
        print()
        response = ""
        print("> Enter: ", end='')

        try:
            response = str(input())
        except ValueError:
            print("Type in a valid configuration!")
            break

        response = response.upper()
        cfs = response.split(" ")
        if len(cfs) == 0:
            ValueError("Try Again")
            continue
        if len(cfs) == 1 and cfs[0] == "QUIT":
            print("Thank you for using the tool. Goodbye!")
            stop = True
        else:
            test_list, run_num_list = runlog_search.search_configuration(cfs)
            print(test_list, run_num_list)

if __name__ == "__main__":
    start()
