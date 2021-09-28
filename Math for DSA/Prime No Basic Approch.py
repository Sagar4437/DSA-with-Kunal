# Q- Find isPrime between 0 to N

# Complexity is O(n*sqrt(n))
def isPrime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1

    return True

n=40
for i in range(2,n+1):
    ans = isPrime(i)
    if ans:
        print(i)
