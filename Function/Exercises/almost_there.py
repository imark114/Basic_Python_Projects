# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n:int) -> bool:
    return (abs(100-n) <= 10) or (abs(200 -n) <=10)

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))