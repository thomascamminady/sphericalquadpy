"""Transformations for points on the sphere.
We can transform from cartesian to spherical
or from spherical to cartesian.
Points are assumed to live on the unit sphere.
The notation is consistent with the one found here:
http://mathworld.wolfram.com/SphericalCoordinates.html
"""
# pylint: disable=C0103
# pylint: disable=E1111
from numpy import arctan2, arccos, cos, sin, zeros
from numpy.linalg import norm


def xyz2thetaphi(xyz):
    """Transformation from points on the unit sphere given by their
    cartesian representation as (x,y,z) to their
    spherical representation as (theta,phi),
    with the azimuthal angle theta in [0,2pi) and
    the polar angle phi in [0,pi].

    Args:
        xyz: An (n,3) numpy.ndarray of cartesian points living on the unit
        sphere.
    Raises:
        ValueError: If any point does not live on the unit sphere.
        ValueError: If not exactly three points per row are given.
    Returns:
        thetaphi: An (n,2) numpy.ndarray of spherical points living on the unit
        sphere.
    """

    n, dim = xyz.shape
    if not dim == 3:
        raise ValueError('We require points in 3D, not %dD.' % (dim,))
    thetaphi = zeros((n, 2))
    for i in range(n):
        x, y, z = xyz[i, :]
        r = norm([x, y, z])
        if not abs(r - 1.0) < 1.0e-14:
            raise ValueError('Point %i does not live on the unit sphere. '
                             'The coordinates are (%d,%d,%d) wit norm %d.'
                             % (i, x, y, z, r))
        thetaphi[i, 0] = arctan2(xyz[i, 1], xyz[i, 0])
        thetaphi[i, 1] = arccos(xyz[i, 2])
    return thetaphi


def thetaphi2xyz(thetaphi):
    """Transformation from points on the unit sphere given by their
    spherical representation as (theta,phi) to their
    cartesian representation as (x,y,z),
    with the azimuthal angle theta in [0,2pi) and
    the polar angle phi in [0,pi].

    Args:
        thetaphi: An (n,2) numpy.ndarray of spherical points living on the unit
        sphere.
    Raises:
        ValueError: If not exactly two points per row are given.
    Returns:
        xyz: An (n,3) numpy.ndarray of cartesian points living on the unit
        sphere.
    """

    n, dim = thetaphi.shape
    if not dim == 2:
        raise ValueError('We require points in 2D, not %dD.' % (dim,))
    xyz = zeros((n, 3))
    for i in range(n):
        theta, phi = thetaphi[i, :]
        xyz[i, 0] = cos(theta) * sin(phi)
        xyz[i, 1] = sin(theta) * sin(phi)
        xyz[i, 2] = cos(phi)
    return xyz
