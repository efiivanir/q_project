import numpy as _np

def compsum(data):
    """ Calculates rolling compounded returns """
    return data.add(1).cumprod() - 1


def comp(data):
    """ Calculates total compounded returns """
    return data.add(1).prod() - 1


def returns(data):
    """ Return simple returns"""
    _df = data.pct_change()
    _df.columns = ['Returns']
    return _df.copy()

def returns_log(data):
    """ Return log returns"""
    _df = _np.log(data.pct_change())
    _df = _df.fillna(0).replace([_np.inf, -_np.inf], 0)
    _df.columns = ['ReturnsLog']
    return _df.copy()

def returns_com(data):
    """ Return comulative returns"""
    _df = (1 + data.pct_change()).cumprod()
    _df.columns = ['ReturnsCom']
    return _df.copy()
