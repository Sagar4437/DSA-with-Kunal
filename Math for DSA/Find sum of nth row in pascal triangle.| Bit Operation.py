
'''
Find sum of nth row in pascal triangle.


Pascal Traiangle:
1
1 1
1 2 1
1 3 3  1
1 4 6  4  1
1 5 10 10 5 1

here Sum == 2 raised to (n-1)

Use Bit operation to find sum

'''

n = 4
ans = 1<<(n-1) # Bit manupulation
ans1 = 2**(n-1) # Using Formula
print(ans,ans1,ans==ans1)
