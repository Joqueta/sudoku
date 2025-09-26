##Travail fait par Axel Barbellion et Fritzi Frois le 26/09/2025

##grille exemple
grille1 = [[0, 0, 1, 0],
           [0, 0, 0, 3],
           [0, 0, 0, 2],
           [2, 0, 3, 0]]
##grille test 9x9
grille2 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def case_vide(grille):
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == 0:
                return (i, j) 
    return None

def test_valeur(grille, ligne, col, val):
    n = len(grille)
    for i in range(n):
        if grille[ligne][i] == val:
            return False
    for i in range(n):
        if grille[i][col] == val:
            return False
    taille_carre = int(n**0.5)
    ligne_carre = (ligne // taille_carre) * taille_carre
    col_carre = (col // taille_carre) * taille_carre
    for i in range(ligne_carre, ligne_carre + taille_carre):
        for j in range(col_carre, col_carre + taille_carre):
            if grille[i][j] == val:
                return False
    return True

def sudoku(grille):
    n=len(grille)
    vide = case_vide(grille)
    if not vide:
        return True
    ligne, col = vide
    for val in range(1, n+1):
        if test_valeur(grille, ligne, col, val):
            grille[ligne][col] = val
            if sudoku(grille):
                return True
            grille[ligne][col] = 0  
    return False

def afficher_grille(grille):
    if sudoku(grille):
        for ligne in grille:
            print(ligne)
    else:
        print("Aucune solution trouvée")


afficher_grille(grille1)
afficher_grille(grille2)


##Le nombre de noeuds qu'il faut pour résoudre un sudoku de 2x2 entièrement vide est de 288 car il y a 4! (24) façons de placer les chiffres 1 à 4 dans la première ligne, et pour chaque configuration de la première ligne, il y a 12 façons de compléter le reste de la grille en respectant les règles du Sudoku. Donc, 24 * 12 = 288.