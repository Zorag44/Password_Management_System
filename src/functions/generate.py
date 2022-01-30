import random
def generator(seed,d):
    s="ABCa1bDc2dEe3fFg4G5hHi6Ij7kJl8mKn9oLp0qMrNs!tO@uPv#wQx$yRz%S^T&U*V(W)X?Y>Z"
    random.seed(seed)
    ok=len(d)
    plist=random.sample(range(1,10000), ok)
    finlist=[]
    for i in plist:
        passw=""
        random.seed(i)
        list1=random.sample(range(0,73), 69)
        for j in list1:
            passw+=s[j]
        finlist.append(passw)
    return finlist
