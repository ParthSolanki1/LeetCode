import math

def powerfulIntegers(x: int, y: int, bound: int):
    results = []
    upperx = 0
    uppery = 0
    if(x > 1):
        upperx = int(math.log(bound, x))
    if(y > 1):
        uppery = int(math.log(bound, y))
    for i in range(upperx+1):
        for j in range(uppery+1):
            check = x**i + y**j
            if(check <= bound and check not in results):
                results.append(x**i + y**j)
    results.sort()
    return results

print(powerfulIntegers(2, 1, 10))