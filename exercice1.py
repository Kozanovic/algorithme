nombre = int(input('Saisir un nombre : '))
def diff_num(n):
    if n > 0:
        l = [int(digit) for digit in str(n)]
        elem_vu = []
        
        for digit in l:
            if digit in elem_vu:
                print(f"l'entier {n} n'est pas distinct car le chiffre {digit} apparait plus d'un fois")
                break
            else:
                elem_vu.append(digit)
        else:
            print(f"Tous les chiffres de {n} sont distincts.")

diff_num(nombre)
