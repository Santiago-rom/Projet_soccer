import math
import numpy as np
#Variables constantes
x_centre_but = 0
y_but = 52.5
x_poteau1 = 3.66
x_poteau2 = -3.66
m_ballon = 0.430
g = 9.81
t_contact = 0.010
rayon_ballon = 0.11
dt = 0.01 #La simulation calcule la position et la vitesse du ballon toutes les 0,01 s
s = 0.0004
position_z = 0

#Variables à déterminer
force_impact = input("Quel est votre force d'impact sur le ballon")
if force_impact > 1500 :
   print("Votre tir est trop fort. Recommencez! Je vous suggère une force entre 1000 et 1500 N.")
elif force_impact < 1000 :
   print("Votre tir est trop faible. Recommencez! Je vous suggère une force entre 1000 et 1500 N.")
position_x = input("Choisir votre position x sur le terrain. L'axe des x correspond à la largeur du terrain et x = 0 est le centre du but!")
if 34 < position_x < -34 :
   print("Erreur! Votre position x sort du cadre du terrain. Essayez avec une valeur entre 34 et -34 ")
position_y = input("Choisir votre position y sur le terrain. L'axe des y correspond à la longueur du terrain et y = 0 est le centre du terrain!")
if 0 < position_y < 52.5 :
   print("Erreur! Votre position y sort du cadre du terrain. Essayez avec une valeur entre 0 et 52.5 ")
positions = np.array([position_x, position_y, position_z])

#Phase 1: déterminer la vitesse initiale
v0 = (force_impact*t_contact)/m_ballon

#Calcul angle verticale (Générée par Chatgpt)
import tkinter as tk
import math

angle_verticale = 0
def click(event):
    xc, yc = 200, 200  # centre du ballon
    dx = event.x - xc
    dy = yc - event.y  # inversion axe Y

    angle_verticale = math.degrees(math.atan2(dy, dx))
    print("Angle vertical :", angle_verticale)


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# dessin du ballon
canvas.create_oval(100, 100, 300, 300)

canvas.bind("<Button-1>", click)

root.mainloop()

# Calcul des composantes de vitesse
angle_horizontale = math.atan((position_x)/(position_y))
teta = math.radians(angle_horizontale)
alpha = math.radians(angle_verticale)

vx = v0 * math.sin(teta)*math.cos(alpha)
vy = v0 * math.cos(teta)*math.cos(alpha)
vz = v0 * math.sin(alpha)

# Rotation (rad/s)
effet_magnus = input("Voulez-vous un effet magnus élevé, moyen ou faible?(E/M/F)")
effet_magnus1 = effet_magnus.upper()
if effet_magnus1 =="E":
   omega_x = 50
   omega_y = 10
   omega_z = 100
elif effet_magnus1 == "M":
   omega_x = 20
   omega_y = 5
   omega_z = 60
elif effet_magnus1 == "F":
   omega_x = 10
   omega_y = 0
   omega_z = 20
else:
   print("Erreur! Veuillez recommencer en insérant une des lettres")

#Produit vectoriel
omegas = np.array([omega_x,omega_y,omega_z])
vitesses = np.array([vx,vy,vz])
prod_vecto = np.cross(omegas,vitesses)

while position_y <= y_but and position_z >= 0:
    # Effet Magnus
    a_magnus = (s / m_ballon) * prod_vecto

    # Accélération gravité
    a_gravite = np.array([0, 0, -g])

    # Accélération totale
    a_total = a_gravite + a_magnus

    # Mise à jour des vitesses
    vitesses += a_total * dt

    # Mise à jour des positions
    positions += vitesses * dt

    # Mise à jour des variables position
    position_y = positions[1]
    position_z = positions[2]