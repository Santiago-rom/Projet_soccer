import math

import tkinter as tk

from tkinter import messagebox

# variables connues

x_centre_but = 0

y_but = 52.5

x_poteau1 = 3.66

x_poteau2 = -3.66

h_ballon = 0.430

g = 9.81

t_contact = 0.010

rayon_ballon = 0.11

# variables √† d√©terminer

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

    # conversion du canvas vers les coordonn√©es du terrain (chatgpt)

    position_x = (event.x / canvas_largeur) * largeur_terrain - 34

    position_y = ((canvas_hauteur - event.y) / canvas_hauteur) * longueur_terrain

    position_z = 0

    if position_x < -34 or position_x > 34:
        messagebox.showerror("Erreur",
                             "Votre position x sort du cadre du terrain. Essayez avec une valeur entre -34 et 34.")

        return

    if position_y < 0 or position_y > 52.5:
        messagebox.showerror("Erreur",
                             "Votre position y sort du cadre du terrain. Essayez avec une valeur entre 0 et 52.5.")

        return

        # effacer ancien ballon

    canvas_terrain.delete("ballon_position")

    # dessiner le ballon

    canvas_terrain.create_oval(event.x - 8, event.y - 8, event.x + 8, event.y + 8,

                               fill="white", outline="black", tags="ballon_position")

    texte_position.config(

        text="Position choisie : x = " + str(round(position_x, 2)) + " m   y = " + str(round(position_y, 2)) + " m"

    )


# clic sur le ballon pour angle vertical

def clic_ballon(event):
    global angle_verticale

    xc = 100

    yc = 100

    dx = event.x - xc

    dy = yc - event.y

    angle_verticale = math.degrees(math.atan2(dy, dx))

    canvas_ballon.delete("point_impact")

    canvas_ballon.create_oval(event.x - 4, event.y - 4, event.x + 4, event.y + 4,

                              fill="red", outline="black", tags="point_impact")

    texte_angle.config(

        text="Angle vertical choisi : " + str(round(angle_verticale, 2)) + "¬∞"

    )


# bouton valider

def valider_donnees():
    global force_impact, effet_magnus1

    try:

        force_impact = float(entree_force.get())

    except:

        messagebox.showerror("Erreur", "Veuillez entrer une valeur num√©rique pour la force.")

        return

    if force_impact > 1500:
        messagebox.showerror("Erreur",
                             "Votre tir est trop fort. Recommencez. Je vous sugg√®re une force entre 1000 et 1500 N.")

        return

    if force_impact < 1000:
        messagebox.showerror("Erreur",
                             "Votre tir est trop faible. Recommencez. Je vous sugg√®re une force entre 1000 et 1500 N.")

        return

    effet_magnus1 = variable_effet.get()

    if effet_magnus1 != "E" and effet_magnus1 != "M" and effet_magnus1 != "F":
        messagebox.showerror("Erreur", "Veuillez choisir un effet magnus valide.")

        return

    if position_x == 0 and position_y == 0:
        messagebox.showerror("Erreur", "Choisir votre position sur le terrain.")

        return

    if angle_verticale == 0:
        messagebox.showerror("Erreur", "Cliquez sur le ballon pour choisir l'angle vertical.")

        return

        # affichage des valeurs (chatgpt)

    zone_resultat.delete("1.0", tk.END)

    zone_resultat.insert(tk.END, "Variables d'entr√©e pour les calculs\n\n")

    zone_resultat.insert(tk.END, "force_impact = " + str(force_impact) + "\n")

    zone_resultat.insert(tk.END, "position_x = " + str(position_x) + "\n")

    zone_resultat.insert(tk.END, "position_y = " + str(position_y) + "\n")

    zone_resultat.insert(tk.END, "position_z = " + str(position_z) + "\n")

    zone_resultat.insert(tk.END, "angle_verticale = " + str(angle_verticale) + "\n")

    zone_resultat.insert(tk.END, "effet_magnus1 = '" + str(effet_magnus1) + "'\n")

    print("force_impact =", force_impact)

    print("position_x =", position_x)

    print("position_y =", position_y)

    print("position_z =", position_z)

    print("angle_verticale =", angle_verticale)

    print("effet_magnus1 =", effet_magnus1)


# fen√™tre principale

root = tk.Tk()

root.title("Interface 1 - Projet soccer")

root.geometry("1200x650")

root.config(bg="#1f1f1f")

# partie gauche

frame_gauche = tk.Frame(root, bg="#1f1f1f")

frame_gauche.pack(side="left", padx=20, pady=20)

titre_terrain = tk.Label(frame_gauche, text="Terrain de soccer (vue du haut)",

                         font=("Arial", 16, "bold"), bg="#1f1f1f", fg="white")

titre_terrain.pack(pady=10)

canvas_terrain = tk.Canvas(frame_gauche, width=canvas_largeur, height=canvas_hauteur,

                           bg="#2e8b57", highlightthickness=0)

canvas_terrain.pack()

# dessin du terrain

canvas_terrain.create_rectangle(20, 20, 680, 430, outline="white", width=3)

canvas_terrain.create_line(350, 20, 350, 430, fill="white", width=2)

canvas_terrain.create_oval(290, 165, 410, 285, outline="white", width=2)

canvas_terrain.create_oval(345, 220, 355, 230, fill="white", outline="white")

# but en haut

canvas_terrain.create_rectangle(310, 10, 390, 20, outline="yellow", width=3)

canvas_terrain.bind("<Button-1>", clic_terrain)

texte_position = tk.Label(frame_gauche, text="Position choisie : aucune",

                          font=("Arial", 12), bg="#1f1f1f", fg="white")

texte_position.pack(pady=10)

# partie droite

frame_droite = tk.Frame(root, bg="#2a2a2a", width=350)

frame_droite.pack(side="right", fill="y", padx=20, pady=20)

frame_droite.pack_propagate(False)

titre_donnees = tk.Label(frame_droite, text="Donn√©es du tir",

                         font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white")

titre_donnees.pack(pady=20)

# force

texte_force = tk.Label(frame_droite, text="Force d'impact sur le ballon",

                       font=("Arial", 11), bg="#2a2a2a", fg="white")

texte_force.pack(anchor="w", padx=20)

entree_force = tk.Entry(frame_droite, font=("Arial", 12))

entree_force.pack(fill="x", padx=20, pady=8)

entree_force.insert(0, "1200")

# effet magnus

texte_effet = tk.Label(frame_droite, text="Effet magnus : E, M ou F",

                       font=("Arial", 11), bg="#2a2a2a", fg="white")

texte_effet.pack(anchor="w", padx=20, pady=(10, 0))

variable_effet = tk.StringVar()

variable_effet.set("M")

menu_effet = tk.OptionMenu(frame_droite, variable_effet, "E", "M", "F")

menu_effet.config(font=("Arial", 11), width=10)

menu_effet.pack(anchor="w", padx=20, pady=8)

# ballon pour angle vertical

texte_ballon = tk.Label(frame_droite, text="Cliquez sur le ballon pour l'angle vertical",

                        font=("Arial", 11), bg="#2a2a2a", fg="white")

texte_ballon.pack(pady=(15, 8))

canvas_ballon = tk.Canvas(frame_droite, width=200, height=200,

                          bg="#2a2a2a", highlightthickness=0)

canvas_ballon.pack()

canvas_ballon.create_oval(20, 20, 180, 180, fill="white", outline="black", width=3)

canvas_ballon.bind("<Button-1>", clic_ballon)

texte_angle = tk.Label(frame_droite, text="Angle vertical choisi : aucun",

                       font=("Arial", 11), bg="#2a2a2a", fg="white")

texte_angle.pack(pady=10)

# bouton

bouton_valider = tk.Button(frame_droite, text="Valider les donn√©es",

                           font=("Arial", 13, "bold"), bg="#4CAF50", fg="white",

                           command=valider_donnees)

bouton_valider.pack(fill="x", padx=20, pady=15)

# zone r√©sultat

zone_resultat = tk.Text(frame_droite, width=35, height=12, font=("Consolas", 10))

zone_resultat.pack(padx=20, pady=10)

root.mainloop()