# Plateaux représentant le début, le milieu et la fin du jeu
plateau_debut = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
]

plateau_milieu = [
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
]

plateau_fin = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 2],
    [2, 2, 2, 2],
]


LIGNES = {0: "A", 1: "B", 2: "C", 3: "D"}  # Define LIGNES before calling the function
PIONS = {0: " ", 1: "●", 2: "○"}  # Define the PIONS dictionary

pions_noirs = 4
pions_blancs = 4

def choisir_plateau():
    while True:
        choix = input("Entrez votre choix (1, 2 ou 3) : ")
        if choix in ['1', '2', '3']:
            if choix == '1':
                plateau = plateau_debut
                return plateau
            elif choix == '2':
                plateau = plateau_milieu
                return plateau
            else:
                plateau = plateau_fin
                return plateau
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

def afficher_plateau(plateau):
    # Couleurs pour les pions
    couleur_pion = {1: '\033[91m', 2: '\033[96m', 0: '\033[0m'}
    print('     1   2   3   4')
    for ligne_index, ligne in enumerate(plateau):
        print(' {} | '.format(LIGNES[ligne_index]), end='')
        for case in ligne:
            print(couleur_pion[case] + PIONS[case] + '\033[0m' + ' | ', end='')
        print()



def _lettre_vers_num(lettre):
    return ord(lettre.lower()) - ord('a')


def est_mouvement_capture(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
    # Déterminer la différence entre les lignes et les colonnes
    diff_ligne = ligne_destination - ligne_origine
    diff_colonne = colonne_destination - colonne_origine

    if (abs(diff_ligne) == 2 and abs(diff_colonne) == 0) or (abs(diff_ligne) == 0 and abs(diff_colonne) == 2):
        return True
    return False


def mouvement_valide(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
    # Valider dans le plateau
    if (0 <= ligne_origine < 4 and 0 <= colonne_origine < 4 and 0 <= ligne_destination < 4
            and 0 <= colonne_destination < 4):

        # Vérifier si le mouvement est un mouvement de capture
        if abs(ligne_origine - ligne_destination) == 2 or abs(colonne_origine - colonne_destination) == 2:
            return True

        # Valider mouvement orthogonal et distance de 1 case
        elif ((abs(ligne_origine - ligne_destination) == 1 and colonne_origine == colonne_destination)
              or (ligne_origine == ligne_destination and abs(colonne_origine - colonne_destination) == 1)):
            # Valider si la case de destination est vide
            if plateau[ligne_destination][colonne_destination] == 0:
                return True
            # Gérer le cas où la case de destination est occupée par un pion de la même couleur
            if (plateau[ligne_destination][colonne_destination] != 0 and
                    plateau[ligne_destination][colonne_destination] == tour):
                return False
        return False
    return False


def est_orthogonal_distance_2_ou_1(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
    # Déterminer la différence entre les lignes et les colonnes
    diff_ligne = ligne_destination - ligne_origine
    diff_colonne = colonne_destination - colonne_origine

    # Un déplacement est orthogonal et de distance 2 ou 1 si :
    # - La différence entre les lignes et les colonnes est de 0 ou 1
    # - La distance entre les deux cases est de 1 ou 2
    return ((abs(diff_ligne) == 1 and diff_colonne == 0) or (diff_ligne == 0 and abs(diff_colonne) == 1)
            or (abs(diff_ligne) == 2 and abs(diff_colonne) == 0) or (abs(diff_ligne) == 0 and abs(diff_colonne) == 2))


def capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
    # Valider saut
    if est_orthogonal_distance_2_ou_1(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
        if abs(ligne_origine - ligne_destination == 2) or abs(colonne_origine - colonne_destination) == 2:
            ligne_intermediaire = (ligne_origine + ligne_destination) // 2
            colonne_intermediaire = (colonne_origine + colonne_destination) // 2

            # Valider si le pion intermédiaire est de l'équipe
            if plateau[ligne_intermediaire][colonne_intermediaire] == plateau[ligne_origine][colonne_origine]:
                return True
            print("Vous ne pouvez pas sauter sur un pion enemi")
            return False
        return False
    print("Mouvement non orthogonal ou distance invalide. err 77")
    return False


def effectuer_mouvement(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination):
    plateau[ligne_destination][colonne_destination] = plateau[ligne_origine][colonne_origine]
    plateau[ligne_origine][colonne_origine] = 0


def changer_tour():
    global tour
    if tour == 'bleus':
        tour = 'rouges'
    else:
        tour = 'bleus'


def compter_pions():
    global pions_noirs, pions_blancs
    pions_noirs = 0
    pions_blancs = 0
    for ligne in plateau:
        for case in ligne:
            if case == 1:
                pions_blancs += 1
            elif case == 2:
                pions_noirs += 1


def fin_du_jeu(plateau):
    global pions_noirs, pions_blancs

    # Vérifier si le nombre de pions est inférieur à 2
    if pions_noirs < 2 or pions_blancs < 2:
        return True

    # Déterminer le tour actuel
    tour = "bleu" if pions_noirs % 2 == 1 else "rouge"

    # Parcourir toutes les cases du plateau
    for ligne in range(4):
        for colonne in range(4):
            # Vérifier si le pion a des mouvements possibles
            for ligne_destination in range(4):
                for colonne_destination in range(4):
                    if mouvement_valide(plateau, ligne, colonne, ligne_destination, colonne_destination, tour):
                        # Si un mouvement est possible, le joueur n'est pas mat
                        return False

    # Si aucun mouvement n'est possible, le joueur est mat
    return True


def demander_mouvement(tour):
    origine = None
    destination = None

    while not origine or not destination:
        print(afficher_message_couleur(f"Tour: {tour}", couleur="jaune", gras=True))
        # Demander la case d'origine
        origine = input(afficher_message_couleur('Entrez la case d\'origine (lettre et numéro) : ', couleur="cyan", gras=False))

        # Demander la case de destination
        destination = input(afficher_message_couleur('Entrez la case de destination (lettre et numéro) : ', couleur="cyan", gras=False))

        if not _valider_case(origine) or not _valider_case(destination):
            print(afficher_message_couleur("Mouvement invalide : format incorrect.", couleur="rouge"))
            origine = None
            destination = None

    ligne_origine = _lettre_vers_num(origine[0])
    colonne_origine = int(origine[1]) - 1
    ligne_destination = _lettre_vers_num(destination[0])
    colonne_destination = int(destination[1]) - 1

    return ligne_origine, colonne_origine, ligne_destination, colonne_destination



def _valider_case(case):
    if len(case) != 2:
        return False
    if not case[0].isalpha():
        return False
    if not case[1].isdigit():
        return False
    return True


def afficher_message_couleur(message, couleur="reset", gras=False, italique=False):
    codes_style = {
        "gras": "\033[1m",
        "italique": "\033[3m"
    }

    codes_couleur = {
        "reset": "\033[0m",
        "noir": "\033[30m",
        "rouge": "\033[31m",
        "vert": "\033[32m",
        "jaune": "\033[33m",
        "bleu": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "blanc": "\033[37m",
        "fond_noir": "\033[40m",
        "fond_rouge": "\033[41m",
        "fond_vert": "\033[42m",
        "fond_jaune": "\033[43m",
        "fond_bleu": "\033[44m",
        "fond_magenta": "\033[45m",
        "fond_cyan": "\033[46m",
        "fond_blanc": "\033[47m",
    }

    code_couleur = codes_couleur.get(couleur.lower(), "")
    code_style = codes_style.get("gras" if gras else "italique" if italique else "")

    if not couleur and not gras and not italique:
        return message

    message_couleur = f"{code_couleur}{code_style}{message}{codes_couleur['reset']}"
    return message_couleur

def fin_du_jeu(plateau):
    global pions_noirs, pions_blancs

    # Vérifier si le nombre de pions est inférieur à 2
    if pions_noirs < 2 or pions_blancs < 2:
        return True

    # Déterminer le tour actuel
    tour = "bleu" if pions_noirs % 2 == 1 else "rouge"

    # Parcourir toutes les cases du plateau
    for ligne in range(4):
        for colonne in range(4):
            # Vérifier si le pion a des mouvements possibles
            for ligne_destination in range(4):
                for colonne_destination in range(4):
                    if mouvement_valide(plateau,ligne, colonne, ligne_destination, colonne_destination, tour):
                        # Si un mouvement est possible, le joueur n'est pas mat
                        return False

    # Si aucun mouvement n'est possible, le joueur est mat
    return True

#afficher_plateau()


def boucle_jeu():
    print("Choisissez un plateau :")
    print("1. Début du jeu")
    print("2. Milieu du jeu")
    print("3. Fin du jeu")
    tour = 'bleu'
    plateau = choisir_plateau()  # Initialiser la variable tour
    while not fin_du_jeu(plateau):
        # Afficher le plateau choisi
        afficher_plateau(plateau)

        # Demander le mouvement au joueur actuel
        ligne_origine, colonne_origine, ligne_destination, colonne_destination = demander_mouvement(tour)

        # Valider le mouvement
        est_mouvement_valide = mouvement_valide(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour)

        # Vérifier si le mouvement est valide et l'effectuer
        if est_mouvement_valide:
            if est_mouvement_capture(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
                if capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
                    effectuer_mouvement(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination)
                    compter_pions()
                else:
                    afficher_message_couleur("Vous ne pouvez pas sauter sur un pion ennemi.", couleur="rouge")
                    continue  # Revenir au début de la boucle pour redemander le mouvement
            else:
                effectuer_mouvement(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination)
        else:
            afficher_message_couleur("Mouvement invalide. Veuillez réessayer.", couleur="rouge")
            continue  # Revenir au début de la boucle pour redemander le mouvement

        # Changer de tour
        tour = 'rouges' if tour == 'bleus' else 'bleus'

        # Afficher l'état actuel du jeu
        afficher_plateau(plateau)
        afficher_message_couleur('Tour: ' + tour, couleur="jaune", gras=True)
        afficher_message_couleur('Pions Bleus: ' + str(pions_noirs), couleur="magenta")
        afficher_message_couleur('Pions Rouges: ' + str(pions_blancs), couleur="magenta")

    afficher_message_couleur("Le jeu est terminé.", couleur="vert", gras=True)


boucle_jeu()