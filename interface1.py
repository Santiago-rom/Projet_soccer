import math
import tkinter as tk
from tkinter import messagebox
from interface2 import afficher_resultat

# variables connues
x_centre_but = 0
y_but = 52.5
x_poteau1 = 3.66
x_poteau2 = -3.66
h_ballon = 0.430
g = 9.81
t_contact = 0.010
rayon_ballon = 0.11

# variables à déterminer
force_impact = 0
angle_verticale = 0
position_x = 0
position_y = 0
position_z = 0
effet_magnus1 = ""

# dimensions du terrain pour le canvas
largeur_terrain = 68
longueur_terrain = 52.5

# dimensions du canvas terrain
canvas_largeur = 700
canvas_hauteur = 450


# clic sur le terrain
def clic_terrain(event):
    global position_x, position_y, position_z

    # conversion du canvas vers les coordonnées du terrain
    position_x = (event.x / canvas_largeur) * largeur_terrain - 34
    position_y = ((canvas_hauteur - event.y) / canvas_hauteur) * longueur_terrain
    position_z = 0

    if position_x < -34 or position_x > 34:
        messagebox.showerror(
            "Erreur",
            "Votre position x sort du cadre du terrain. Essayez avec une valeur entre -34 et 34."
        )
        return

    if position_y < 0 or position_y > 52.5:
        messagebox.showerror(
            "Erreur",
            "Votre position y sort du cadre du terrain. Essayez avec une valeur entre 0 et 52.5."
        )
        return

    # effacer ancien ballon
    canvas_terrain.delete("ballon_position")

    # dessiner le ballon
    canvas_terrain.create_oval(
        event.x - 8, event.y - 8, event.x + 8, event.y + 8,
        fill="white", outline="black", tags="ballon_position"
    )

    texte_position.config(
        text="Position choisie : x = " + str(round(position_x, 2)) + " m   y = " + str(round(position_y, 2)) + " m"
    )


# clic sur le ballon pour angle vertical
def clic_ballon(event):
    global angle_verticale, spin_choisi

    xc = 100
    yc = 100

    # 1. NETTOYAGE : Supprime l'ancien point rouge s'il existe
    canvas_ballon.delete("point_impact")

    # 2. CALCULS
    dx = event.x - xc
    dy = yc - event.y

    # Angle vertical (on garde abs(dx) pour que l'angle soit cohérent même sur les bords)
    angle_verticale = math.degrees(math.atan2(dy, abs(dx)))

    # Spin latéral (Gauche/Droite)
    spin_choisi = -(event.x - xc) / 10

    # 3. DESSIN : On ajoute le tag "point_impact" pour qu'il soit supprimable au prochain clic
    canvas_ballon.create_oval(
        event.x - 4, event.y - 4,
        event.x + 4, event.y + 4,
        fill="red",
        outline="black",
        tags="point_impact"  # <--- C'EST CETTE LIGNE QUI MANQUAIT
    )

    texte_angle.config(text=f"Angle: {round(angle_verticale, 2)}° | Spin: {round(spin_choisi, 2)}")
# bouton valider
def valider_donnees():
    global force_impact, angle_verticale, position_x, position_y,spin_choisi

    try:
        force_impact = float(entree_force.get())
    except:
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique pour la force.")
        return

    from calculs import simuler_tir
    liste_x, liste_y, liste_z, verdict = simuler_tir(
        force_impact,
        position_x,
        position_y,
        angle_verticale,
        spin_choisi,

    )
    # On envoie le spin positif ou négatif ici

    if position_x == 0 and position_y == 0:
        messagebox.showerror("Erreur", "Choisir votre position sur le terrain.")
        return

    if angle_verticale == 0:
        messagebox.showerror("Erreur", "Cliquez sur le ballon pour choisir l'angle vertical.")
        return

    # Affichage des valeurs dans la zone de texte
    zone_resultat.delete("1.0", tk.END)
    zone_resultat.insert(tk.END, "=== VARIABLES D'ENTRÉE ===\n\n")
    zone_resultat.insert(tk.END, f"Force: {force_impact} N\n")
    zone_resultat.insert(tk.END, f"Angle Vert: {round(angle_verticale, 2)}°\n")
    zone_resultat.insert(tk.END, f"Effet: {variable_effet.get()} (Spin: {spin_choisi})\n")

    # --- CORRECTION DE L'APPEL ---
    from calculs import simuler_tir
    # On envoie maintenant l'angle_verticale et le spin_value
    # Note : assure-toi que ta fonction simuler_tir accepte ces arguments
    liste_x, liste_y, liste_z, verdict = simuler_tir(
        force_impact,
        position_x,
        position_y,
        angle_verticale,
        spin_choisi,
    )

    afficher_resultat(liste_x, liste_y, verdict, force_impact)

# fenêtre principale
root = tk.Tk()
root.title("Interface 1 - Projet soccer")
root.geometry("1200x650")
root.config(bg="#1f1f1f")

# partie gauche
frame_gauche = tk.Frame(root, bg="#1f1f1f")
frame_gauche.pack(side="left", padx=20, pady=20)

titre_terrain = tk.Label(
    frame_gauche,
    text="Terrain de soccer (vue du haut)",
    font=("Arial", 16, "bold"),
    bg="#1f1f1f",
    fg="white"
)
titre_terrain.pack(pady=10)

canvas_terrain = tk.Canvas(
    frame_gauche,
    width=canvas_largeur,
    height=canvas_hauteur,
    bg="#2e8b57",
    highlightthickness=0
)
canvas_terrain.pack()

# dessin du demi-terrain

# contour du demi-terrain
canvas_terrain.create_rectangle(20, 20, 680, 430, outline="white", width=3)

# ligne du haut (ligne de but)
canvas_terrain.create_line(20, 20, 680, 20, fill="white", width=3)

# surface de réparation
canvas_terrain.create_rectangle(200, 20, 500, 140, outline="white", width=2)

# petite surface
canvas_terrain.create_rectangle(270, 20, 430, 80, outline="white", width=2)

# point de penalty
canvas_terrain.create_oval(345, 100, 355, 110, fill="white", outline="white")

# arc de cercle du penalty
canvas_terrain.create_arc(290, 80, 410, 200, start=180, extent=180, outline="white", width=2)

# but
canvas_terrain.create_rectangle(310, 5, 390, 20, outline="yellow", width=3)

# cliquer sur le terrain
canvas_terrain.bind("<Button-1>", clic_terrain)

texte_position = tk.Label(
    frame_gauche,
    text="Position choisie : aucune",
    font=("Arial", 12),
    bg="#1f1f1f",
    fg="white"
)
texte_position.pack(pady=10)

# partie droite
frame_droite = tk.Frame(root, bg="#2a2a2a", width=350)
frame_droite.pack(side="right", fill="y", padx=20, pady=20)
frame_droite.pack_propagate(False)

titre_donnees = tk.Label(
    frame_droite,
    text="Données du tir",
    font=("Arial", 16, "bold"),
    bg="#2a2a2a",
    fg="white"
)
titre_donnees.pack(pady=20)

# force
texte_force = tk.Label(
    frame_droite,
    text="Force d'impact sur le ballon",
    font=("Arial", 11),
    bg="#2a2a2a",
    fg="white"
)
texte_force.pack(anchor="w", padx=20)

entree_force = tk.Entry(frame_droite, font=("Arial", 12))
entree_force.pack(fill="x", padx=20, pady=8)
entree_force.insert(0, "1200")

# effet magnus
texte_effet = tk.Label(
    frame_droite,
    text="Effet magnus : E, M ou F",
    font=("Arial", 11),
    bg="#2a2a2a",
    fg="white"
)
texte_effet.pack(anchor="w", padx=20, pady=(10, 0))

variable_effet = tk.StringVar()
variable_effet.set("M")

menu_effet = tk.OptionMenu(frame_droite, variable_effet, "E", "M", "F")
menu_effet.config(font=("Arial", 11), width=10)
menu_effet.pack(anchor="w", padx=20, pady=8)

# ballon pour angle vertical
texte_ballon = tk.Label(
    frame_droite,
    text="Cliquez sur le ballon pour l'angle vertical",
    font=("Arial", 11),
    bg="#2a2a2a",
    fg="white"
)
texte_ballon.pack(pady=(15, 8))

canvas_ballon = tk.Canvas(
    frame_droite,
    width=200,
    height=200,
    bg="#2a2a2a",
    highlightthickness=0
)
canvas_ballon.pack()

canvas_ballon.create_oval(20, 20, 180, 180, fill="white", outline="black", width=3)
canvas_ballon.bind("<Button-1>", clic_ballon)

texte_angle = tk.Label(
    frame_droite,
    text="Angle vertical choisi : aucun",
    font=("Arial", 11),
    bg="#2a2a2a",
    fg="white"
)
texte_angle.pack(pady=10)

# bouton
bouton_valider = tk.Button(
    frame_droite,
    text="Valider les données",
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    command=valider_donnees
)
bouton_valider.pack(fill="x", padx=20, pady=15)

# zone résultat
zone_resultat = tk.Text(
    frame_droite,
    width=35,
    height=8,
    font=("Consolas", 10),
    bg="#1f1f1f",
    fg="white",
    insertbackground="white"
)
zone_resultat.pack(padx=20, pady=10)

root.mainloop()
