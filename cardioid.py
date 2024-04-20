import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Parse the equation and create a function
equation = "sin(t)*sqrt(abs(cos(t)))/(sin(t)+7/5)-2*sin(t)+2"
expr = sp.sympify(equation)
func = sp.lambdify("t", expr, modules="numpy")

# Generate the x and y values
theta = np.linspace(0.5 * np.pi, 2.5 * np.pi, 1000)
radius = func(theta)

# Plot the graph
fig, ax = plt.subplots(subplot_kw=dict(polar=True))

color = "#e3256b"
for scale in np.linspace(1, 4, num=4):
    ax.plot(theta, radius * scale, color=color, alpha=0.0)
    ax.fill_between(theta, 0, radius * scale, color=color, alpha=0.15)

# Customize the graph
plt.axis("off")
ax.grid(False)
plt.savefig("cardioid.png", dpi=300, bbox_inches="tight", pad_inches=0)
plt.show()
