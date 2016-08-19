"""
This function accepts a string and gives such a pattern as demonstrated:
phone  => pphphophonphone
ab     => aab
like   => lliliklike
"""
class StringSplosion(object):
    def __init__(self, string):
        self.string = str(string)

def manipulate(string):
    #string = str(string)
    terms = []          #this is the list that will contain terms for the resulting pattern
    steps = 1           #steps with which characters will be dded to pattern
    end = len(string) + 1 
    left_chars = len(string) #characters left out in term generation
    for steps in range(steps,end):
        term = string[0:end - left_chars] #the term to be added to the list of terms
        terms.append(term)  #add the term to list of terms
        left_chars -= 1
    pattern = ''.join(terms)    #join the terms that make the patter
    return pattern


print(manipulate('cow'))