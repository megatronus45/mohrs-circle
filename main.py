import numpy as np
import matplotlib.pyplot as plt


 #   s_x = float(input("Enter σx (MPa):"))
  #  s_y = float(input("Enter σy (MPa):"))
   # t_xy = float(input("Enter τxy (MPa):"))


def eqns(s_x, s_y, t_xy):
    
    r = t_max = np.sqrt(((s_x - s_y)/2)**2 + (t_xy)**2)
    s_avg = ((s_x + s_y)/2)
    s_max = s_avg + t_max
    s_min = s_avg - t_max

    return r, s_avg, s_min, s_max

def circle(s_avg, r):
    phi = np.linspace(0, 2 * np.pi, 500)

    s_prime = s_avg + r * np.cos(phi)
    t_prime = -r * np.sin(phi)

    circle_x = s_prime
    circle_y = t_prime

    return circle_x, circle_y

def angles(t_xy, s_x, s_y):
    theta_p = 0.5 * np.arctan2(2*t_xy, (s_x - s_y)) 
    theta_s = theta_p + np.pi/4

    theta_p = np.degrees(theta_p)
    theta_s = np.degrees(theta_s)

    return theta_p, theta_s

def o_plot(x, y, xkeypts, ykeypts, circle_x, circle_y, r, s_avg, s_max, s_min, s_x, s_y, t_xy):

    x = np.array([s_x, s_y])
    y = np.array([t_xy, -t_xy])
    xkeypts = np.array([s_avg, s_max, s_min, s_avg])
    ykeypts = np.array([0, 0, 0, r])

    plt.title(
            label = 'Mohrs Stress Circle', 
            loc = 'center'
            )
    plt.xlabel("σ (MPa)")
    plt.ylabel("τ (MPa)")
    plt.axis('equal')

    plt.axvline(
                x = 0, 
                color = 'black', 
                linestyle = '-', 
                linewidth = 1.5
                )

    plt.axhline(
                y = 0, 
                color = 'black',
                linestyle = '-',
                linewidth = 1.5
                )

    plt.xlabel("σ (MPa)")
    plt.ylabel("τ (MPa)")

    plt.plot(circle_x, circle_y, color = '#880808')

    plt.plot(x, y, '.-', color = 'black', ms = 8)
    plt.plot(xkeypts, ykeypts, '.', color = '#880808', ms = 8)


