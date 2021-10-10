from . import core
from . import functor
from . import monoid
from . import operations
from .operations import fold
from .operations import foldr
from .par_operations import fold as par_fold

# from .par_operations import foldr as par_foldr

__all__ = ["core", "monoid", "functor", "operations", "fold", "foldr", "par_fold"]
