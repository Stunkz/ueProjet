# Position initiale
plateau = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    ]
LIGNES = {0: "A", 1: "B", 2: "C", 3: "D"}  # Define LIGNES before calling the function
PIONS = {0: " ", 1: "●", 2: "○"}  # Define the PIONS dictionary

pions_noirs = 2
pions_blancs = 2
tour = 'noirs'

def afficher_plateau():
  for ligne_index, ligne in enumerate(plateau):
    print(' {} | '.format(LIGNES[ligne_index]), end='')
    print(' | '.join(PIONS[case] for case in ligne), end='')
    print(' |')

def _lettre_vers_colonne(lettre):
  return ord(lettre.lower()) - ord('a')

def mouvement_valide(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  # Valider dans le plateau
  if not (0 <= ligne_origine < 4 and 0 <= colonne_origine < 4 and 0 <= ligne_destination < 4 and 0 <= colonne_destination < 4):
    return False

  # Valider mouvement orthogonal et distance de 2 cases
  if (abs(ligne_origine - ligne_destination) == 2 and colonne_origine == colonne_destination) or (
          ligne_origine == ligne_destination and abs(colonne_origine - colonne_destination) == 2):

      # Valider si la case de destination est vide
    if plateau[ligne_destination][colonne_destination] == 0:
      # Valider si la case intermédiaire est vide pour un déplacement simple
      if not capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
        ligne_intermediaire = (ligne_origine + ligne_destination) // 2
        colonne_intermediaire = (colonne_origine + colonne_destination) // 2
        if plateau[ligne_intermediaire][colonne_intermediaire] != 0:
          return False
      return True
  return False


def capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
    # Valider saut
    if abs(ligne_origine - ligne_destination) == 2 and abs(colonne_origine - colonne_destination) == 2:
        ligne_intermediaire = (ligne_origine + ligne_destination) // 2
        colonne_intermediaire = (colonne_origine + colonne_destination) // 2

        # Valider si la case intermédiaire est occupée par un pion ennemi
        if plateau[ligne_intermediaire][colonne_intermediaire] != 0:
            # Valider si le pion intermédiaire est de l'équipe adverse
            if plateau[ligne_intermediaire][colonne_intermediaire] != plateau[ligne_origine][colonne_origine]:
                # Valider le tour
                if plateau[ligne_origine][colonne_origine] == tour:
                    return True

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
        pions_noirs += 1
      elif case == 2:
        pions_blancs += 1

def fin_du_jeu():
  global pions_noirs, pions_blancs
  if pions_noirs < 2 or pions_blancs < 2:
    return True
  # Implémenter la détection du mat (aucun mouvement possible)
  return False

def demander_mouvement():
  origine = None
  destination = None

  while not origine or not destination:
    # Demander la case d'origine
    origine = input('Entrez la case d\'origine (lettre et numéro) : ').strip().upper()
    if not _valider_case(origine):
      print('Mouvement invalide : format incorrect.')

    # Demander la case de destination
    destination = input('Entrez la case de destination (lettre et numéro) : ').strip().upper()
    if not _valider_case(destination):
      print('Mouvement invalide : format incorrect.')

  ligne_origine = int(ord(origine[0])) - 65
  colonne_origine = _lettre_vers_colonne(origine[1])
  ligne_destination = int(ord(origine[0])) - 65
  colonne_destination = _lettre_vers_colonne(destination[1])

  return ligne_origine, colonne_origine, ligne_destination, colonne_destination


def convertir_case(ligne, colonne):
    lettre = _lettre_vers_colonne(colonne)
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
    if mouvement_valide(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
      if capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination, tour):
        effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination)
        compter_pions()
      else:
        print('Mouvement non valide : impossible de capturer une pièce de la même équipe.')
    else:
      print('Mouvement non valide : en dehors du plateau ou mouvement non orthogonal.')

    # Changer de tour
    changer_tour()

    # Afficher le plateau et l'état actuel
    afficher_plateau()
    print('Tour: ' + tour)
    print('Pions noirs: ' + str(pions_noirs))
    print('Pions blancs: ' + str(pions_blancs))

# Début du jeu
tour = 'noirs'
boucle_jeu()

# Fin du jeu
print('Fin du jeu !')

