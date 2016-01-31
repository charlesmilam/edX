def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiation_exposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    tot_exp = 0
    stepper = start

    while stepper < stop:
        tot_exp += f(stepper) * step
        stepper += step

    print 'tot exp', tot_exp
    return tot_exp

radiation_exposure(0, 5, 1) # should be 39.10318784326239
radiation_exposure(5, 11, 1) # should be 22.94241041057671
radiation_exposure(0, 11, 1) # should be 62.0455982538
radiation_exposure(40, 100, 1.5) # should be 0.434612356115
