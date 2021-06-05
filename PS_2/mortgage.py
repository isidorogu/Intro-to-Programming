import math
def mortgage_pymnt(l, p, r):
    mortgage =  (r*l)/(1-(1+r)**(-p))
    return mortgage
    print(mortgage)
