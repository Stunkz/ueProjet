# -*- coding: utf-8 -*-

# Les Imports sont ici seulement pour rendre le jeux plus visible.
# Ils ne vont pas intervenir dans le code du jeux.
import subprocess
import time

# ___FONCTIONS DE TEST___


def test():
    test_est_au_bon_format()  #Fonction obligatoire
    test_est_dans_grille()    #Fonction Obligatoire
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
    assert est_au_bon_format("A2") == True
    print("Test 1 'OK'")

# Verification des coordonnées


def test_est_dans_grille():
    assert est_dans_grille("A1", grille_debut) == True
    assert est_dans_grille("A4", grille_debut) == True
    assert est_dans_grille("Z5", grille_debut) == False
    assert est_dans_grille("T9", grille_debut) == False
    print("Test 2 'OK'")

# test distance_case_valide


def test_distance_case_valide():
    assert distance_case_valide((0, 0)) == True
    assert distance_case_valide((-3, 0)) == False
    assert distance_case_valide((0, 3)) == False
    assert distance_case_valide((3, -3)) == False
    print("Test 3 'OK'")


# test calcul distance


def test_calcul_distance():
    assert calcul_distance((0, 0), (0, 0)) == (0, 0)
    assert calcul_distance((2, 2), (1, 1)) == (-1, -1)
    assert calcul_distance((1, 1), (2, 2)) == (1, 1)
    print("Test 4 'OK'")


# test pion_milieu


def test_pion_milieu():
    assert pion_milieu(grille_debut, (0, 2), (2, 2)) == True
    assert pion_milieu(grille_debut, (0, 0), (4, 4)) == True
    print("Test 5 'OK'")


# test distance_pour_manger_pion


def test_distance_pour_manger_pion():
    assert distance_pour_manger_pion((2, 2), (1, 1)) == False
    assert distance_pour_manger_pion((0, 2), (0, 4)) == True
    assert distance_pour_manger_pion((0, 4), (0, 2)) == True
    print("Test 6 'OK'")

# test distance_pour_deplacement


def test_distance_pour_deplacement():
    assert distance_pour_deplacement((0, 2), (0, 3)) == True
    assert distance_pour_deplacement((0, 2), (0, 5)) == False
    assert distance_pour_deplacement((1, 2), (2, 2)) == True
    print("Test 7 'OK'")

# test saut_valide


def test_saut_valide():
    assert saut_valide(grille_fin, (5, 3), 1) == True
    assert saut_valide(grille_fin, (4, 3), 2) == False
    print("Test 8 'OK'")


# test deplacement_valide


def test_deplacement_valide():
    assert deplacement_valide((0, 2), (0, 1)) == True
    assert deplacement_valide((0, 2,), (0, 4)) == False
    print("Test 9 'OK'")

#  ___ VARIABLES ___

LIGNES = {0: "A", 1: "B", 2: "C", 3: "D"}
PIONS = {0: " ", 1: "●", 2: "○"}

# ____ GRILLES ____

grille_debut = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    ]
grille_milieu = [
    [1, 0, 0, 2],
    [1, 2, 2, 0],
    [2, 2, 0, 1],
    [2, 0, 1, 1],
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
    return len(coord) == 2 and 65 <= int(ord(coord[0])) <= 68 and 0 <= int(coord[1]) - 1 <= 3

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
            coord_brut = input("erreur format de saisie : ")

# Verification des distances entre des coord de départ et d'arrivée

def distance_case_valide(distance):
    return -2 <= distance[0] <= 2 and -2 <= distance[1] <= 2

# Calcul de la distance entre le départ et l'arrivée

def calcul_distance(coord_depart, coord_arrivee):
    return (coord_arrivee[0] - coord_depart[0]), (coord_arrivee[1] - coord_depart[1])  # le [0] et [1] servent pour donner les coord en x et y


def pion_milieu(grille, coord_depart, coord_arrivee):
    distance = calcul_distance(coord_depart, coord_arrivee)
    pion_milieu = (coord_depart[0]+(distance[0]//2),coord_depart[1]+(distance[1]//2))
    return grille[pion_milieu[0]][pion_milieu[1]] != 0

def distance_pour_manger_pion(coord_depart, coord_arrivee):
    distance = calcul_distance(coord_depart, coord_arrivee)
    x = distance[0]
    y = distance[1]
    return ((x==2)and(y==0)) or ((x==0)and(y==2)) or ((x==-2)and(y==0)) or ((x==0)and(y==-2))

def distance_pour_deplacement(coord_depart, coord_arrivee):
    distance = calcul_distance(coord_depart, coord_arrivee)
    x = distance[0]
    y = distance[1]
    return ((x==1)and(y==0)) or ((x==0)and(y==1)) or ((x==-1)and(y==0)) or ((x==0)and(y==-1))

def pion_mangeable(grille, coord_depart, joueur):
    for i in range(len(grille)):
        for j in range(len(grille)):
            coord_arrivee = (i, j)
            distance = calcul_distance(coord_depart, coord_arrivee)
            pion_milieu = (coord_depart[0]+(distance[0]//2),coord_depart[1]+(distance[1]//2))
            if distance_pour_manger_pion(coord_depart, coord_arrivee) and case_vide(coord_arrivee, grille) and grille[pion_milieu[0]][pion_milieu[1]] != joueur and grille[pion_milieu[0]][pion_milieu[1]] != 0:
                return True
    return False

def pion_deplacable(grille, coord_depart):
    for i in range(len(grille)):
        for j in range(len(grille)):
            coord_arrivee = (i, j)
            calcul_distance(coord_depart, coord_arrivee)
            if case_vide(coord_arrivee, grille) and distance_pour_deplacement(coord_depart, coord_arrivee):
                return True
    return False

def jeu_fini(grille, joueur):
    #un des joueurs est en dessus de 6 pions
    nb_pion_blanc = 0 #2
    nb_pion_noir = 0 #1
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == 1:
                nb_pion_noir+=1
            if grille[i][j] == 2:
                nb_pion_blanc+=1

    #un des deux joueurs ne peut plus effectuer de déplacements avec ces pions
    pion_noir_deplacable = 0
    pion_blanc_deplacable = 0
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == 1 and (pion_mangeable(grille, (i, j), 1) or pion_deplacable(grille, (i,j))):
                pion_noir_deplacable += 1
            if grille[i][j] == 2 and (pion_mangeable(grille, (i, j), 2) or pion_deplacable(grille, (i,j))):
                pion_blanc_deplacable += 1

    return (nb_pion_blanc < 2 or nb_pion_noir < 2) or (pion_noir_deplacable == 0 or pion_blanc_deplacable == 0)


def deplacement_simple(grille, coord_depart, coord_arrivee):
    pion = grille[coord_depart[0]][coord_depart[1]]
    grille[coord_depart[0]][coord_depart[1]] = 0
    grille[coord_arrivee[0]][coord_arrivee[1]] = pion
    return grille

def deplacement_saut(grille, coord_depart, coord_arrivee):
    pion = grille[coord_depart[0]][coord_depart[1]]
    distance = calcul_distance(coord_depart, coord_arrivee)
    pion_du_milieu = (coord_depart[0]+(distance[0]//2),coord_depart[1]+(distance[1]//2))
    pion = grille[coord_depart[0]][coord_depart[1]]
    grille[pion_du_milieu[0]][pion_du_milieu[1]] = 0
    grille[coord_depart[0]][coord_depart[1]] = 0
    grille[coord_arrivee[0]][coord_arrivee[1]] = pion
    return grille


def deplacement_valide(coord_depart, coord_arrivee):
    distance = calcul_distance(coord_depart, coord_arrivee)
    return distance[0] == 1 or distance[1] == 1 or distance[0] == -1 or distance[1] == -1

def saut_valide(grille, pion_du_milieu, joueur):
    return grille[pion_du_milieu[0]][pion_du_milieu[1]] > 0 and grille[pion_du_milieu[0]][pion_du_milieu[1]] != joueur

def id_pion_milieu(coord_depart, coord_arrivee):
    distance = calcul_distance(coord_depart, coord_arrivee)
    return (coord_depart[0]+(distance[0]//2),coord_depart[1]+(distance[1]//2))

def pion_restant(grille):   #FONCTION RÉPETE
    pion_noir = 0
    pion_blanc = 0
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == 1:
                pion_noir+=1
            if grille[i][j] == 2:
                pion_blanc+=1
    return (pion_noir, pion_blanc)

def comparer_listes(grille1, grille2):
    for i in range(len(grille1)):
        for j in range(len(grille1)):
            if grille1[i][j] != grille2[i][j]:
                return False
    return True

def list_copy(l):
    copy = [None] * len(l)
    for i in range(len(l)):
        copy[i] = l[i][:]
    return copy


def deplacer_pion(grille, joueur):
    print("Veuillez saisir la coordonnée du pion a déplacer", end="")
    coord_depart = saisir_coordonnees(grille)

    # vérifie si le jouer selectionne bien un pion a lui
    while joueur != grille[coord_depart[0]][coord_depart[1]]:
        print(
            "Vous ne pouvez pas jouer un pion qui n'est pas le votre.\nVeuillez saisir la coordonnée du pion a déplacer",
            end="")
        coord_depart = saisir_coordonnees(grille)

    # verifie que le pion choisi peut se deplacer
    while not (pion_deplacable(grille, coord_depart) or pion_mangeable(grille, coord_depart, joueur)):
        print("Le pion ne peut pas se déplacer.\nVeuillez saisir la coordonnée du pion a déplacer", end="")
        coord_depart = saisir_coordonnees(grille)

    print("Veuillez saisir la coordonnée de le case ou doit atterir le pion", end="")
    coord_arrivee = saisir_coordonnees(grille)
    distance = calcul_distance(coord_depart, coord_arrivee)

    # vérification de la distance
    while not distance_case_valide(distance):
        print("La case est trop éloigné, \nVeuillez saisir la coordonnée de le case ou doit atterir le pion", end="")
        coord_arrivee = saisir_coordonnees(grille)
        distance = calcul_distance(coord_depart, coord_arrivee)

    # vérification si la case est bien vide a l'arrivée
    while not case_vide(coord_arrivee, grille):
        print("La case contient déjà un pion, \nVeuillez saisir la coordonnée de le case ou doit atterir le pion",
              end="")
        coord_arrivee = saisir_coordonnees(grille)
        distance = calcul_distance(coord_depart, coord_arrivee)

    # 2 cas s'offre a nous, 1er cas il se déplace normalement d'une case, 2 eme cas il veut manger un pion

    if deplacement_valide(coord_depart, coord_arrivee):  # deplacement simple
        grille = deplacement_simple(grille, coord_depart, coord_arrivee)
    else:  # deplacement saut
        pion_du_milieu = id_pion_milieu(coord_depart, coord_arrivee)
        if saut_valide(grille, pion_du_milieu, joueur):
            grille = deplacement_saut(grille, coord_depart, coord_arrivee)
            if pion_mangeable(grille, coord_arrivee, joueur):
                return grille, coord_arrivee
        else:
            print("Vous voulez déplacer un pion de 2 cases sans en manger un ou vous voulez manger un de vos pions.\n")
            # on demande de resaisir les coordonnée pour choisir un nouveau pion dans le programme principal car la recursivité n'est pas autorisée

    return grille, 0


### FONCTION POUR ENCHAINER LES PIONS

def enchainement(grille, coord_depart, joueur):
    while pion_mangeable(grille, coord_depart, joueur):
        print("Veuillez saisir la coordonnée d'arrivée du pion", end="")
        coord_arrivee = saisir_coordonnees(grille)

        while not case_vide(coord_arrivee, grille):
            print("La case contient déjà un pion.\nveuillez resaisir la coordonnée d'arrivée du pion", end="")
            coord_arrivee = saisir_coordonnees(grille)

        distance = calcul_distance(coord_depart, coord_arrivee)

        while not distance_saut_valide(distance):
            print("La distance n'est pas correcte.\nveuillez resaisir la coordonnée d'arrivée du pion", end="")
            coord_arrivee = saisir_coordonnees(grille)

        pion_du_milieu = id_pion_milieu(coord_depart, coord_arrivee)

        while not saut_valide(grille, pion_du_milieu, joueur):
            print(
                "Vous voulez déplacer un pion de 2 cases sans en manger un ou vous voulez manger un de vos pions.\nVeuillez resaisir la coordonnée d'arrivée du pion",
                end="")
            coord_arrivee = saisir_coordonnees(grille)

        grille = deplacement_saut(grille, coord_depart, coord_arrivee)
        subprocess.call('cls', shell=True)  # clear la console pour ne pas voir les affichages précedents
        print("---------- Binvenue dans le jeu Marée ! ----------\n")
        afficher_grille(grille)
        print("c'est au tour du joueur", joueur, "\n")
        pions = pion_restant(grille)
        print("Pions noirs (joueur 1 ●) :", pions[0], "| Pions blancs (joueur 2 ○) :", pions[1], "\n")
        coord_depart = coord_arrivee

        if pion_mangeable(grille, coord_depart, joueur):
            choix = input("Voulez vous continuer ? (0 : oui / 1 : non) : \n")
            while choix != "0" and choix != 1:
                print("Veuillez saisir 0 pour oui et 1 pour non.\n")
                choix = input("Voulez vous continuer ? (0 : oui / 1 : non) : \n")
            choix = int(choix)
            if choix == 1:
                return grille

    return grille


### FONCTION QUI VALIDE LA DISTANCE DE DEPLACEMENT EN SAUT

def distance_saut_valide(distance):
    return distance == (2, 0) or distance == (-2, 0) or distance == (0, 2) or distance == (0, -2)


test()

# affichage des grilles

print("Grille début de partie :")
afficher_grille(grille_debut)
print("Pions ● restant : 8 | Pions ○ restant : 8")
print("C'est au tour du joueur 1 ●")
print("--------------------------")
print("Grille milieu de partie :")
afficher_grille(grille_milieu)
print("Pions ● restant : 5 | Pions ○ restant : 6")
print("C'est au tour du joueur 2 ○")
print("--------------------------")
print("Grille fin de partie :")
afficher_grille(grille_fin)
print("Pions ● restant : 2 | Pions ○ restant : 2")
print("C'est au tour du joueur 2 ○")
print("--------------------------")

# demande au joueur sur quelle grille il veut jouer

print("Sur quelle grille voulez vous jouer ?")
print("1 : Grille début")
print("2 : Grille début")
print("3 : Grille début")
choix = input()
while choix != "1" and choix != "2" and choix != "3":
    print("Veuillez saisir 1, 2 ou 3 pour choisir la configuration.")
    choix = input()

choix = int(choix)

if choix == 1:
    grille = list_copy(grille_debut)
    joueur = 1

if choix == 2:
    grille = list_copy(grille_milieu)
    joueur = 2

if choix == 3:
    grille = list_copy(grille_fin)
    joueur = 2

subprocess.call('cls', shell=True)  # clear la console pour ne pas voir les affichages précedents

print("Avec quel joueur voulez vous jouer ?")
print("1 : Joueur 2")
print("2 : IA\n !(beta)!")

choix_joueur = input()
while choix_joueur != "1" and choix_joueur != "2":
    print("Veuillez saisir 1 ou 2 pour choisir un adversaire.")
    choix_joueur = input()

subprocess.call('cls', shell=True)  # clear la console pour ne pas voir les affichages précedents

if choix_joueur == "1":
    i = 0
    while i == 0:
        print("---------- Binvenue dans le jeu des Canaries ! ----------\n")

        afficher_grille(grille)
        print("c'est au tour de", joueur, "\n")
        pions = pion_restant(grille)
        print("Pions noirs (joueur 1 ●) :", pions[0], "| Pions blancs (joueur 2 ○) :", pions[1], "\n")

        # cas 2 de la fonction deplacer_pion traité ici pour éviter d'utiliser la récursivité

        save_grille = list_copy(grille)
        grille, coord_enchainement = deplacer_pion(grille, joueur)
        while comparer_listes(save_grille, grille):
            print("Déplavement invalide, veuillez esssayer à nouveau.", "\n")
            grille, coord_enchainement = deplacer_pion(grille, joueur)

        subprocess.call('cls', shell=True)  # clear la console pour ne pas voir les affichages précedents
        print("---------- Binvenue ! ----------\n")
        print("-------- Jeux des Canaries --------\n")
        afficher_grille(grille)
        print("c'est au tour de", joueur, "\n")
        pions = pion_restant(grille)
        print("Pions noirs (joueur 1 ●) :", pions[0], "| Pions blancs (joueur 2 ○) :", pions[1], "\n")
        if coord_enchainement != 0 and pion_mangeable(grille, coord_enchainement, joueur):
            choix_enchainement = input("Souhaitez vous enchainer le saut de pions ? (0 : oui / 1 : non) : \n")
            while choix_enchainement != "0" and choix_enchainement != "1":
                print("Veuillez saisir 0 pour oui et 1 pour non.")
                choix_enchainement = input("Souhaitez vous enchainer le saut de pions ? (0 : oui / 1 : non) : \n")
            choix_enchainement = int(choix_enchainement)
            if choix_enchainement == 0:
                grille = enchainement(grille, coord_enchainement, joueur)

        # changement de tour des joueurs
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1

        # savoir si le jeu est fini (pion en dessous de 6 ou aucun déplacement possible)

        if jeu_fini(grille, joueur):
            pions = pion_restant(grille)
            print("Pions noirs :", pions[0], "| Pions blancs :", pions[1], "\n")
            print("Joueur", joueur, "a gagné\n")
            time.sleep(3)  # laisse le temps au joueur de voir qui a gagné
            i = 1

        subprocess.call('cls', shell=True)  # clear la console pour ne pas voir les affichages précedents

    else:
        print("Zone en construction")
        print("Prochainement sera disponible!!")