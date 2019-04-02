from numpy import zeros, dot
from abc import ABCMeta, abstractmethod


class Quadrature(object, metaclass=ABCMeta):

    @abstractmethod
    def computequadpoints(self, order):
        pass

    @abstractmethod
    def computequadweights(self, order):
        pass

    def __init__(self, order):
        self.xyz = self.computequadpoints(order)
        self.weights = self.computequadweights(order)

    def integrate(self, functions):
        """Integrate an array of functions with the given quadrature.
        It is assumed that every function has the signature f(x,y,z), i.e.
        takes three inputs and returns one scalar output."""
        results = zeros(len(functions))
        for i, func in enumerate(functions):
            results[i] = dot(self.weights,
                             func(self.xyz[:, 0],
                                  self.xyz[:, 1],
                                  self.xyz[:, 2]))
        return results
