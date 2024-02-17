# -*- coding: utf-8 -*-

# Les Imports sont ici seulement pour rendre le jeux plus visible.
# Ils ne vont pas intervenir dans le code du jeux.
import subprocess
import time

# ___FONCTIONS DE TEST___


def test():
    test_est_au_bon_format()
    test_est_dans_grille()
    test_distance_case_valide()
    test_calcul_distance()
    test_pion_milieu()
    test_distance_pour_manger_pion()
    test_distance_pour_deplacement()
    test_saut_valide()
    test_deplacement_valide()
    print("Tests completés")

# Verification du format des inputs


def test_est_au_bon_format():
    assert est_au_bon_format("") == False
    assert est_au_bon_format("1") == False
    assert est_au_bon_format("A") == False
    assert est_au_bon_format("a") == False
    assert est_au_bon_format("aaaaa") == False
    assert est_au_bon_format("77777") == False
    assert est_au_bon_format("7A") == False
    assert est_au_bon_format("A7") == True

# Verification des coordonnées


def test_est_dans_grille():
    assert est_dans_grille("A0", grille_debut) == True
    assert est_dans_grille("A8", grille_debut) == False
    assert est_dans_grille("Z5", grille_debut) == False
    assert est_dans_grille("T9", grille_debut) == False

# test distance_case_valide


def test_distance_case_valide():
    assert distance_case_valide((0, 0)) == True
    assert distance_case_valide((-3, 0)) == False
    assert distance_case_valide((0, 3)) == False
    assert distance_case_valide((3, -3)) == False


# test calcul distance


def test_calcul_distance():
    assert calcul_distance((0, 0), (0, 0)) == (0, 0)
    assert calcul_distance((2, 2), (1, 1)) == (-1, -1)
    assert calcul_distance((1, 1), (2, 2)) == (1, 1)


# test pion_milieu


def test_pion_milieu():
    assert pion_milieu(grille_fin, (0, 2), (2, 2)) == True
    assert pion_milieu(grille_fin, (0, 2), (0, 4)) == False


# test distance_pour_manger_pion


def test_distance_pour_manger_pion():
    assert distance_pour_manger_pion((2, 2), (1, 1)) == False
    assert distance_pour_manger_pion((0, 2), (0, 4)) == True
    assert distance_pour_manger_pion((0, 4), (0, 2)) == True

# test distance_pour_deplacement


def test_distance_pour_deplacement():
    assert distance_pour_deplacement((0, 2), (0, 3)) == True
    assert distance_pour_deplacement((0, 2), (0, 5)) == False
    assert distance_pour_deplacement((1, 2), (2, 2)) == True

# test saut_valide


def test_saut_valide():
    assert saut_valide(grille_fin, (5, 3), 1) == True
    assert saut_valide(grille_fin, (4, 3), 2) == False


# test deplacement_valide


def test_deplacement_valide():
    assert deplacement_valide((0, 2), (0, 1)) == True
    assert deplacement_valide((0, 2,), (0, 4)) == False

### VARIABLES

LIGNES = {0: "A", 1: "B", 2: "C", 3: "D"}
PIONS = {0: " ", 1: "●", 2: "○"}

### INITIALISATION DES GRILLES

grille_debut = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    ]

grille_fin = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 2, 1, 0],
    [1, 1, 1, 2],
    ]

# ____PARTIE GRAPHIQUE____

def afficher_grille(grille):
    print("   1 2 3 4 ")
    for i in range(len(grille)):
        print(LIGNES[i], "|", end="")
        for j in range(len(grille[i])):
            print(PIONS[grille[i][j]], end="|")
        print("")
    print("")


# FONCTION CASE VIDE

def case_vide(coord, grille):
    return grille[coord[0]][coord[1]] == 0

# FONCTION BON FORMAT

def est_au_bon_format(coord):
    return len(coord) == 2 and 65 <= int(ord(coord[0])) <= 90 and 0 <= int(coord[1]) - 1 <= 4

# VERIFICATION DANS GRILLE

def est_dans_grille(coord, grille):
    return 0 <= ord(coord[0]) - 65 < len(grille_debut) and 0 <= int(coord[1]) - 1 < len(grille_debut)

# Gestion de saisie


def saisir_coordonnees(grille):
    coord_brut = input(" (!! format LETTRE CHIFFRE ex : C3) : ")
    i = 0
    while i == 0:
        if (est_au_bon_format(coord_brut) and est_dans_grille(coord_brut, grille)):
            coord = ord(coord_brut[0]) - 65, int(coord_brut[1]) - 1
            i = 1
            return coord
        else:
            coord_brut = input("erreur 144 format de saisie : ")

# Verification des distances entre des coord de départ et d'arrivée

def distance_case_valide(distance):
    return -2 <= distance[0] <= 2 and -2 <= distance[1] <= 2
# Fonction de calcul entre
