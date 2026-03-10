# Adam Daki
import math

def simuler_tir(force_impact,position_x,position_y):
    # Constantes de mon coequipier Santiago
    y_but = 52.5
    x_centre_but = 0
    x_poteau1 = 3.66
    x_poteau2 = -3.66
    m_ballon = 0.430
    g = 9.81
    t_contact = 0.010
    rayon_ballon = 0.11
    dt= 0.01
    #La ballon va commncer au sol. C'est pour cette raison qu'on a défini la position de la hauteur a 0
    position_z = 0
    #Determiner la vitesse initiale
    v0 = (force_impact * t_contact)/ m_ballon
    #Angle horizontale vers le centre
    angle_horizontale = math.atan((x_centre_but - position_x)/ (y_but - position_y))
    # Angle verticale
    angle_verticale = 20

    teta = angle_horizontale
    alpha = math.radians(angle_verticale)


    #Composantes de vitesse

    vx = v0 * math.sin(teta) * math.cos(alpha)
    vy = v0 * math.cos(teta) * math.cos(alpha)
    vz = v0 * math.sin(alpha)

    #Poisition initiale que l'utilisateur va choisir
    x = position_x
    y = position_y
    z = position_z

    # Liste pour conserver les donner de la  trajectoire

    liste_x = []
    liste_y = []
    liste_z = []


    # boucle qui demontre que la simulatio continue tant que le ballon na pas depasser le but ou toucher le sol
    while y <= y_but and z >= 0:
        liste_x.append(x)
        liste_y.append(y)
        liste_z.append(z)
        # Gravité
        vz = vz - g * dt
        # Mise a jour des positions
        x = x + vx * dt
        y = y + vy * dt
        z = z + vz * dt
    # Condition pour determiner le verdict
    if x_poteau2 <= x <= x_poteau1 and z <= 2.44:
        verdict = "BUT"
    elif abs(x - x_poteau1) < rayon_ballon or abs(x-x_poteau2) < rayon_ballon:
        verdict = "Poteau"
    else:
        verdict = "Dehors"
    return liste_x, liste_y, liste_z, verdict
