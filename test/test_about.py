import os

from sphericalquadpy.__about__ import __author__, __copyright__, __credits__, \
    __email__, __license__, __maintainer__, __status__, __version__


def test_about():
    # https://packaging.python.org/single_source_version/
    base_dir = "../"
    about = {}
    with open(os.path.join(base_dir, "sphericalquadpy", "__about__.py"),
              "rb") as f:
        exec(f.read(), about)


def test_about2():
    a = __author__
    b = __copyright__
    c = __credits__
    d = __email__
    e = __license__
    f = __maintainer__
    g = __status__
    h = __version__
