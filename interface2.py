import matplotlib.pyplot as plt


def afficher_resultat(x, y, verdict, force):
    plt.figure(figsize=(8, 10))

    plt.plot(x, y, color="black", label="Trajectoire du ballon", zorder=1)
    plt.scatter(x, y, color="green", s=10, alpha=0.5, zorder=2)

    plt.scatter(x[0], y[0], color="red", label="Départ", zorder=3)
    plt.scatter(x[-1], y[-1], color="blue", label="Arrivée", s=50, zorder=3)

    plt.ylabel("Distance vers le but (y) en m")
    plt.xlabel("Distance latérale (x) en m")

    titres = {
        "BUT": "C'EST BUT !!!!",
        "Poteau": "C'EST LE POTEAU !",
        "Dehors": "Le tir n'est pas cadré",
        "Dehors (Trop haut)": "Le ballon passe au-dessus du but",
        "Touche le sol": "Le ballon a touché le sol avant le but"
    }

    plt.title(f"{titres.get(verdict, 'Résultat du tir')}\nForce : {force} N")

    plt.ylim(0, 55)
    plt.xlim(-35, 35)

    plt.hlines(52.5, -3.66, 3.66, colors="red", lw=3, label="Ligne de but")

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()

    print("--- Résultat ---")
    print(f"Verdict : {verdict}")
    print(f"Force : {force} N")
    print(f"Position finale : x={round(x[-1], 2)}, y={round(y[-1], 2)}")

    plt.show()
