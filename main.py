# Position initiale
plateau = [[1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2]]

# Constantes
LIGNES = {0: "A", 1: "B", 2: "C", 3: "D"}
PIONS = {0: " ", 1: "●", 2: "○"}

# Variables globales
pions_noirs = 4
pions_blancs = 4
tour = 'noirs'

# Fonctions

def afficher_plateau():
  for ligne_index, ligne in enumerate(plateau):
    print(' {} | '.format(LIGNES[ligne_index]), end='')
    print(' | '.join(PIONS[case] for case in ligne), end='')
    print(' |')

def _lettre_vers_num(lettre):
  return ord(lettre.lower()) - ord('a')

def est_mouvement_valide(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  return 0 <= ligne_origine < 4 and 0 <= colonne_origine < 4 and 0 <= ligne_destination < 4 and 0 <= colonne_destination < 4

def est_mouvement_capture(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  diff_ligne = ligne_destination - ligne_origine
  diff_colonne = colonne_destination - colonne_origine
  return abs(diff_ligne) == 2 and abs(diff_colonne) == 0 or abs(diff_ligne) == 0 and abs(diff_colonne) == 2 and plateau[ligne_destination][colonne_destination] != 0

def capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  ligne_intermediaire = (ligne_origine + ligne_destination) // 2
  colonne_intermediaire = (colonne_origine + colonne_destination) // 2
  return (abs(ligne_origine - ligne_destination) == 2 or abs(colonne_origine - colonne_destination) == 2) and plateau[ligne_intermediaire][colonne_intermediaire] == plateau[ligne_origine][colonne_origine] and plateau[ligne_destination][colonne_destination] != 0 and plateau[ligne_destination][colonne_destination] != plateau[ligne_origine][colonne_origine]

def effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
  plateau[ligne_destination][colonne_destination] = plateau[ligne_origine][colonne_origine]
  plateau[ligne_origine][colonne_origine] = 0

def changer_tour():
  global tour
  tour = 'noirs' if tour == 'blancs' else 'blancs'

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
  return pions_noirs < 2 or pions_blancs < 2

def demander_mouvement():
  origine = None
  destination = None
  while not origine or not destination:
    print("tour:", tour)
    origine = input('Entrez la case d\'origine (lettre et numéro) : ').strip().upper()
    if not _valider_case(origine):
      print('Mouvement invalide : format incorrect.')
    destination = input('Entrez la case de destination (lettre et numéro) : ').strip().upper()
    if not _valider_case(destination):
      print('Mouvement invalide : format incorrect.')
  ligne_origine = _lettre_vers_num(origine[0])
  colonne_origine = int(origine[1]) - 1
  ligne_destination = _lettre_vers_num(destination[0])
  colonne_destination = int(destination[1]) - 1
  return ligne_origine, colonne_origine, ligne_destination, colonne_destination

def _valider_case(case):
  return len(case) == 2 and case[0].isalpha() and case[1].isdigit()

# Début du jeu
afficher_plateau()

def boucle_jeu():
  while not fin_du_jeu():
    ligne_origine, colonne_origine, ligne_destination, colonne_destination = demander_mouvement()
    if est_mouvement_valide(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
      if est_mouvement_capture(ligne_origine, colonne_origine, ligne_destination, colonne_destination):
        if capturer_pion(plateau, ligne_origine, colonne_origine, ligne_destination, colonne_destination):
          effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination)
          compter_pions()
      else:
        effectuer_mouvement(ligne_origine, colonne_origine, ligne_destination, colonne_destination)
    else:
      print('Mouvement non valide.')

    changer_tour()

    afficher_plateau()
    print('Tour: ' + tour)
    print('Pions noirs: ' + str(pions_noirs))
    print('Pions blancs: ' + str(pions_blancs))

boucle_jeu()
