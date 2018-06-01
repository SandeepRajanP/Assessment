n = int(raw_input())
while n!=1:	
	if n%2 == 0:
		print n,
		n = n/2
	else:
		print n,
		n = 3*n+1
		
