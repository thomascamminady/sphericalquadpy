"""Check whether the transformations from spherical to cartesian coordinates
and vice versa are implemented such that when applying both of them
consecutively we end up at the same points.
"""

from numpy import array, pi
from numpy.linalg import norm
import pytest
import sphericalquadpy
from sphericalquadpy.tools.transformations import xyz2thetaphi, thetaphi2xyz


def test_xyz2thetaphi2xyz():
    """Starting from a point in (x,y,z), we have to return to the same point
    when performing the transformation to (theta,phi) followed by the
    transformation back to (x,y,z)."""

    poles = array([[+1, 0, 0],
                   [0, +1, 0],
                   [0, 0, +1],
                   [-1, 0, 0],
                   [0, -1, 0],
                   [0, 0, -1]])
    thetaphi = xyz2thetaphi(poles)
    newpoles = thetaphi2xyz(thetaphi)
    assert norm(poles - newpoles) < 1.0e-14


def test_thetaphi2xyz2thetaphi():
    """Starting from a point in (theta,phi), we have to return to the same
    point when performing the transformation to (x,y,z) followed by the
    transformation back to (theta,phi)."""
    poles = array([[0, 0],
                   [0, pi / 2],
                   [pi / 2, pi / 2],
                   [pi, pi / 2],
                   [-1 / 2 * pi, pi / 2],
                   [0, pi]])
    xyz = thetaphi2xyz(poles)
    newpoles = xyz2thetaphi(xyz)
    assert norm(poles - newpoles) < 1.0e-14
