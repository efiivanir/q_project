__version__ = '0.0'
__author__ = "Efi Ivanir efi.ivanir@gmail.com"

from . import Finance,Statistics,Common
__all__ = ['Finance','Statistics','Common']


def extend_pandas():
    """
    extends pandas by exposing methods to be used like:
    df.sharpe(), df.best('day'), ...
    """
    from pandas.core.base import PandasObject as _po
    _po.compsum = Statistics.compsum
    _po.comp = Statistics.comp
    _po.returns = Statistics.returns
    _po.returns_log = Statistics.returns_log
    _po.returns_com = Statistics.returns_com

extend_pandas()
