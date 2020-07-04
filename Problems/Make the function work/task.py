def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    y = x + 5
    return y - y % 5
