def fizz_buzz(number):
  if number % (3 * 5) == 0: #Numbers devisible by x and y are divisible by xy
    return 'FizzBuzz'
  elif number % 3 == 0: 
    return 'Fizz'
  elif number % 5 == 0:
    return 'Buzz'
  else:
    return number

def range_fizz_buzz(limit):
    #accepts an ending number then does fizzbuzz on all the numbers giving output
    number = 0
    while number <= limit:
        print (number ," : ", fizz_buzz(number))
        number += 1
