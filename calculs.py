
import math

def simuler_tir(force_impact, position_x, position_y):

    y_but = 52.5
    x_centre_but = 0
    x_poteau1 = 3.66
    x_poteau2 = -3.66

    m_ballon = 0.430
    g = 9.81
    t_contact = 0.010
    dt = 0.01
    rayon_ballon = 0.11

    position_z = 0

    # vitesse initiale
    v0 = (force_impact * t_contact) / m_ballon

    # angles
    angle_horizontale = math.atan2(
        x_centre_but - position_x,
        y_but - position_y
    )

    angle_verticale = math.radians(20)

    # vitesses
    vx = v0 * math.sin(angle_horizontale) * math.cos(angle_verticale)
    vy = v0 * math.cos(angle_horizontale) * math.cos(angle_verticale)
    vz = v0 * math.sin(angle_verticale)

    x, y, z = position_x, position_y, position_z

    liste_x = []
    liste_y = []
    liste_z = []

    # boucle stable
    while z >= 0:

        liste_x.append(x)
        liste_y.append(y)
        liste_z.append(z)

        vz -= g * dt

        x += vx * dt
        y += vy * dt
        z += vz * dt

    # verdict
    if x_poteau2 <= x <= x_poteau1 and z <= 2.44:
        verdict = "BUT"
    elif abs(x - x_poteau1) < rayon_ballon or abs(x - x_poteau2) < rayon_ballon:
        verdict = "POTEAU"
    else:
        verdict = "DEHORS"

    return liste_x, liste_y, liste_z, verdict

