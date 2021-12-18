#stackoverflow clutch
import numpy as np
import pandas
import more_itertools
from copy import deepcopy

def islocalmax(x):
    """Both neighbors are lower,
    assumes a centered window of size 3"""
    return (x[0] < x[1]) & (x[2] < x[1])

def islocalmin(x):
    """Both neighbors are higher,
    assumes a centered window of size 3"""
    return (x[0] > x[1]) & (x[2] > x[1])

def isextrema(x):
    return islocalmax(x) or islocalmin(x)

def create_pp(col): 
    # @param p percentage filter
    mcol = deepcopy(list(col))
    mcol.insert(0, mcol[0])
    mcol.append(mcol[-1])
    tcol = [isextrema(x) for x in list(more_itertools.windowed(mcol, n=3))]
    stcol = [(x) for x in list(more_itertools.windowed(mcol, n=3))]
    pp = []
    for i, t_w in enumerate(tcol):
        if(t_w):
            if(islocalmax(stcol[i])):
                pp.append(1)
            if(islocalmin(stcol[i])):
                pp.append(-1)
        else:
            pp.append(0)
    return pp


