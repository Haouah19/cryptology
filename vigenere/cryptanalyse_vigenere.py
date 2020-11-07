# Sorbonne Université 3I024 2018-2019
# TME 2 : Cryptanalyse du chiffre de Vigenere
#
# Etudiant.e 1 : HAOUILI AHMED 3774394
# Etudiant.e 2 : DEGHRI AMINE 3801757

import sys, getopt, string, math

# Alphabet français
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fréquence moyenne des lettres en français
freq_FR = [0.09213414037491088,  0.010354463742221126,  0.030178915678726964,  0.03753683726285317,  0.17174710607479665,  0.010939030914707838,  0.01061497737343803,  0.010717912027723734,  0.07507240372750529,  0.003832727374391129,  6.989390105819367e-05,  0.061368115927295096,  0.026498684088462805,  0.07030818127173859,  0.049140495636714375,  0.023697844853330825,  0.010160031617459242,  0.06609294363882899,  0.07816806814528274,  0.07374314880919855,  0.06356151362232132,  0.01645048271269667,  1.14371838095226e-05,  0.004071637436190045,  0.0023001447439151006,  0.0012263202640210343] 

# Chiffrement César
def chiffre_cesar(txt, key):
    """
    Permet de chiffrer un message Clair txt avec une clé, et retourne le message Chiffré.
    """
    m=ord('Z')-ord('A')+1
    message_chiffre=""
    for c in txt:
        message_chiffre += chr(((ord(c)-ord('A')+key)%m)+ord('A'))
    txt = message_chiffre
    return txt

# Déchiffrement César
def dechiffre_cesar(txt, key):
    """
    Permet de déchiffrer un message Chiffré txt avec une clé, et retourne le  message Clair.
    """
    m=ord('Z')-ord('A')+1
    message_dechiffre=""
    for c in txt:
        message_dechiffre += chr(((ord(c)-ord('A')-key)%m)+ord('A'))
    txt = message_dechiffre
    return txt

# Chiffrement Vigenere
def chiffre_vigenere(txt, key):
    """
    Permet de chiffrer un message Clair txt avec une clé.
    """
    message_chiffre=""
    for c in range(0, len(txt)):
        message_chiffre += chr((alphabet.index(txt[c]) +key[c%len(key)])%len(alphabet)+ord('A'))   
    txt = message_chiffre
    return txt

# Déchiffrement Vigenere
def dechiffre_vigenere(txt, key):
    """
    Permet de déchiffrer un message Chiffré txt avec une clé.
    """
    message_dechiffre=""
    for c in range(0, len(txt)):
        message_dechiffre += chr((alphabet.index(txt[c]) - key[c%len(key)])%len(alphabet)+ord('A'))   
    txt = message_dechiffre
    return txt

# Analyse de fréquences
def freq(txt): 
    """
    Analyse de fréquences d'un texte txt et retourne un tableau (Histogramme) des frequences des lettres.
    """
    hist=[0.0]*len(alphabet)
    for caractere in txt:
        hist[alphabet.index(caractere)] +=1
    return hist

# Renvoie l'indice dans l'alphabet
# de la lettre la plus fréquente d'un texte
def lettre_freq_max(txt):
    return freq(txt).index(max(freq(txt)))

# indice de coïncidence
def indice_coincidence(hist):
    """
    Applique la formule de l'indice de coincidence de William F. Friedman.
    """
    nb_mot = sum(hist)
    ic = 0
    for caractere in hist:
        ic += (caractere*(caractere -1))/(nb_mot*(nb_mot-1))
    return ic

# Recherche la longueur de la clé
def longueur_clef(cipher):
    """
    Recherche la longueur de la clé grâce à l'indice de coincidence.
    """
    bonne_taille = 0.06
    for taille in range (1, 20):
        ic = 0
        for l in range(1,taille):
            ic += indice_coincidence(freq(cipher[(l-1):len(cipher):taille]))
        if(ic/taille > bonne_taille):
            return taille
    return 0
    
# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en utilisant la lettre la plus fréquente
# de chaque colonne
def clef_par_decalages(cipher, key_length):
    """
    Renvoie le tableau des décalages probables étant
    donné la longueur de la clé
    en utilisant la lettre la plus fréquente
    de chaque colonne
    """
    decalages=[0]*key_length
    for i in range(0, key_length):
        decalages[i]=(lettre_freq_max(cipher[i:len(cipher):key_length])-alphabet.index('E'))%len(alphabet)
    return decalages

# Cryptanalyse V1 avec décalages par frequence max
def cryptanalyse_v1(cipher):
    """
    Cryptanalyse du Chiffrement de Vigenère : longueur de la clef etprincipe de cryptanalyse
    """
    length_key = longueur_clef(cipher)
    key = clef_par_decalages(cipher, length_key)
    if(len(key)> 0):
        return dechiffre_vigenere(cipher, key)
    return "Pas de key"

################################################################
#   1) Combien de textes sont correctement cryptanalysés ?
#       11 texts successfully unciphered.
#       Test cryptanalyse_v1 : OK
#
#   2) Comment expliquez-vous cela ?
#      On découpe le texte chiffré en bloc de caractères et on applique une cryptanalyse par décalage sur les colonnes !
#      mais les sous-textes produits sont plus courts, donc l'analyse des fréquences nous fournit moins d'informations.
#      On déduit que c'est plus difficile pour trouver la clef
################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V2.

# Indice de coincidence mutuelle avec décalage
def indice_coincidence_mutuelle(h1,h2,d):
    """
    Applique la formule de l'indice de coincidence  mutuelle de William F. Friedman 
    """
    nb_mot_text1 = sum(h1)
    nb_mot_text2 = sum(h2)
    ic = 0
    for i in  range(len(h1)):
        ic += ((h1[i])*(h2[(i+d)%len(alphabet)])/((nb_mot_text1)*(nb_mot_text2)))
    return ic

# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en comparant l'indice de décalage mutuel par rapport
# à la première colonne
def tableau_decalages_ICM(cipher, key_length):
    """
    Renvoie le tableau des décalages probables étant
    donné la longueur de la clé
    en comparant l'indice de décalage mutuel par rapport
    à la première colonne
    """
    decalages=[0]*key_length
    h1=freq(cipher[0:len(cipher):key_length])
    icm =[]
    for i in range(key_length):
        for j in range(0,len(alphabet)):
            icm.append(indice_coincidence_mutuelle(h1,freq(cipher[i:len(cipher):key_length]),j))
        decalages[i]=icm.index(max(icm))
        icm =[]
    return decalages

# Cryptanalyse V2 avec décalages par ICM
def cryptanalyse_v2(cipher):
    """
    Cryptanalyse du chiffrement de Vigenère avec les indices de coïncidence
    """
    # On récupére la clé
    key_length = longueur_clef(cipher)
    if(key_length != 0):
        # On récupére le tableau de décalages 
        decalages = tableau_decalages_ICM(cipher, key_length)
        j=0
        text_chifrre_en_cesar = ""
        # On parcourt le texte et on décale chaque lettre grâce au tableau décalages
        for i in cipher:
            text_chifrre_en_cesar+=dechiffre_cesar(i, decalages[j%len(decalages)])
            j+=1
        text_dechifrre_en_cesar = ""
        # On récupére la fréquence maximum du texte
        freq_max=lettre_freq_max(text_chifrre_en_cesar)
        # On récupére le décalage
        decalage=(freq_FR.index(max(freq_FR))-freq_max)%len(alphabet)
        for i in text_chifrre_en_cesar:
            text_dechifrre_en_cesar+=chiffre_cesar(i, decalage)
        return text_dechifrre_en_cesar
    else:
        return cipher

################################################################
#   1) Combien de textes sont correctement cryptanalysés ?
#     42 texts successfully unciphered.
#     Test cryptanalyse_v2 : OK
#
#   2) Comment expliquez-vous cela ?
#      L’indice de coïncidence mutuelle(ICM) entre deux textes t1 et t2 est la probabilité de tirer au hasard la même lettre dans t1 et t2
#      Découper le texte en colonnes C ,  on calucul la moyenne, Si m>0.06 alors l est la longueur de la clef, sinon on passe à la valeur suivante
#      je suposse donc que pour les textes non déchifrés, si on trouve une moyenne inferieure à 0,06 on itére sur une autre taille, mais il arrive qu'on
#      ne trouve pas de moyenne > 0,06 dans ces textes la.
#
#
################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V3.


def esperance (X):
    return sum(X)/len(X)

# Prend deux listes de même taille et
# calcule la correlation lineaire de Pearson
def correlation(L1,L2):
    """
    Applique la formule de Corrélation de Pearson
    """
    correlation = 0.0
    A=0.0
    B=0.0
    C=0.0
    X = esperance(L1)
    Y = esperance(L2)

    for i in range(len(L1)):
        A+=(L1[i]-X)*(L2[i]-Y)
        B+=(L1[i]-X)*(L1[i]-X)
        C+=(L2[i]-X)*(L2[i]-Y)

    correlation = A/(math.sqrt(B*C))
    return correlation

# Renvoie la meilleur clé possible par correlation
# étant donné une longueur de clé fixée
def clef_correlations(cipher, key_length):
    """
    Renvoie la meilleur clé possible par correlation
    étant donné une longueur de clé fixée
    """
    key=[0]*key_length
    score = 0.0

    for i in range(key_length):
        maxCorel = [0]*len(alphabet)
        for j in range(len(alphabet)):
            maxCorel[j] = correlation(freq(dechiffre_cesar(cipher[i:len(cipher):key_length], j)),freq_FR)
        key[i] = maxCorel.index(max(maxCorel))
        score+=(max(maxCorel)/key_length)
    return (score, key)

# Cryptanalyse V3 avec correlations
def cryptanalyse_v3(cipher):
    """
    Utilisation de la corrélation de Pearson pour la cryptanalyse de Vigenère
    """
    resultat=list()
    for i in range(20): 
        resultat.append(clef_correlations(cipher,i))
    score = [a for (a,b) in resultat]

    index = score.index(max(score))
    (s,key) = resultat[index]
    return dechiffre_vigenere(cipher, key)

################################################################
#   1) Combien de textes sont correctement cryptanalysés ?
#     94 texts successfully unciphered.
#     Test cryptanalyse_v3 : OK
#
#   2) Comment expliquez-vous cela ?
#      Le coefficient de corrélation de Pearson mesure la qualité de cet alignement et peut donc servir de révélateur pour déterminer si la substitution s'effectuée sur le chiffré C est la bonne.
#      Comme pour la V2, je suppose que la moyenne des corrélations de Pearson ne dépasse jamais 0,06 pour les textes non déchiffrés
#
#
# ###############################################################

################################################################
# NE PAS MODIFIER LES FONCTIONS SUIVANTES
# ELLES SONT UTILES POUR LES TEST D'EVALUATION
################################################################


# Lit un fichier et renvoie la chaine de caracteres
def read(fichier):
    f=open(fichier,"r")
    txt=(f.readlines())[0].rstrip('\n')
    f.close()
    return txt

# Execute la fonction cryptanalyse_vN où N est la version
def cryptanalyse(fichier, version):
    cipher = read(fichier)
    if version == 1:
        return cryptanalyse_v1(cipher)
    elif version == 2:
        return cryptanalyse_v2(cipher)
    elif version == 3:
        return cryptanalyse_v3(cipher)

def usage():
    print ("Usage: python3 cryptanalyse_vigenere.py -v <1,2,3> -f <FichierACryptanalyser>", file=sys.stderr)
    sys.exit(1)

def main(argv):
    size = -1
    version = 0
    fichier = ''
    try:
        opts, args = getopt.getopt(argv,"hv:f:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-v"):
            version = int(arg)
        elif opt in ("-f"):
            fichier = arg
    if fichier=='':
        usage()
    if not(version==1 or version==2 or version==3):
        usage()

    print("Cryptanalyse version "+str(version)+" du fichier "+fichier+" :")
    print(cryptanalyse(fichier, version))
    
if __name__ == "__main__":
   main(sys.argv[1:])
