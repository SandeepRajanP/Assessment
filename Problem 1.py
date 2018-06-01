def validate(s):
	l = len(s)
	count = 0
	for i in range(l):
		if s[i].isalpha() and s[i].isupper():
			count = count + 1
			break

	for i in range(l):
		if s[i].isalpha() and s[i].islower():
			count = count + 1
			break

	for i in range(l):
		if s[i].isdigit():
			count = count + 1
			break

	for i in range(l):
		if s[i] in ["$","#","@"]:
			count = count + 1
			break

	if l>=6 and l<=12:
		count = count + 1		

	if count == 5:
		print "password is valid"
	else:
		print "password is invalid"

if __name__ == "__main__":
    password = raw_input()
    validate(password)
    		