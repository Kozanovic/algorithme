N = int(input("saisir un nombre positif : "))
est_auto_nombre = True

if N <= 0:
    print('veuillez saisir un nombre positif')
else:
    for M in range(1, N):
        somme_chiffres = 0
        for chiffre in str(M):
            somme_chiffres += int(chiffre)
            if N == M + somme_chiffres:
                est_auto_nombre = False
            break
    
if est_auto_nombre:
    print(f"{N} est un auto-nombre.")
else:
    print(f"{N} n'est pas un auto-nombre.")
