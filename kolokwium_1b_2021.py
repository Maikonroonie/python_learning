import math
def len_a(a):
    return int(math.log10(a)+1)

def rotacja(a,b):
    l=len_a(a)
    T=[0 for i in range(l)]
    for i in range(l) :
        a=a%(10**(l-1))*10+(a//10**(l-1))
        T[i]=a
    return T[b]
#print(rotacja(1428,0))
def zamiana_na_sys(a,i):
    tab=[17 for i in range(a)]
    x=0
    cp_a=a
    while a!=0:
        tab[x]=a%i
        a//=i
        x+=1
   # tab=[tab[i] for i in range(len_a(cp_a)-1,-1,-1)]
    tab=[tab[x] for x in range(cp_a) if tab[x]!=17]
    tab.reverse()
    return tab
#print(zamiana_na_sys(16,3))
def czy_iloczynowo_pierwsza(T):
    l=len(T)
    iloczyn=1
    for i in range(l):
        iloczyn*=T[i]
    if iloczyn==0:
        return False
    if iloczyn<2:
        return False
    if iloczyn==2 or iloczyn==3:
        return True
    if iloczyn%2==0:
        return False
    for i in range(3,math.isqrt(iloczyn)+1,2):
        if iloczyn%i==0:
            return False
    return True
#print(czy_iloczynowo_pierwsza(zamiana_na_sys(16,3)))
def zad(a):
    for i in range(2,17):
        for j in range(len_a(a)):
            a=rotacja(a,j)
            if (czy_iloczynowo_pierwsza(zamiana_na_sys(a,i))):
                return i
    return None
print(zad(16))



