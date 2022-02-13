import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

def func(x):
    return x**2

a, b = 7, 9  # integral limits
x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
plt.xticks(range(11))
plt.yticks(range(0, 110, 10))

# Make the shaded region
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.set_xticks([a, b], labels=['$x$', '$x+h$'])
ax.set_yticks([func(a), func(b)], labels=['$x^2$', '$(x+h)^2$'])

plt.title('y = x^2')

plt.show()