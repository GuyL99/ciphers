with open('cipher_in_here.txt','r') as f:
	data = f.read()

with open('key.txt', 'r') as ff:
	key = ff.read()
#key = int(input("enter key: "))
key_ = [ord(k) for k in key]
key_bin =[]
for t in  key_: 
	key_bin.append(bin(t))
key_bin = ''.join(key_bin)
data_bin = int(''.join(format(ord(x),'b') for x in data)) #bin(int(data))
new_key = ''
for x in range(0,len(data)):
	new_key+=str(key_bin)[x%(len(str(key))-1)]
print(new_key)
p = 0
dta = ''
for c in data:
	dta+=chr(ord(c)^ord(new_key[p]))
	p+=1
print(dta)
