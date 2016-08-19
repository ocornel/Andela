def string_length(strings):     #accepts string(s) as input
    lengths = []                  #create a new list that will hold length of each string in the provided list
    a=len(strings)
    if type(strings) == str:      #checks if input is a string
        lengths.append(a)
    else:
        strings=list(strings)   #otherwise, transforms to list
        for i in range(a):
            lengths.append(len(strings[i])) #add into the second list, length of string in first list
    return lengths
