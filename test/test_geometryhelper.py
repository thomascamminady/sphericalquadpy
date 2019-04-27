from sphericalquadpy.tools.geometryhelper import cross, cross_, project, lerp, \
    slerp, distance, angle, s2area, area, EPSILON, eightfold
from numpy import zeros, ones, sqrt, pi
from numpy.linalg import norm
from numpy.random import rand, randn


def test_EPSILON():
    assert EPSILON == 1e-12


def test_cross():
    vec1 = [0, 0, 1]
    vec2 = [0, 1, 0]
    result = zeros(3)
    result[0] = -1
    assert norm(cross(vec1, vec2) - result) < 1e-12


def test_project_alreadynormalized():
    vec1 = zeros(3)
    vec1[0] = 1

    assert norm(project(vec1) - vec1) < 1e-12


def test_project():
    vec1 = ones(3)
    assert norm(project(vec1) - vec1 / sqrt(3)) < 1e-12


def test_lerp_endpoints():
    vec1 = rand(3)
    vec2 = rand(3)
    l = lerp(vec1, vec2, 2)

    assert norm(vec1 - l[:, 0]) < 1e-12
    assert norm(vec2 - l[:, 1]) < 1e-12


def test_lerp_endpoints():
    vec1 = rand(3)
    vec2 = rand(3)
    n = 100
    l = lerp(vec1, vec2, n)

    assert l.shape == (3, n)


def test_slerp_endpoints():
    vec1 = randn(3)
    vec1 /= norm(vec1)
    vec2 = randn(3)
    vec2 /= norm(vec2)
    sl = slerp(vec1, vec2, 2)

    assert norm(vec1 - sl[:, 0]) < 1e-12
    assert norm(vec2 - sl[:, 1]) < 1e-12


def test_distance_1():
    vec1 = zeros(3)
    vec1[0] = 1

    vec2 = zeros(3)
    vec2[0] = -1

    assert norm(pi - distance(vec1, vec2)) < 1e-12


def test_distance_2():
    vec1 = zeros(3)
    vec1[0] = 1

    vec2 = zeros(3)
    vec2[2] = 1

    assert norm(pi / 2 - distance(vec1, vec2)) < 1e-12


def test_distance_3():
    vec1 = zeros(3)
    vec1[0] = 1

    vec2 = zeros(3)
    vec2[0] = 1

    assert norm(0 - distance(vec1, vec2)) < 1e-12


def test_angle():  # area of octant
    vec1 = zeros(3)
    vec2 = zeros(3)
    vec3 = zeros(3)

    vec1[0] = 1
    vec2[1] = 1
    vec3[2] = 1

    assert norm(angle(vec2, vec1, vec3) - pi / 2) < 1e-12


def test_area():  # area of octant
    vec1 = zeros(3)
    vec2 = zeros(3)
    vec3 = zeros(3)

    vec1[0] = 1
    vec2[1] = 1
    vec3[2] = 1

    assert norm(area(vec1, vec2, vec3) - pi / 2) < 1e-12


def test_area_radius_equals2():  # area of octant
    vec1 = zeros(3)
    vec2 = zeros(3)
    vec3 = zeros(3)

    vec1[0] = 2
    vec2[1] = 2
    vec3[2] = 2

    assert norm(area(vec1, vec2, vec3) - 2 * pi) < 1e-12


def test_s2area():  # area of octant
    vec1 = zeros(3)
    vec2 = zeros(3)
    vec3 = zeros(3)

    vec1[0] = 100
    vec2[1] = 100
    vec3[2] = 100

    assert norm(s2area(vec1, vec2, vec3) - pi / 2) < 1e-12


def test_eightfold():
    pts = zeros((3, 1))
    pts[0, 0] = 1
    pts[1, 0] = 2
    pts[2, 0] = 3

    allpts = eightfold(pts)
    n,m = allpts.shape
    assert n == 3
    assert m == 8
