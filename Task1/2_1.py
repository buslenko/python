import math

def f21(x):
    if x[4] == 'haml':
        if x[1] == 2010:
            if x[0] == 1970:
                if x[3] == 'sass':
                    return 2
                elif x[3] == 'nit':
                    return 3
            elif x[0] == 2019:
                return 1
            elif x[0] == 1985:
                return 0
        elif x[1]  == 2007:
            return 4
    elif x[4] == 'ecl':
        if x[3] == 'nit':
            if x[1] == 2010:
                return 6
            elif x[1] == 2007:
                return 7
        elif x[3] == 'sass':
            return 5
    elif x[4] == 'rebol':
        if x[1] == 2010:
            if x[0] == 1985:
                return 8
            elif x[0] == 2019:
                return 9
            elif x[0] == 1970:
                return 10
        elif x[1] == 2007:
            return 11