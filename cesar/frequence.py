import sys
def frequence(path):
    fichier= open(path,"r")
    l=[0 for i in range(ord('A'),ord('Z')+1)]
    print (l)
    freq=0
    for a in fichier:
       for c in a:
           if ord(c)<ord('Z') and ord(c)>(ord('A')-1):
                l[ord(c)-ord('A')]=l[ord(c)-ord('A')]+1
                freq=freq+1
    for i in range(0,ord('Z')-ord('A')+1):
        l[i]/=freq
    fichier.close()
    return l


frequence('Germinal.txt')