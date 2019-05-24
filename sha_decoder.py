import hashlib as hl

hashes = []
with open('common_pass_to_try.txt','r') as f:
    for line in f:
        hashes.append([line.rstrip("\n"),line.rstrip("\n")])
for x in range(0,len(hashes)):
    hashes[x][1] = hl.sha256(hashes[x][0].encode('utf-8')).hexdigest()
    print(hashes[x][1])

with open('cipher_in_here.txt','r') as ff:
    #for line in ff:
     #   hashe = hl.sha256((line.rstrip("\n")).encode('utf-8')).hexdigest()
    #print(hashe)
    hashe = ff.read()
a = True
for h in hashes:
    if h[1] == hashe:
        print(f"the decodes hash is {h[0]} and it was sha-256")
        a = False

for x in range(0,len(hashes)):
    hashes[x][1] = hl.sha1(hashes[x][0].encode('utf-8')).hexdigest()
    print(hashes[x][1])

with open('cipher_in_here.txt','r') as ff:
    hashe = ff.read()
a = True
for h in hashes:
    if h[1] == hashe:
        print(f"the decodes hash is {h[0]} and it was sha-1")
        a = False

 
for x in range(0,len(hashes)):
    hashes[x][1] = hl.sha512(hashes[x][0].encode('utf-8')).hexdigest()
    print(hashes[x][1])

with open('cipher_in_here.txt','r') as ff:
    hashe = ff.read()
a = True
for h in hashes:
    if h[1] == hashe:
        print(f"the decodes hash is {h[0]} and it was sha-512")
        a = False

for x in range(0,len(hashes)):
    hashes[x][1] = hl.md5(hashes[x][0].encode('utf-8')).hexdigest()
    print(hashes[x][1])

with open('cipher_in_here.txt','r') as ff:
    hashe = ff.read()
a = True
for h in hashes:
    if h[1] == hashe:
        print(f"the decodes hash is {h[0]} and it was md-5")
        a = False


if a :
    print("could'nt locate your hash")




