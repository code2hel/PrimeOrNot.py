def is_prime(x):
    if  x <= 1:
        return False
    n = 2
    while n <= x/2:
        if x % n == 0:
            return False
        n += 1
    else:
        return True
        
print is_prime(2200112012)
