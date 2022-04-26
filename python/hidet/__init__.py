import sys
from . import ir
from . import backend
from . import implement
from . import utils
from . import tos
from . import runtime
from . import driver

from .tos import Tensor, Operator, Module, FlowGraph

from .tos import ops
from .tos import empty, randn, zeros, ones, symbol, array, empty_like, randn_like, zeros_like, ones_like, symbol_like
from .tos import space_level, opt_level
from .tos import trace_from

sys.setrecursionlimit(10000)
