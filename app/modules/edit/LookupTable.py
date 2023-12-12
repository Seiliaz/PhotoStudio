import scipy
from scipy.interpolate import UnivariateSpline

def LookupTable(x, y) -> UnivariateSpline :
    spline = UnivariateSpline(x, y)
    return spline
