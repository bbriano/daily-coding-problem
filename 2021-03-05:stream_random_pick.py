import random


def stream_random_pick(stream):
    """
    Pick a random element from a stream
    input
        stream -- a stream object that have a is_open and get_next method
    output
        a random element from the stream with uniform probability
    """
    count = 0
    element = None
    while stream.is_open():
        e = stream.get_next()
        count += 1
        r = random.random()
        if r < 1/count:
            element = e
    return element


def stream_random_pick_v2(stream):
    """
    Pick a random element from a stream
    input
        stream -- a stream object that have a is_open and get_next method
    output
        a random element from the stream with uniform probability
    """
    element = None
    for i,e in enumerate(stream):
        if random.randint(1, i+1) == 1:
            element = e
    return element
