from sphericalquadpy.levelsymmetric.writtendict import levelsymmetricdictionary
from sphericalquadpy.levelsymmetric.createxyzwdict import createdict, writedict
import os
from numpy.linalg import norm
from numpy import pi


def test_dictionary_correct():
    d = levelsymmetricdictionary()
    orders = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    for order in orders:
        assert order in d
        q = d[order]
        assert abs(sum(q[:, 3]) - 4 * pi) < 1e-12


def test_writedictionaryworks():
    os.chdir("sphericalquadpy/levelsymmetric/")
    writedict()
    d1 = createdict()
    d2 = levelsymmetricdictionary()

    orders = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    for order in orders:
        a = norm(d1[order])
        b = norm(d2[order])
        assert abs(a - b) < 1e-12
    os.chdir("../../")
