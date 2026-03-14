# My code
def is_square(n):
    try:
        if n >= 0.0:
            calc = pow(n,0.5)
            if n % calc != 0 or n == 0:
                return False
                return f"{n}: is not a square number"
            else:
                return True
                return f"{n} is a square number ({calc:.0f} * {calc:.0f})"
        else:
            return False
            return f"{n}: Negative numbers cannot be square numbers"
    except ZeroDivisionError:
        return True
        return f"{n} is a square number ({calc:.0f} * {calc:.0f})"
    
# Another code
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

# Another code with library
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0
    

print("gamer")
print("gamer")
print("gamer")
print("gamer")
print("gamer")