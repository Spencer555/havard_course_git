import math

def is_prime(n):
    if n < 2:
        return False 
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % 1 == 0:
                return False
        return True
    
    
print(is_prime(10))
print(is_prime(5))