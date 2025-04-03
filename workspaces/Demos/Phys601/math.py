import math
import textwrap
import time

delay = 0.1

for f in [
    "exp",
    "sin",
    "cos",
    "tan",
    "tan2",
    "asin",
    "acos",
    "atan",
    "atan2",
    "erf",
    "erfc",
    "factorial",
    "log",
    "log10",
    "sqrt",
    "sinh",
    "cosh",
    "tanh",
    "perm",
    "comb",
]:
    code = f"""\
    def {f}(*args):
        time.sleep(delay)
        return math.{f}(*args)
    """
    exec(textwrap.dedent(code))
