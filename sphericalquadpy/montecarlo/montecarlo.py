from sphericalquadpy.quadrature import Quadrature
from numpy import pi, ones
from numpy.random import randn
from numpy.linalg import norm


class MonteCarlo(Quadrature):

    def computequadpoints(self, order):
        xyz = randn(order, 3)
        xyz /= norm(xyz, axis=1)[:, None]
        return xyz

    def computequadweights(self, order):
        weights = 4 * pi / order * ones(order)
        return weights


