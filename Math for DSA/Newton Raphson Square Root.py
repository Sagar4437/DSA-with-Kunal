import math

def newton_raphson_Sqrt(n):
    x = n
    root = 0
    while True:
        root = 0.5*(x+(n/x))
        if abs(root-x)<0.0001:
            break

        x = root

    return root

print(newton_raphson_Sqrt(40),math.sqrt(40))
