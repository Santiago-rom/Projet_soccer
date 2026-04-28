
import math


def simuler_tir(force_impact, position_x, position_y, angle_vertical_choisi, spin):

    # Constantes
    y_but = 52.5
    x_centre_but = 0
    x_poteau1 = 3.66
    x_poteau2 = -3.66
    m_ballon = 0.430
    g = 9.81
    t_contact = 0.010
    rayon_ballon = 0.11
    dt = 0.01
    # Utilise l'angle reçu de l'interface au lieu de la valeur fixe 20
    alpha = math.radians(angle_vertical_choisi)

    # Coefficient de Magnus (S) - Ajustable pour plus ou moins d'effet
    # Valeur typique pour un ballon de foot : 0.2 a 0.5
    S = 0.025

    position_z = 0
    v0 = (force_impact * t_contact) / m_ballon

    # Correction : Utilisation de atan2(dx, dy) pour plus de précision
    angle_horizontale = math.atan2((x_centre_but - position_x), (y_but - position_y))
    angle_verticale = 20

    teta = angle_horizontale
    alpha = math.radians(angle_verticale)

    # Composantes de vitesse initiales
    vx = v0 * math.sin(teta) * math.cos(alpha)
    vy = v0 * math.cos(teta) * math.cos(alpha)
    vz = v0 * math.sin(alpha)

    x, y, z = position_x, position_y, position_z

    liste_x, liste_y, liste_z = [], [], []

    while y <= y_but and z >= 0:
        liste_x.append(x)
        liste_y.append(y)
        liste_z.append(z)

        # --- EFFET MAGNUS ---
        # L'accélération de Magnus est perpendiculaire à la vitesse horizontale
        # ax_magnus dépend de vy, ay_magnus dépend de vx
        ax_magnus = (S / m_ballon) * spin * vy
        ay_magnus = -(S / m_ballon) * spin * vx

        # Mise à jour des vitesses
        vx = vx + ax_magnus * dt
        vy = vy + ay_magnus * dt
        vz = vz - g * dt

        # Mise à jour des positions
        x = x + vx * dt
        y = y + vy * dt
        z = z + vz * dt

    # Condition pour déterminer le verdict
        # --- CALCUL DU VERDICT ---

        # On vérifie d'abord si le ballon est bien arrivé au niveau de la ligne de but
        if y >= y_but:
            # 1. Vérification de la hauteur (Z) : la barre transversale est à 2.44m
            if z <= 2.44:
                # 2. Vérification de la largeur (X) : entre les deux poteaux
                if x_poteau2 <= x <= x_poteau1:
                    # On affine pour le poteau (si le ballon touche exactement le montant)
                    if abs(x - x_poteau1) < rayon_ballon or abs(x - x_poteau2) < rayon_ballon:
                        verdict = "Poteau"
                    else:
                        verdict = "BUT"
                else:
                    verdict = "Dehors"
            else:
                # Le ballon est passé au-dessus de la barre
                verdict = "Dehors (Trop haut)"

        elif z < 0:
            # Le ballon a touché le sol avant d'atteindre la ligne de but
            verdict = "Touche le sol"
        else:
            verdict = "Dehors"

    return liste_x, liste_y, liste_z, verdict
