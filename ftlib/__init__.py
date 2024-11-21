from ._Ftlib import Ftlib


from .projects import _Projects
from .cursus import _Cursus
from ._Constants import *
from .journal import _Journal
from .users import _Users

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")