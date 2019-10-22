# higher_order_functions.py
#
# A collection of Python3 higher order functions that can be used as decorators.


def trace(fn):
    """Returns a wrapper function that traces the function name, location
    and inputs.

    >>> @trace
        def double(x):
            return 2 * x

    >>> double(12)
    -> <function double at 0x10f65c158> ( 12 )
    24
    """
    def wrapped(x):
        print(f'-> {fn} ( {x} )')
        return fn(x)
    return wrapped


def memo(fn):
    """Returns a memoized function that makes use of a dictionary to re-use
    computed values in order to speed up tree recursive function calls.
    """
    cache = {}

    def memoized(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return memoized
