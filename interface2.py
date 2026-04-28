
import matplotlib.pyplot as plt


# Afficher le résultat sous forme de graphique
def afficher_resultat(x, y, verdict, force):
    # Création de la figure
    plt.figure(figsize=(8, 10))

    # Trace la trajectoire (ligne continue)
    plt.plot(x, y, color="black", label="Trajectoire du ballon", zorder=1)

    # Affiche les points de position (scatter)
    # On réduit la taille (s=10) pour que ce soit lisible si beaucoup de points
    plt.scatter(x, y, color="green", s=10, alpha=0.5, zorder=2)

    # Marquer le point de départ et le point final
    plt.scatter(x[0], y[0], color="red", label="Départ", zorder=3)
    plt.scatter(x[-1], y[-1], color="blue", label="Arrivée", s=50, zorder=3)

    # Noms des axes
    plt.ylabel("Distance vers le but (y) en m")
    plt.xlabel("Distance latérale (x) en m")

    # Titre dynamique selon le verdict
    titres = {
        "BUT": "C'EST BUT !!!!",
        "Poteau": "C'EST LE POTEAU !",
        "Dehors": "Le tir n'est pas cadré",
        "Touche le sol": "Le ballon a touché le sol avant le but"
    }
    plt.title(f"{titres.get(verdict, 'Résultat du tir')}\nForce : {force} N")

    # Limites du terrain (vue de dessus)
    plt.ylim(0, 55)
    plt.xlim(-35, 35)

    # Dessin des limites du but pour référence visuelle
    plt.hlines(52.5, -3.66, 3.66, colors='red', linestyles='solid', lw=3, label="Ligne de but")

    # Grille et légende
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Affichage console pour débogage
    print(f"--- Résultat ---")
    print(f"Verdict : {verdict}")
    print(f"Force : {force} N")
    print(f"Position finale : x={round(x[-1], 2)}, y={round(y[-1], 2)}")

    # Affichage du graphique
    plt.show()
