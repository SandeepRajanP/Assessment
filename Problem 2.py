f = open("input.txt","r")
str = f.read()
l = str.split()
dict = {}
for word in l:
	word =''.join(e for e in word if e.isalnum())
    if word in dict:
        dict[word] = dict[word] + 1
    else:
		dict[word] = 1
a = []		
a.append(dict.iterkeys for k in sorted(dict, key = lambda a:a[word]==1))
f = open ("output.txt","w")
f.write(a)
    