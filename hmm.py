import random
import sys
import os
import subprocess
from subprocess import check_call
from subprocess import call
import pyfiglet
import pyperclip

  

name=sys.argv[1]
fil=input("Enter unlocker: ")

def copy(txt):
    cmd = 'echo | set /p nul=' + txt.strip() + '| clip'
    check_call(cmd,shell=True)


def get_seed(filename):
    try:
        f = open(fil, 'rb')
        file_content = f.read()
        f.close()
        ok=0
        file_content=str(file_content)
        for i in file_content:
            if i=='0':
                ok+=1
        return ok
    except:
        return "NOO!!!"

# print(get_seed(fil))
if get_seed(fil)=='NOO!!!':
    print(get_seed(fil))
f1=open('passwords.txt','r')
d={}
sad=0
for line in f1.readlines():
    if sad==0:
        sad+=1
        continue
    l=line.split()
    d[l[0]]=0

# print(*d)
seed=get_seed(fil)
if(seed=="NOO!!!"):
    sys.exit()
s="ABCa1bDc2dEe3fFg4G5hHi6Ij7kJl8mKn9oLp0qMrNs!tO@uPv#wQx$yRz%S^T&U*V(W)X?Y>Z"
# s1="1234567890"
# s2="!@#$%^&*(),./;[]\-<>?:"
# s3="abcdefghijklmnopqrstuvxyz"
random.seed(seed)
ok=len(d)
plist=random.sample(range(1,10000), ok)
# print(plist)
finlist=[]
for i in plist:
    passw=""
    random.seed(i)
    list1=random.sample(range(0,73), 69)
    for j in list1:
        passw+=s[j]
    # random.seed(i)
    # list2=random.sample(range(0,9),5)
    # for j in list2:
    #     passw+=s1[j]
    # random.seed(i)
    # list3=random.sample(range(0,21),5)
    # for j in list3:
    #     passw+=s2[j]
    # random.seed(i)
    # list4=random.sample(range(0,25),12)
    # for j in list4:
    #     passw+=s3[j]
    finlist.append(passw)

k=0
for i in d.keys():
    d[i]=finlist[k]
    k+=1

# print(d[name])
try:
    subprocess.call('ok.bat')
    pyperclip.copy(d[name])
    result = pyfiglet.figlet_format("Success")
    print(result)

except:
    subprocess.call('man.bat')
    print(pyfiglet.figlet_format("DOES NOT EXIST!!!"))




