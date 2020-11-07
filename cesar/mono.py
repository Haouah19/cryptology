import sys
import string
def chiffrer_mono(message_clair, clef):
    m=ord('Z')-ord('A')+1
    message_chiffre=""
    for c in message_clair:
        message_chiffre+=clef[ord(c)-ord('A')]

    return message_chiffre
                                   
def dechiffrer_mono(message_clair, clef):
    alphabet=string.ascii_uppercase
    
    message_chiffre=""
    for c in message_clair:
        message_chiffre +=alphabet[clef.index(c)]
    return message_chiffre

# NE PAS MODIFIER APRES CETTE LIGNE

def usage():
    print ("Usage : python mono.py clef c/d phrase",file=sys.stderr)
    print ("Exemple 1 : python mono.py QWERTYUIOPASDFGHJKLZXCVBNM c ALICE",file=sys.stderr)
    print ("\t > QSOET",file=sys.stderr)
    print ("Exemple 2 : python mono.py QWERTYUIOPASDFGHJKLZXCVBNM d QSOET",file=sys.stderr)
    print ("\t > ALICE",file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 4:
    usage()
    
clef = sys.argv[1]
operation = sys.argv[2]
phrase = sys.argv[3]

if operation == 'c' : 
    phrase2 = chiffrer_mono(phrase, clef)
elif operation == 'd' :
    phrase2 = dechiffrer_mono(phrase, clef)
else:
    usage()
print(phrase2)
