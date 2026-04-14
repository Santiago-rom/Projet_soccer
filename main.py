from interface1 import force_impact, position_x, position_y
from calculs import simuler_tir
from interface2 import afficher_resultat

# lancer les calculs
liste_x, liste_y, liste_z, verdict = simuler_tir(force_impact, position_x, position_y)

# afficher vue du dessus (X-Y)
afficher_resultat(liste_x, liste_y, verdict, force_impact)
