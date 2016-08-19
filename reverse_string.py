def reverse_string(string):
    reverse = []           #this empty list will hold the reverse of the string
    i = len(string)
    while i > 0:
        reverse.append(string[i - 1]) #Adds the last letter in string to the recent position of reverse
        i -= 1              #shifts the pointer
    if string == '':
        return None
    elif ''.join(reverse) == ''.join(string): #convert both to a word and compare
        return True
    else:
        return ''.join(reverse)
        
