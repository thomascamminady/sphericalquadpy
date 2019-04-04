"""Monte Carlo Quadrature uses random quadrature points and equal
weights to integrate a function."""
from numpy import pi, loadtxt
from sphericalquadpy.quadrature.quadrature import Quadrature
from sphericalquadpy.tools.findnearest import find_nearest
from sphericalquadpy.lebedevdicitionary import lebedevdictionary

AVAILABLEORDERS = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 35,
                   41, 47, 53, 59, 65, 71, 77]#, 83, 89, 95, 101, 107, 113, 119,
                   #125, 131]

NUMBERQUADPOINTS = [6, 14, 26, 38, 50, 74, 86, 110, 146, 170, 194,
                    230, 266, 302, 350, 434, 590, 770, 974, 1202, 1454, 1730,
                    2030, 2354, 2702, 3074, 3470, 3890, 4334, 4802, 5294, 5810]


# NUMBERQUADPOINTS = zeros(len(AVAILABLEORDERS), dtype=int)
# for i, order in enumerate(AVAILABLEORDERS):
#    tmp = loadtxt("data/"+str(order) + "_lebedev.txt", delimiter=",")
#    NUMBERQUADPOINTS[i] = tmp.shape[0]


class Lebedev(Quadrature):
    """Lebedev Quadrature"""

    def computequadpoints(self, order):
        """Quadrature points for Lebedev quadrature. Read from file."""
        if order not in AVAILABLEORDERS:
            neighbor = find_nearest(AVAILABLEORDERS, order)
            raise ValueError("Order not available. Next closest would be"
                             "%i.", AVAILABLEORDERS[neighbor])

        d = lebedevdictionary()
        xyzw = d[order]
        return xyzw[:, 0:2]

    def computequadweights(self, order):
        """Quadrature weights for Lebedev quadrature. Read from file."""
        if order not in AVAILABLEORDERS:
            neighbor = find_nearest(AVAILABLEORDERS, order)
            raise ValueError("Order not available. Next closest would be"
                             "%i.", AVAILABLEORDERS[neighbor])

        d = lebedevdictionary()
        xyzw = d[order]
        w = xyzw[:, 3]
        w /= sum(w)
        w *= 4 * pi
        return

    def nqbyorder(self, order):
        """Scaling was derived from files in data/"""
        idx = find_nearest(AVAILABLEORDERS, order)
        return NUMBERQUADPOINTS[idx]
