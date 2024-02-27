# Position initiale
plateau = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    ]
LIGNES = {0: "A", 1: "B", 2: "C", 3: "D"}  # Define LIGNES before calling the function
PIONS = {0: " ", 1: "●", 2: "○"}  # Define the PIONS dictionary

pions_noirs = 4
pions_blancs = 4
tour = 'noirs'

def afficher_plateau():
  for ligne_index, ligne in enumerate(plateau):
    print(' {} | '.format(LIGNES[ligne_index]), end='')
    print(' | '.join(PIONS[case] for case in ligne), end='')
    print(' |')

def _lettre_vers_num(lettre):
  return ord(lettre.lower()) - ord('a')

def est_mouvement_capture(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  # Déterminer la différence entre les lignes et les colonnes
  diff_ligne = ligne_destination - ligne_origine
  diff_colonne = colonne_destination - colonne_origine

  if (abs(diff_ligne) == 2 and abs(diff_colonne) == 0) or (abs(diff_ligne) == 0 and abs(diff_colonne) == 2):
    return True
  return False


def mouvement_valide(ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
  # Valider dans le plateau
  if (0 <= ligne_origine < 4 and 0 <= colonne_origine < 4 and 0 <= ligne_destination < 4 and 0 <= colonne_destination < 4):

    # Vérifier si le mouvement est un mouvement de capture
    if (abs(ligne_origine - ligne_destination) == 2 or abs(colonne_origine - colonne_destination) == 2):
      return True

    # Valider mouvement orthogonal et distance de 1 case
    elif (abs(ligne_origine - ligne_destination) == 1 and colonne_origine == colonne_destination) or (ligne_origine == ligne_destination and abs(colonne_origine - colonne_destination) == 1):
      # Valider si la case de destination est vide
      if plateau[ligne_destination][colonne_destination] == 0:
        return True
      # Gérer le cas où la case de destination est occupée par un pion de la même couleur
      if plateau[ligne_destination][colonne_destination] != 0 and plateau[ligne_destination][colonne_destination] == tour:
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
  return (abs(diff_ligne) == 1 and diff_colonne == 0) or (diff_ligne == 0 and abs(diff_colonne) == 1) or (abs(diff_ligne) == 2 and abs(diff_colonne) == 0) or (abs(diff_ligne) == 0 and abs(diff_colonne) == 2)


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

def effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  plateau[ligne_destination][colonne_destination] = plateau[ligne_origine][colonne_origine]
  plateau[ligne_origine][colonne_origine] = 0

def changer_tour():
  global tour
  if tour == 'noirs':
    tour = 'blancs'
  else:
    tour = 'noirs'

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

def fin_du_jeu():
  global pions_noirs, pions_blancs

  # Vérifier si le nombre de pions est inférieur à 2
  if pions_noirs < 2 or pions_blancs < 2:
    return True

  # Déterminer le tour actuel
  tour = "noir" if pions_noirs % 2 == 1 else "blanc"

  # Parcourir toutes les cases du plateau
  for ligne in range(4):
    for colonne in range(4):
      # Vérifier si le pion a des mouvements possibles
      for ligne_destination in range(4):
        for colonne_destination in range(4):
          if mouvement_valide(ligne, colonne, ligne_destination, colonne_destination, tour):
            # Si un mouvement est possible, le joueur n'est pas mat
            return False

  # Si aucun mouvement n'est possible, le joueur est mat
  return True



def demander_mouvement():
  origine = None
  destination = None

  while not origine or not destination:
    print("tour:", tour)
    # Demander la case d'origine
    origine = input('Entrez la case d\'origine (lettre et numéro) : ').strip().upper()
    if not _valider_case(origine):
      print('Mouvement invalide : format incorrect. err 99')

    # Demander la case de destination
    destination = input('Entrez la case de destination (lettre et numéro) : ').strip().upper()
    if not _valider_case(destination):
      print('Mouvement invalide : format incorrect.err 104')

  ligne_origine = _lettre_vers_num(origine[0])
  colonne_origine = int(origine[1])-1
  ligne_destination = _lettre_vers_num(destination[0])
  colonne_destination = int(destination[1])-1

  return ligne_origine, colonne_origine, ligne_destination, colonne_destination


def convertir_case(ligne, colonne):
    lettre = _lettre_vers_num(colonne)
    numero = str(ligne + 1)
    return lettre + numero

def _valider_case(case):
  if len(case) != 2:
    return False
  if not case[0].isalpha():
    return False
  if not case[1].isdigit():
    return False
  return True


afficher_plateau()
def boucle_jeu():
  while not fin_du_jeu():
    # Demander le mouvement au joueur actuel
    ligne_origine, colonne_origine, ligne_destination, colonne_destination = demander_mouvement()

    # Valider le mouvement et l'effectuer
    if mouvement_valide(ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
      if est_mouvement_capture(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
        if capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
          effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination)
          compter_pions()
      else:
        effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination)
    else:
      print('Mouvement non valide : en dehors du plateau ou mouvement non orthogonal. err 143')

    # Changer de tour
    changer_tour()

    # Afficher le plateau et l'état actuel
    afficher_plateau()
    print('Tour: ' + tour)
    print('Pions noirs: ' + str(pions_noirs))
    print('Pions blancs: ' + str(pions_blancs))
  return True

boucle_jeu()