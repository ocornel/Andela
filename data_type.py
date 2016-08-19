def data_type(argument):
    dtype = type(argument)          #gets us the data type
    if argument == None:
        output = 'no value'
    elif dtype == str:
        output = len(argument)      #the length of the argument
    elif dtype == bool:
        output = argument
    elif dtype == int:
        if argument == 100:
            output = 'equal to 100'
        elif argument > 100:
            output = 'more than 100'
        else:
            output = 'less than 100'
    elif dtype == list:
        if len(argument) < 3:
            output = None
        else:
            output = argument[2]    #the third item on the list
    else:
            output = 'Not an option data type'

    return output
