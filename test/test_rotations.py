import pytest
from numpy import array, pi
from numpy.random import randn, rand
from numpy.linalg import norm
from sphericalquadpy.tools.rotations import rotate, randomrotate, \
    randomaxisrotate, randomanglerotate, rotationmatrix


def test_rotatedpointsareonsphere():
    """Test whether points that were on the sphere remain on the sphere."""
    n = 10
    points = randn(n, 3)
    for i in range(n):
        points[i, :] /= norm(points[i, :])

    axis = randn(3)
    axis = axis / norm(axis)

    angle = 2 * pi * rand()

    rotatedpoints = rotate(axis, angle, points)

    assert norm(1.0 - norm(rotatedpoints, axis=1)) < 1e-12


def test_rotatedpointisonsphere():
    """Test whether a point that were on the sphere remain on the sphere."""
    point = randn(3)
    point = point / norm(point)
    axis = randn(3)
    axis = axis / norm(axis)

    angle = 2 * pi * rand()

    rotatedpoint = rotate(axis, angle, point)

    assert norm(1.0 - norm(rotatedpoint)) < 1e-12


def test_rotatedpointsareonsphere_manyrotations():
    """Test whether points that were on the sphere remain on the sphere,
    even after performing many rotations"""
    n = 10
    points = randn(n, 3)
    for i in range(n):
        points[i, :] /= norm(points[i, :])

    for _ in range(100):
        axis = randn(3)
        axis = axis / norm(axis)

        angle = 2 * pi * rand()

        points = rotate(axis, angle, points)

        assert norm(1.0 - norm(points, axis=1)) < 1e-12


def test_rotate_forth_and_back():
    """Test whether points that were on the sphere remain on the sphere."""
    n = 10
    points = randn(n, 3)
    for i in range(n):
        points[i, :] /= norm(points[i, :])

    axis = randn(3)
    axis = axis / norm(axis)

    angle = 2 * pi * rand()

    rotatedpoints = rotate(axis, angle, points)
    twicerotatedpoints = rotate(axis, -angle, rotatedpoints)
    assert norm(points - twicerotatedpoints) < 1e-12


def test_rotatedpointsareonsphere_partiallyrandom():
    """Test whether points that were on the sphere remain on the sphere.
    But here we check the methods that choose axis or angle at random"""
    n = 10
    points = randn(n, 3)
    for i in range(n):
        points[i, :] /= norm(points[i, :])

    rotatedpoints = randomrotate(points)
    assert norm(1.0 - norm(rotatedpoints, axis=1)) < 1e-12

    axis = randn(3)
    axis = axis / norm(axis)
    rotatedpoints = randomanglerotate(axis, points)
    assert norm(1.0 - norm(rotatedpoints, axis=1)) < 1e-12

    angle = 2 * pi * rand()
    rotatedpoints = randomaxisrotate(angle, points)
    assert norm(1.0 - norm(rotatedpoints, axis=1)) < 1e-12

    rotatedpoints = randomrotate(points)
    assert norm(1.0 - norm(rotatedpoints, axis=1)) < 1e-12
