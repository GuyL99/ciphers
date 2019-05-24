a = 0
b = 0

with open('cipher_in_here.txt','r') as f:
	data = f.read()
#key = input("enter key:")
with open('key.txt','r') as ff:
	key = ff.read()
if len(key) == 0:
	print(data)
else:
	for i in range(0,len(data)):
		c = ord(data[i])
		if data[i] == ' ':
			print(" ",end="")
		if c <65 or c>122:
			print(data[i],end="")
		elif c>=65 and c<=90:
			c+=ord(key[(i-1)%len(key)])-90
			if c >90:
				c-=26
		elif c>=91 and c<=122:
			c+=ord(key[(i-1)%len(key)])-90
			if c >122:
				c-=26
		print(chr(c),end="")

