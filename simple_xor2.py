#key = input("enter key here:  ")
with open('key.txt','r') as ff:
	key = ff.read()
bit_key = []
for k in key:
	bit_key.append(ord(k)%2)
with open('cipher_in_here.txt','r') as f:
	data = f.read()
bit_data = []
for d in data:
	bit_data.append(ord(d)%2)
bit_result = []
for i in range(0,len(bit_data)):
	bit_result.append((bit_key[i%(len(bit_key)-1)]+bit_data[i])%2)
	
print(f"bit_data:{bit_data}\nbit_key:{bit_key}\nbit_result:{bit_result}")
bit_result = [str(x) for x in bit_result]
final_res = ''.join(bit_result)
print(f"copyable string: {final_res}")
