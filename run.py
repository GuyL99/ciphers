import os
import platform as plt

commands_arr =[]
key1 = input("hi!, if you posses a key then enter it here, if you don't' please enter Idonthavekey\n")
if key1 == "Idonthavekey":
    if plt.system() == 'linux' :
        commands_arr = ["python3 ceaser_cipher.py >>log.txt"]
    else :
        commands_arr = ["python ceaser_cipher.py >>log.txt"]
else:
    with open('key.txt','w') as f :
        f.write(key1)
    for l in os.listdir():
        if l!='run.py' and l!='ceaser_cipher.py' and l.endswith('.py'):
            if plt.system() == 'Linux':
                commands_arr.append(f"python3 {l} >>log.txt" )
            else:
                commands_arr.append(f"python {l} >>log.txt" )
    for x in commands_arr:
        print(x)
        os.system(x)

