def a_Raised_b(base,power):
	ans = 1
	while power > 0:
		if (power & 1) == 1:
			ans *= base 

		base *= base
		power = power >> 1

	print(ans)

a_Raised_b(3,10)
