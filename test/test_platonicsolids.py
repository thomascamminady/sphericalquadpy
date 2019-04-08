from sphericalquadpy.tools.platonicsolids import icosahedron, octahedron
from numpy.linalg import norm


def test_ico_dim():
    vertices, faces = icosahedron()

    assert vertices.shape == (3, 12)
    assert faces.shape == (3, 20)


def test_ico_onunitsphere():
    vertices, faces = icosahedron()

    for i in range(12):
        x = norm(vertices[:, i])
        assert abs(x - 1) < 1e-12


def test_octa_dim():
    vertices, faces = octahedron()

    assert vertices.shape == (3, 6)
    assert faces.shape == (3, 8)


def test_octa_onunitsphere():
    vertices, faces = octahedron()

    for i in range(6):
        x = norm(vertices[:, i])
        assert abs(x - 1) < 1e-12
