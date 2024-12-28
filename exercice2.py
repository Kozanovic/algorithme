def prod_div_sum(num):
    l = [int(digit) for digit in str(num)]
    sum = 0
    prod = 1

    for digit in l:
        sum += digit
        prod *= digit

    if (prod % sum == 0):
        print(f"la somme de {n} : {sum} divise son produit: {prod}")
    else :
        print('erreur')

n = input("entrez un nombre:")

prod_div_sum(n)

# Début
#     // Déclaration des variables
#     Déclarer n comme Entier
#     Déclarer somme comme Entier
#     Déclarer produit comme Entier
#     Déclarer chiffre comme Entier

#     // Demander à l'utilisateur d'entrer un nombre n
#     Afficher "Entrez un nombre : "
#     Lire n

#     // Initialiser la somme et le produit
#     Initialiser somme à 0
#     Initialiser produit à 1

#     // Parcourir chaque chiffre du nombre n
#     Pour chaque chiffre dans n faire
#         // Ajouter le chiffre à la somme
#         Ajouter chiffre à somme

#         // Multiplier le produit par le chiffre
#         Multiplier produit par chiffre
#     Fin Pour

#     // Vérifier si le produit est divisible par la somme
#     Si produit mod somme = 0 alors
#         Afficher "La somme de", n, "divise son produit."
#     Sinon
#         Afficher "Erreur"
#     Fin Si
# Fin
