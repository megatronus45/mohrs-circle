import numpy as np
import matplotlib.pyplot as plt

def eqns(s_x, s_y, t_xy):
    
    r = t_max = np.sqrt(((s_x - s_y)/2)**2 + (t_xy)**2)
    s_avg = ((s_x + s_y)/2)
    s_max = s_avg + t_max
    s_min = s_avg - t_max

    return r, s_avg, s_min, s_max, s_x, s_y, t_xy
    
def slider(r, s_avg, theta_slider, s_x, s_y, t_xy):

    phi = np.linspace(0, 2*np.pi, 500)

    theta_p = 0.5 * np.arctan2(2 * t_xy, s_x - s_y)
    mohr_angle = 2 * (theta_slider + theta_p)

    sx_prime = s_avg + ((s_x - s_y)/2) * np.cos(mohr_angle) + t_xy * np.sin(mohr_angle)
    sy_prime = s_avg - ((s_x - s_y)/2) * np.cos(mohr_angle) - t_xy * np.sin(mohr_angle)
    t_prime = -((s_x - s_y)/2) * np.sin(mohr_angle) + t_xy * np.cos(mohr_angle)

    circle_x = s_avg + r * np.cos(phi)
    circle_y = r * np.sin(phi)

    return circle_x, circle_y, sx_prime, sy_prime, t_prime, theta_slider

def o_plot(r, s_avg, s_max, s_min, s_x, s_y, t_xy, circle_x, circle_y, sx_prime, sy_prime, t_prime):

    x = np.array([s_x, s_y])
    y = np.array([t_xy, -t_xy])
    xkeypts = np.array([s_avg, s_max, s_min, s_avg])
    ykeypts = np.array([0, 0, 0, r])

    s_primept = np.array([sx_prime, sy_prime])
    t_primept = np.array([t_prime, -t_prime])



    fig, ax = plt.subplots()

    plt.title(
            label = 'Mohrs Stress Circle', 
            loc = 'center'
            )
   
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

    plt.xlabel("σ (Normal stress)")
    plt.ylabel("τ (Shear stress)")

    plt.plot(circle_x, circle_y, color = '#880808')
    plt.plot(x, y, '.-', color = 'black', ms = 8)
    plt.plot(s_primept, t_primept, '.-', color = "#002F57", ms = 8)
    plt.plot(xkeypts, ykeypts, '.', color = '#880808', ms = 8)

    return fig
