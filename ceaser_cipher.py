with open ('cipher_in_here.txt','r') as f:
	data = f.read()
for i in range(0,26):
	c = -1
	d = 0
	for a in data:
		if a == '#':
			print("",end="")
			d+=1
		elif a == ' ':
			print(" ",end="")
		else:
			b = ord(a)
			if b >=97 and b<=122:
				b+=i
				if b > 122:
					b-=26
			elif b>=65 and b<=90:
				b+=i
				if b>90:
					b-=26
			else:
				print("",end="")
				c+=1
			print(chr(b),end="")
	print(f"     the number of NON-LETTERS:{c}\n     the number of comments is {d}")
	
