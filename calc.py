import sys
import logging


def calc(variableDict, varList, value, pos):
    """
    Recursive function that returns the value of varList
    Inputs: 
    variableDict: dict of all variables, varList: the list to go through,
    value: the current value of the calculation, pos: current position in list
    """
    if pos == len(varList):
        return value

    op, var = varList[pos]

    # If the other variable in the operation is not int, get variable's value
    if not var.isnumeric():
        if var not in variableDict:
            logging.error("variable " + var + " is not defined")
        var = calc(variableDict, variableDict[var], 0, 0)

    # Do arithmetic operation of choice
    if op == "add":
        return calc(variableDict, varList, value + int(var), pos + 1)

    elif op == "subtract":
        return calc(variableDict, varList, value - int(var), pos + 1)

    elif op == "multiply":
        return calc(variableDict, varList, value * int(var), pos + 1)



def getInput(filename):
    """
    Gets and makes input usable
    Divides  the commands up and makes them lower case
    Returns a list of the commands to run
    """
    commands = []

    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        temp = line.split("\n")[0].split(" ")

        for i, elem in enumerate(temp):
            temp[i] = elem.lower()
        commands.append(temp)

    return commands


def main(filename):

    commands = getInput(filename)

    variableDict = {}

    for command in commands:
        # Quit - exit calculator
        if command[0] == "quit":
            break

        # Prints and calculates output for variable
        elif command[0] == "print" and len(command) == 2:
            if command[1] in variableDict:
                print(calc(variableDict, variableDict[command[1]], 0, 0))  
            else:
                logging.error("variable " + command[1] + " is not defined")

        # If command is arithmetic operation of size 3 and variable 1 not int
        elif (len(command) == 3 and (command[1] == "add" or 
                                    command[1] == "subtract" or 
                                    command[1] == "multiply") and 
                                    not command[0].isnumeric()):

            # removes first element to add the of list to first elem's dict
            var = command.pop(0)

            # If variable does not exist, make a list for it in variableDict
            if var not in variableDict: 
                variableDict[var] = []

            # Add command to variables list in the dictionary
            variableDict[var].append(command)
        else:
            if not command == ['']:
                logging.error("Bad command: " + ' '.join(command))


if __name__ == "__main__": 
    main(sys.argv[1])  
