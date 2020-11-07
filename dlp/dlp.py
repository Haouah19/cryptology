from prime import is_probable_prime
from math import *
import random


#Exercice 1
#Q1
def bezout(a, b):
    if a==0 and b==0: return (0,0,0)
    if b==0 : return(a//abs(a), 0, abs(a))
    (u,v,p)=bezout(b,a%b) 
    return (v, (u-v*(a//b)), p)

#Q2
def inv_mod(a, n):
    for i in range(1,n):
        if(((i*a)%n)==1):
            return i
    return n


def invertibles(N):
    invertibles = []
    for i in range(N):
        if(inv_mod(i,N)!= N):
            invertibles.append(i)
    return invertibles


#Q3
#
def phi(N):
    cpt =0
    for i in range(N):
        (_,_,a) = bezout(i,N)
        if(a==1):
            cpt=cpt+1
    return cpt


#Exercice 2
#Q1
def exp(a, n, p):
    x=1
    for  i in range (p):
        x=x*x%n
    return x


#Q2
def factor(n):
    div=2
    facto=list()
    while(n!=1):
        i=0
        while(n%div==0):
            n=n//div
            i+=1
        if(i!=0):
            facto.append((div,i))
        div+=1        
    return facto


#Q3
def order(a, p, factors_p_minus1):
    liste_div = [i for (i,j) in factors_p_minus1]
    liste_div.append(p-1)
    liste_div.sort()
    for e in liste_div:
        if exp(a,e,p) == 1:
            return e
    return -1


#Q4
def find_generator(p, factors_p_minus1):
    liste = []
    for a in range(1,p):
        if order(a,p,factors_p_minus1) == p-1:
            liste.append(a)
    return liste


#Q5
def generate_safe_prime(k):
    return random_probable_prime(k)


#Q6
def bsgs(n, g, p):
    s=ceil(sqrt(n))
    x=1
    BS=list()
    BS.append(x)
    for i in range(s-1):
        x=(x*g)%n
        BS.append(x)
    
    x=(x*g)%n
    G=inv_mod(x, n)
    x=p
    GS=list()
    GS.append(p)
    for i in range(s-1):
        x=x*G%n
        GS.append(x)
    
    for i in range(len(GS)):
        for j in range(len(BS)):
            if(GS[i]==BS[j]):
                return s*i+j
    return 0


#Q8
def next(x, a, b, n, h, p):
    if x%3 == 0:
        a_1 = (a+1)%p
        b_1 = b%p
        x_1 = h*x
    elif x%3 == 1:
        a_1 = a%p
        b_1 = (b+1)%p
        x_1 = n*x
    else:
        a_1 = (2*a)%p
        b_1 = (2*b)%p
        x_1 = x*x
    return (x_1, a_1, b_1, n, h, p)


#Q9
def rho_pollard(n, h, q, p):
    import random
    #a = random.randint(,)
    #b = random.randint(,)
    x = (h**a)*(n**b)
    while True:
        sN = next(x, a, b, n, h, p)
        s2N = sN*sN
        x1,a1,b1,_,_,_ = sN
        x2,a2,b2,_,_,_ = s2N
        if x1 == x2:
            break
    return inv_mod(h**((a1-a2)*(b2-b1)),p)

print(bezout(3712,2984))
print(inv_mod(7,10))
print(invertibles(10))
print(phi(10))