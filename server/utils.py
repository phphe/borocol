
def toDict(arg):
    r = None
    if type(arg) == list:
        r = [dict(i) for i in arg]
    else:
        r = dict(arg)
    return r