from scipy.special import sph_harm
from sphericalquadpy.tools.transformations import xyz2thetaphi
from numpy import stack


def ylm(l, m, *args):
    if len(args) == 2:  # args = [theta,phi]
        return sph_harm(l, m, args[1], args[0])
    elif len(args) == 3:  # args = [x,y,z]
        xyz = stack([args[0], args[1],args[2]],axis=1)
        thetaphi = xyz2thetaphi(xyz)
        return sph_harm(l, m, thetaphi[:,1], thetaphi[:,0])
