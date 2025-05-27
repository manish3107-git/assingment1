import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.3, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w / 2, w / 2, n)
        )
        self.x, self.y, self.z = self._compute_mesh()

    def _compute_mesh(self):
        u = self.u
        v = self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def compute_surface_area(self):
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)

        xu = np.gradient(self.x, du, axis=1)
        yu = np.gradient(self.y, du, axis=1)
        zu = np.gradient(self.z, du, axis=1)

        xv = np.gradient(self.x, dv, axis=0)
        yv = np.gradient(self.y, dv, axis=0)
        zv = np.gradient(self.z, dv, axis=0)

        cross_prod = np.cross(np.stack((xu, yu, zu), axis=-1), np.stack((xv, yv, zv), axis=-1))
        area_elements = np.linalg.norm(cross_prod, axis=-1)
        surface_area = np.sum(area_elements) * du * dv
        return surface_area

    def compute_edge_length(self):
        edge1 = np.array([(self.x[0, i], self.y[0, i], self.z[0, i]) for i in range(self.n)])
        edge2 = np.array([(self.x[-1, i], self.y[-1, i], self.z[-1, i]) for i in range(self.n)])
        full_edge = np.vstack((edge1, edge2[::-1]))
        edge_diff = np.diff(full_edge, axis=0)
        return np.sum(np.linalg.norm(edge_diff, axis=1))

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, rstride=4, cstride=4, color='skyblue', edgecolor='k', alpha=0.8)
        ax.set_title('Möbius Strip')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.4, n=300)
    mobius.plot()
    print("Surface Area (approx):", mobius.compute_surface_area())
    print("Edge Length (approx):", mobius.compute_edge_length())
