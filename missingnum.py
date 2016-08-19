def find_missing(a1,a2):        #accepts two arrays
    a1,a2 = set(a1) , set(a2)   #convert arrays to sets to allow operations
    if len(a1) == len(a2):        #checking lengths
        return 0
    else:      #When lengths aren't same, means something unique is in one of the sets
        if len(a1) > len(a2):     #The unique thing could be in first array
            miss = list(a1 - a2)    #code returns a list, thus the conversion
            return miss[0]
        else:                   #or could have been in the second array
            miss = list(a2 - a1)    
            return miss[0]
