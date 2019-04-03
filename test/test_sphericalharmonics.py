import pytest
from scipy.integrate import dblquad
from numpy import conj, sin, pi, array
from numpy.linalg import norm
from sphericalquadpy.tools.sphericalharmonics import ylm
from sphericalquadpy.tools.transformations import xyz2thetaphi


def test_integrate_to_unity():
    i, j, m, n = 1, 2, 1, 2

    def f(theta, phi):
        return ylm(i, j, theta, phi) * conj(ylm(m, n, theta, phi)) * sin(theta)

    val, err = dblquad(f, 0, 2 * pi, 0, pi)
    assert abs(val - 1.0) < 2 * err

    i, j, m, n = 12, 23, 12, 23

    def f(theta, phi):
        return ylm(i, j, theta, phi) * conj(ylm(m, n, theta, phi)) * sin(theta)

    val, err = dblquad(f, 0, 2 * pi, 0, pi)
    assert abs(val - 1.0) < 2 * err


def test_integrate_to_zero():
    i, j, m, n = 1, 2, 0, 2

    def f(theta, phi):
        return ylm(i, j, theta, phi) * conj(ylm(m, n, theta, phi)) * sin(theta)

    val, err = dblquad(f, 0, 2 * pi, 0, pi)
    assert abs(val - 0.0) < 2 * err

    i, j, m, n = 1, 2, 1, 3

    def f(theta, phi):
        return ylm(i, j, theta, phi) * conj(ylm(m, n, theta, phi)) * sin(theta)

    val, err = dblquad(f, 0, 2 * pi, 0, pi)
    assert abs(val - 0.0) < 2 * err


def test_multievaluate_thetaphi():
    thetaphi = array([[0, 0], [1, 1]])
    ylm(1, 2, thetaphi[:, 0], thetaphi[:, 1])


def test_multievaluate_xyz():
    xyz = array([[0, 0, 1], [1, 0, 0]])
    ylm(1, 2, xyz[:, 0], xyz[:, 1], xyz[:, 2])


def test_duality_spherical_cartesian():
    poles = array(
        [[+1.0, 0, 0], [0, +1, 0], [0, 0, +1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    )
    valxyz = ylm(1, 2, poles[:, 0], poles[:, 1], poles[:, 2])

    thetaphi = xyz2thetaphi(poles)
    valthetaphi = ylm(1, 2, thetaphi[:, 0], thetaphi[:, 1])
    assert norm(valxyz - valthetaphi) < 1.0e-10


def test_toomanyinputsyieldserro():
    with pytest.raises(Exception):
        _ = ylm(1, 1, 1, 2, 3, 4, 5)
