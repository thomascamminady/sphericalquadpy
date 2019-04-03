"""A collection of functions which have a known integral
when integrated over the unit sphere.
These functions take cartesian input, i.e. (x,y,z) from the unit sphere
and return a scalar f(x,y,z), together with the known integral.
The inputs x,y and z can also be numpy arrays, then also f(x,y,z) is an
array of the same length."""

from numpy import pi, ones, inf
from sphericalquadpy.tools.sphericalharmonics import ylm


def f1(x, y, z):
    """The constant function."""
    return 1.0 * (z > -inf), 4 * pi


def f2(x, y, z):
    """The indicator function for the upper half."""
    return 1.0 * (z > 0), 2 * pi


def f3(x, y, z):
    """Spherical harmonic of order 1,1"""
    return ylm(1, 1, x, y, z), 999999
