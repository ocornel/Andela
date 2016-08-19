class PrimeChecker(object):
    def __init__(self, number=''):
        self.number = number

    def is_prime(self): 
        try:
            num = int(self.number)
            for divisor in range(2,num):
                if((num % divisor) == 0):
                    return False
                    break
                else:
                    if(divisor == num - 1):
                        return True
        except ValueError:
            return False
