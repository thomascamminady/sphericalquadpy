"""Octalerp quadrature."""
from numpy import pi, inf, zeros, sqrt, cos, sin, array
from numpy.linalg import norm
from sphericalquadpy.quadrature.quadrature import Quadrature
from sphericalquadpy.tools.geometryhelper import lerp, eightfold


class Octalerp(Quadrature):
    """Octalerp Quadrature"""

    def name(self):
        return "Octalerp Quadrature"

    def getmaximalorder(self):
        return inf

    def computequadpoints(self, order):
        """Quadrature points for Octalerp quadrature."""
        n = order
        pt0 = array([0.0, 0.0, 1.0])
        pt1 = array([0.0, 1.0, 0.0])
        pt2 = array([1.0, 0.0, 0.0])

        pts01 = lerp(pt0, pt1, n)
        pts02 = lerp(pt0, pt2, n)
        nptsoctant = (n * (n + 1)) // 2
        pts = zeros((3, nptsoctant))

        counter = 0
        for i in range(n):

            tmp = lerp(pts01[:, i].T, pts02[:, i].T, i + 1)
            for j in range(tmp.shape[1]):
                pts[:, counter] = tmp[:, j]
                counter += 1

        # project onto sphere
        for i in range(nptsoctant):
            pts[:, i] /= norm(pts[:, i])

        # We now want to get the connectivity. Therefore enumerate all
        # the points (overkill from a computational point of view) and then
        # write the correct connectivity.
        # Matrix that assigns an ID to the points
        ids = zeros((n, n), dtype=int)  # Too large, but not important.

        # Matrix that will later contain all triangles
        nTrianglesOctant = n * n - 2 * n + 1
        triangles = zeros((3, nTrianglesOctant), dtype=int)
        counter = 0
        for i in range(n):
            for j in range(n):
                ids[i, j] = counter
                counter += 1

        # now create triangles
        counter = 0
        for i in range(n):
            for j in range(i - 1):
                tmp = array([ids[i, j], ids[i, j + 1], ids[i - 1, j]])
                triangles[:, counter] = tmp
                counter += 1
            if i < n - 1:
                for j in range(i - 1):
                    tmp = array([ids[i, j], ids[i, j + 1], ids[i + 1, j + 1]])
                    triangles[:, counter] = tmp
                    counter += 1

        allpts = eightfold(pts)

        return allpts.T

    def computequadweights(self, order):
        """Quadrature weights for Octalerp quadrature."""
        w = 1
        # w /= sum(w)
        # w *= 4 * pi
        return w

    def nqbyorder(self, order):
        """Scales in the following way"""
        nq = order ** 2
        return order, nq
