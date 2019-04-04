"""A collection of functions which have a known integral
when integrated over the unit sphere.
These functions take cartesian input, i.e. (x,y,z) from the unit sphere
and return a scalar f(x,y,z), together with the known integral.
The inputs x,y and z can also be numpy arrays, then also f(x,y,z) is an
array of the same length."""

from numpy import pi, inf, conj, sin
from sphericalquadpy.tools.sphericalharmonics import ylm
from sphericalquadpy.tools.transformations import xyz2thetaphi


def f1(x, y, z):
    """The constant function."""
    return 1.0 * (z > -inf)


def integralf1():
    return 4 * pi


def f2(x, y, z):
    """The indicator function for the upper half."""
    return 1.0 * (z > 0)


def integralf2():
    return 2 * pi


def f3(x, y, z):
    """Spherical harmonic of order 1,1"""
    thetaphi = xyz2thetaphi([x, y, z])
    i, j, m, n = 1, 1, 1, 1
    theta = thetaphi[:, 0]
    phi = thetaphi[:, 1]
    return ylm(i, j, theta, phi) * conj(ylm(m, n, theta, phi)) * sin(theta)


def integralf3():
    return 1
