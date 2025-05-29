import numpy as np


def generate_exp(n, lam):
    return np.random.exponential(scale=1 / lam, size=n)


def generate_lognormal(n, sigma):
    return np.random.lognormal(mean=0, sigma=sigma, size=n)


def generate_normal(n, sigma):
    return np.random.normal(0, sigma, n)


def rand_skew_norm(fAlpha, fLocation, fScale):
    """
    https://stackoverflow.com/questions/36200913/generate-n-random-numbers-from-a-skew-normal-distribution-using-numpy
    literal adaption from:
    http://stackoverflow.com/questions/4643285/how-to-generate-random-numbers-that-follow-skew-normal-distribution-in-matlab
    original at:
    http://www.ozgrid.com/forum/showthread.php?t=108175
    """
    sigma = fAlpha / np.sqrt(1.0 + fAlpha**2)

    afRN = np.random.randn(2)
    u0 = afRN[0]
    v = afRN[1]
    u1 = sigma * u0 + np.sqrt(1.0 - sigma**2) * v

    if u0 >= 0:
        return u1 * fScale + fLocation
    return (-u1) * fScale + fLocation


def generate_skewnormal(N, skew=0.0):
    return [rand_skew_norm(skew, 0, 1) for _ in range(N)]
