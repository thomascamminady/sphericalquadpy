from sphericalquadpy.ldfeLinDisc.ldfe import *
from numpy import linspace, pi, array
from numpy.linalg import norm
from sphericalquadpy.ldfeLinDisc.helper.miscellaneous import project


def test_computeomegas_same_midpoint():
    x0, x1, z0, z1 = 1.0, 2.0, 3.0, 4.0
    omegas = computeomegas(x0, x1, z0, z1)

    # assert all have the same midpoint
    for i in range(3):
        assert norm(omegas[i](0) - omegas[3](0)) < 1e-10


def test_computeomegas_same_second_component():
    x0, x1, z0, z1 = 1.0, 2.0, 3.0, 4.0
    omegas = computeomegas(x0, x1, z0, z1)
    # assert that the second component of each point on the line is a
    a = 1 / sqrt(3)
    T = linspace(0, 1, 100)  # some t values
    for i in range(4):
        for t in T:
            assert norm(omegas[i](t)[1] - a) < 1e-10


def test_computeomegas_interpolatedonline():
    x0, x1, z0, z1 = 1.0, 2.0, 3.0, 4.0
    omegas = computeomegas(x0, x1, z0, z1)
    # assert that the points that are being interpolated fall between the
    # end point and the mid point
    T = linspace(0, 1, 100)  # some t values
    for i in range(4):
        out = omegas[i](1)
        mid = omegas[i](0)

        xMin = min([out[0], mid[0]])
        xMax = max([out[0], mid[0]])

        zMin = min([out[2], mid[2]])
        zMax = max([out[2], mid[2]])
        for t in T:
            assert xMin <= omegas[i](t)[0] <= xMax
            assert zMin <= omegas[i](t)[2] <= zMax


def test_computeomegas_endpoints():
    x0, x1, z0, z1 = 1.0, 2.0, 3.0, 4.0
    omegas = computeomegas(x0, x1, z0, z1)
    a = 1 / sqrt(3)
    # test that the end points are correct
    x = array([x1, a, z1])
    assert norm(x - omegas[0](1)) < 1e-10

    x = array([x1, a, z0])
    assert norm(x - omegas[1](1)) < 1e-10

    x = array([x0, a, z0])
    assert norm(x - omegas[2](1)) < 1e-10

    x = array([x0, a, z1])
    assert norm(x - omegas[3](1)) < 1e-10


def test_computeareas_equal_due_to_symmetry():
    x0, x1, z0, z1 = -0.1, +0.1, -0.1, +0.1
    omegas = computeomegas(x0, x1, z0, z1)
    areas = computeareas(omegas, x0, x1, z0, z1)
    for i in range(4):
        assert abs(areas[i] - areas[3]) < 1e-10


def test_computeareas_sums2fullsphere():
    x0, x1, z0, z1 = 0, 1 / sqrt(3), 0, 1 / sqrt(3)
    omegas = computeomegas(x0, x1, z0, z1)
    areas = computeareas(omegas, x0, x1, z0, z1)
    assert abs(4 * pi - sum(areas) * 24) < 1e-10


def test_computeweights_equalweightssymmetry():
    x0, x1, z0, z1 = 0.0, +0.1, 0.0, +0.1
    omegas = computeomegas(x0, x1, z0, z1)
    rhos = [0.5, 0.5, 0.5, 0.5]
    a = 1 / sqrt(3)
    weights = computeweights(rhos, omegas, a, x0, x1, z0, z1)
    print(weights)
    assert abs(weights[1] - weights[3]) < 1e-10


def test_computewieghts_invariant_under_rotation():
    x0, x1, z0, z1 = 0.0, +0.1, 0.0, +0.1
    omegas = computeomegas(x0, x1, z0, z1)
    rhos = [0.5, 0.5, 0.5, 0.5]
    a = 1 / sqrt(3)
    weights1 = computeweights(rhos, omegas, a, x0, x1, z0, z1)

    x0, x1, z0, z1 = -0.1, 0.0, -0.1, 0.0
    omegas = computeomegas(x0, x1, z0, z1)
    rhos = [0.5, 0.5, 0.5, 0.5]
    a = 1 / sqrt(3)
    weights2 = computeweights(rhos, omegas, a, x0, x1, z0, z1)
    assert abs(weights1[1] - weights2[1]) < 1e-10
    assert abs(weights1[3] - weights2[3]) < 1e-10
    assert abs(weights1[2] - weights2[0]) < 1e-10
    assert abs(weights1[0] - weights2[2]) < 1e-10


def test_projectOntoSphere():
    x0, x1, z0, z1 = 0.0, +0.1, 0.0, +0.1
    omegas = computeomegas(x0, x1, z0, z1)
    T = linspace(0, 1, 100)  # some t values
    for i in range(4):
        for t in T:
            s = project(omegas[i](t))
            assert abs(norm(s) - 1) < 1e-10
