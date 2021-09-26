
# find magic number
'''
Magic no is calculated as follow
	1) Take binary of ith index
	2) Take sum of power of 5 of respective index
'''


i = 6
bi = bin(i).split('0b')[1][::-1]
s = 0
for i,val in enumerate(bi):
	s += (5**(i+1))*int(val)
print(s)

