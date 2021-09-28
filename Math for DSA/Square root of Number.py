import math

# Find squar root of perfect numbers
# O(n)
def sqrt_p(n):
    for i in range(n):
        if i*i == n:
            return i 


# Find squar root of perfect numbers
# O(logN)
def modified_sqrt(n):
    si = 1
    ei = n 
    while si <= ei:
        mi = (si+ei) // 2
        if mi*mi == n:
            return mi
        elif mi*mi < n:
            si = mi + 1
        else:
            ei = mi-1


# Find squar root of in-perfect numbers
# O(logN)
def sqrt(n,p=15):
    si = 1
    ei = n 
    while si <= ei:
        mi = (si+ei) // 2
        if mi*mi == n:
            return mi
        elif mi*mi < n:
            si = mi + 1
        else:
            ei = mi-1

    root = ei 
    incr = 0.1
    for i in range(p):
        while root * root < n:
            root += incr
        root -= incr
        incr /= 10

    return root


print(sqrt(25.09),math.sqrt(25.09))
