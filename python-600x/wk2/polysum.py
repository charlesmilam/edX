import math # module used for pi constant and tangent

def polysum(n, s):
    '''
    A regular polygon has 'n' number of sides. Each side has length 's'.
    n should be an int > 2
    s can be either a positive int or float > 0

    The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    The perimeter of a polygon is: length of the boundary of the polygon

    This function will determine the area of a regular polygon based on the
    parameters n and s. It also computes the perimeter of the polygon, also
    based on n and s.

    The function returns the sum of the area of the polygon and the squared
    perimeter of the polygon, rounded to 4 decimal places
    '''

    # compute the area of the polygon, based on passed in parameters
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    # compute the perimeter of the polygon based on same parameters
    peri = n * s

    # now return the sum of the area and the squared perimeter, rounded to
    # 4 decimal places
    return round(area + peri**2, 4)
