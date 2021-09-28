# Seive Algorithm
# Complexity is O(N*log(logN))
# Algo to check primes between Range

def isPrime_Seive_Algo(n):

    arr = [0 for i in range(n+1)]
    # O(N)
    i=2
    while i*i <= n:
        if not arr[i]:
            # O(log(logN))
            for j in range(2*i,n,+i):
                arr[j]=1
        i+=1

    for i in range(2,n+1):
        if not arr[i]:
            print(i,end=' ')

isPrime_Seive_Algo(37)

