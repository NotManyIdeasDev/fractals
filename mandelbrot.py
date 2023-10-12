import matplotlib.pyplot as plt
import numpy as np

# Piano complesso di grandezza |xmax-xmin|, |ymax-ymin|, di densita' pixel_density.
# la funzione linspace distribuisce i valori linearmente.
def complex_plane(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int(xmax - xmin) * pixel_density)
    im = np.linspace(ymin, ymax, int(ymax - ymin) * pixel_density)
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

# Controlla se il numero esce fuori dal raggio di Mandelbrot dopo num_iterations iterazioni (operato su tutta la matrice c_plane)
def is_stable(c_plane, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c_plane
    return abs(z) <= 2

# Seleziona solamente i punti del piano stabili (filtra l'array c_plane con la mask costruita tramite is_stable)
def get_stables(c_plane, num_iterations):
    mask = is_stable(c_plane, num_iterations)
    return c_plane[mask]

c = complex_plane(-1.75, 0.75, -1.25, 1.25, 2048)

plt.imshow(is_stable(c, num_iterations=30), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
