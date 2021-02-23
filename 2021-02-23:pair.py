
def cons(a, b):
    """
    a -> b -> (f -> c)
    """
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """
    (f -> c) -> c
    """
    def first(a, b):
        return a
    return pair(first)


def cdr(pair):
    """
    (f -> c) -> c
    """
    def last(a, b):
        return b
    return pair(last)


assert cdr(cons(3, 4)) == 4
