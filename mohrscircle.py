import numpy as np
import matplotlib.pyplot as plt

σx = float(input("Enter σx (MPa):"))
σy = float(input("Enter σy (MPa):"))
τxy = float(input("Enter τxy (MPa):"))

def eqns(σx, σy, τxy):
    
    r = τmax = np.sqrt(((σx - σy)/2)**2 + (τxy)**2)
    σavg = ((σx + σy)/2)
    σmax = σavg + τmax
    σmin = σavg - τmax
    
    return r, σavg, σmin, σmax

r, σavg, σmin, σmax = eqns(σx, σy, τxy)

# Values adjusted by user interacting with UI (undefined var theta)
# σx_prime = σavg + ((σx - σy)/2) * np.cos(2*θ) + τxy * np.sin(2*θ)
# σy_prime = σavg - ((σx - σy)/2) * np.cos(2*θ) - τxy * np.sin(2*θ)
# τxy_prime = -((σx - σy)/2) * np.sin(2*θ) + τxy * np.cos(2*θ)

def circle(σavg, r):
    𝜙 = np.linspace(0, 2 * np.pi, 500)

    σ_prime = σavg + r * np.cos(𝜙)
    τ_prime = -r * np.sin(𝜙)

    circle_x = σ_prime
    circle_y = τ_prime
    
    return circle_x, circle_y

circle_x, circle_y = circle(σavg, r)

plt.plot(circle_x, circle_y, color = '#880808')

# angles for max stress and shear
θp = 0.5 * np.arctan2(2*τxy, (σx - σy)) 
θs = θp + np.pi/4

θp = np.degrees(θp)
θs = np.degrees(θs)

print(round(θp, 2),"\b° to get to σavg")
print(round(θs, 2), "\b° to get to τmax")

print("τmax is", round(r, 2), "MPa")
print("σavg is", round(σavg, 2), "MPa")
print("σmax", round(σmax, 2), "MPa")
print("σmin", round(σmin, 2), "MPa")

plt.title(
          label = 'Mohrs Stress Circle', 
          loc = 'center'
          )
plt.xlabel("σ (MPa)")
plt.ylabel("τ (MPa)")

x = np.array([σx, σy])
y = np.array([τxy, -τxy])
xkeypts = np.array([σavg, σmax, σmin, σavg])
ykeypts = np.array([0, 0, 0, r])

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

plt.plot(x, y, '.-', color = 'black', ms = 8)
plt.plot(xkeypts, ykeypts, '.', color = '#880808', ms = 8)

plt.show()