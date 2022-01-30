import random
import sys
import os
import subprocess
from subprocess import check_call
from subprocess import call
import pyfiglet
import pyperclip
from get_seed import get_seed
from generate import generator

name=sys.argv[1]
fil=input("Enter unlocker: ")

# def copy(txt):
#     cmd = 'echo | set /p nul=' + txt.strip() + '| clip'
#     check_call(cmd,shell=True)

f1=open('passwords.txt','r')
d={}
sad=0
for line in f1.readlines():
    if sad==0:
        sad+=1
        continue
    l=line.split()
    d[l[0]]=0


seed=get_seed(fil)
if(seed=="NOO!!!"):
    print("NOO!!!")
    sys.exit()


finlist=generator(seed,d)
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




