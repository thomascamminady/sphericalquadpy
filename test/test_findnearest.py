from sphericalquadpy.tools.findnearest import find_nearest


def test_find_nearest():
    a = [1, 2, 3, 4, 5]
    assert find_nearest(a, 1.9) == 1  # the index


def test_find_nearest_toolow():
    a = [1, 2, 3, 4, 5]
    assert find_nearest(a, -100) == 0


def test_find_nearest_toohigh():
    a = [1, 2, 3, 4, 5]
    assert find_nearest(a, +100) == 4


def test_find_nearest_inthemiddle():
    a = [1, 2, 3, 4, 5]
    assert find_nearest(a, 1.5) == 1  # same as for rounding
