def is_prime(n):
	is_prime = True
	if (n == 0) or (n == 1):
			is_prime = False
	else:
		for i in range(2, n):
			if (n % i) == 0:
				is_prime = False
	return(is_prime)

n=130
i = 2
k = 0
sum = 0
while((sum+i) <= n):
	if(is_prime(i)):
		sum += i
		k += 1
	i+=1

print(k)

