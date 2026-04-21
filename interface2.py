
import matplotlib.pyplot as plt

# Creer la fonction qui va afficher le résultat sous forme de graphique avec des paramétres x et y
def afficher_resultat(x ,y, verdict , force  ):

    # Trace le graphique dont le x est l'axe horizontal et le y l'axe vertical avec une ligne et des points a chaque position du ballon
    plt.plot(x ,y , color="black")
    plt.scatter(x ,y , color="green")
    x_final = x[len(x)-1]
    y_final = y[len(y)-1]
    plt.scatter(x_final, y_final , color="blue")

    # On determine le nom des axes horizontales et verticales et aussi le titre du graphique
    plt.ylabel("La distance vers le but en (m)")
    plt.xlabel("La distance latéral du ballon en (m)")
    if verdict == "BUT":
        plt.title("C'est But !!!!")
    elif verdict == "Poteau":
        plt.title("C'est Poteau !!!!")
    else:
        plt.title("Le tir n'est pas cadrer ")

    # Le ballon peut parcourir une distance entre 0 a 55 m sur l'axe verticale . Car pour qu'un tir soit considérer comme un but il doit pouvoir franchir la ligne blanche qui est de 52,5 m
    plt.ylim(0 ,55)
    # Limite horizontale du terrain
    plt.xlim(-35 ,35)

    # Ajoute une grille au graphique
    plt.grid()
    # Ajout de la legende pour differencier la trajectoire du ballon avec sa position
    plt.legend(["trajectoire du ballon" , "position du ballon "])
    # Affiche le verdict du tir et des données
    print("Le verdict du tir = " , verdict )
    print("La force du tir est de  " , force , "N")
    # Pour afficher le graphique
    plt.show()
