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


f1=open('passwords.txt','r')
lis=[]
sad=0
for line in f1.readlines():
    if sad==0:
        sad+=1
        continue
    l=line.split()
    if l[0]==name:
        lis.append("deleted!\n")
    else:
        lis.append(line)
f2=open('passwords.txt','w')
f2.writelines(lis)
f2.close()
print("Deleted!!")







