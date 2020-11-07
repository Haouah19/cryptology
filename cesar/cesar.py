import sys



def chiffrer_cesar(message_clair, clef):
    m=ord('Z')-ord('A')+1
    decale=(ord(clef)-ord('A'))%m
    message_chiffre=""
    for c in message_clair:
        message_chiffre+=chr(((ord(c)-ord('A')+decale)%m)+ord('A'))
    return message_chiffre

def dechiffrer_cesar(message_clair, clef):
    m=ord('Z')-ord('A')+1
    decale=(ord(clef)-ord('A'))%m
    message=""
    for c in message_clair:
        message+=chr(((ord(c)-ord('A')-decale)%m)+ord('A'))
    message_chiffre = message
    return message_chiffre

# NE PAS MODIFIER APRES CETTE LIGNE

def usage():
    print ("Usage : python cesar.py clef c/d phrase",file=sys.stderr)
    print ("Exemple 1 : python cesar.py E c ALICE",file=sys.stderr)
    print ("\t > EPMGI",file=sys.stderr)
    print ("Exemple 2 : python cesar.py E d EPMGI",file=sys.stderr)
    print ("\t > ALICE",file=sys.stderr)
    sys.exit(1)

if len(sys.argv) != 4:
    usage()
    
clef = sys.argv[1]
operation = sys.argv[2]
phrase = sys.argv[3]

if operation == 'c' : 
    phrase2 = chiffrer_cesar(phrase, clef)
elif operation == 'd' :
    phrase2 = dechiffrer_cesar(phrase, clef)
else:
    usage()
print(phrase2)


