def range_gen(start=None, stop=None, step=None):
    if step is None:
        step = 1
    if not start is None and stop is None:
        start, stop = 0, start
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > step:
            yield start
            start += step
    return
