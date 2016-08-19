def factorial (number):
    fact = 1
    if number < 0:
        return 'negative'
    elif number <= 1:
        return fact
    else:
        for n in range(number):
            fact *= n+1
        return fact

def alt_factorial (number):     #This finds factorial by recussion
    if number < 0:
        return 'negative'
    elif number <= 1:
        return 1
    else:
        return number * alt_factorial(number - 1) # the factorial of a number is the product of the number and the factorial of it's smaller number
