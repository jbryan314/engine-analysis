def interp(x, xp, yp, type='linear'):

    """ Interpolates all values between two arrays, given an intermediate value x and its index i in the arrays.
    Supports linear, monotonic cubic, and nearest neighbor interpolation

    Parameters:
        x : float
            The x value at which to interpolate. Must lie between xp[i] and xp[j] (some two adjacent values in xp).
        i : int
        xp : array-like
        yp : array-like
    """

    if type == 'linear':
        pass
    elif type == 'cubic':
        pass
    elif type == 'nearest':
        pass
    else:
        raise ValueError("Interpolation type '{}' not supported".format(type))


def linear_interp(x, xp, yp):
    pass


def cubic_interp(x, xp, yp):
    # TODO: find x in xp

    # TODO: perform cubic interpolation between xp and yp given x
    pass


def nearest_neighbor(x, xp, yp):
    pass
