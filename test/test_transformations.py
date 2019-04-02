"""Check whether the transformations from spherical to cartesian coordinates
and vice versa are implemented such that when applying both of them
consecutively we end up at the same points.
"""

import pytest
from numpy import array, pi
from numpy.linalg import norm
from sphericalquadpy.tools.transformations import xyz2thetaphi, thetaphi2xyz


def test_xyz2thetaphi_then_thetaphi2xyz():
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


def test_thetaphi2xyz_then_xyz2thetaphi():
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


def test_xyz2thetaphi_dimension_exception():
    """Test whether we raise an exception for the
    case when we give an input that has not dimension 3."""

    invalidpoint = array([[1, 0, 0, 0]])
    with pytest.raises(Exception):
        _ = xyz2thetaphi(invalidpoint)


def test_thetaphi2xyz_dimension_exception():
    """Test whether we raise an exception for the
    case when we give an input that has not dimension 3."""

    invalidpoint = array([[pi, pi, 0]])
    with pytest.raises(Exception):
        _ = thetaphi2xyz(invalidpoint)


def test_xyz2thetaphi_point_not_on_unitsphere_exception():
    """Test whether we raise an exception for the
    case when the point does not have norm one and therefore
    is not part of the unit sphere."""

    invalidpoint = array([[1.1, 0, 0, ]])
    with pytest.raises(Exception):
        _ = xyz2thetaphi(invalidpoint)
