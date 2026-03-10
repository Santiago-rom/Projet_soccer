
import matplotlib.pyplot as plt



#Creer la fonction qui va afficher le résultat sous forme de graphique avec des paramétres y et z
def afficher_resultat(y,z , verdict , force  ):

#Trace le graphique dont le y est l'axe horizontal et le z l'axe vertical avec une ligne et des points a chaque position du ballon
    plt.plot(y, z , color="black")
    plt.scatter(y,z , color="green")

# On determine le nom des axes horizontales et verticales et aussi le titre du graphique
    plt.xlabel("La distance vers le but en (m)")
    plt.ylabel("La hauteur du ballon en (m)")
    plt.title("La trajectoire du tir ")

#Le ballon peut parcourir une distance entre 0 a 60 m sur l'axe horizontale . Car pour qu'un tir soit considérer comme un but il doit pouvoir franchir la ligne blanche qui est de 52,5 m
    plt.xlim(0,60)
#La ballon ne peut pas depasser 3 m de hauteur
    plt.ylim(0,3)
#Ajoute une grille au graphique
    plt.grid()
#Ajout de la legende pour differencier la trajectoire du ballon avec sa position
    plt.legend(["trajectoire du ballon" , "position du ballon "])
#Affiche le verdict du tir et des données
    print("Le verdict du tir = " , verdict )
    print("La force du tir est de  " , force , "N")
#Pour afficher le graphique
    plt.show()

