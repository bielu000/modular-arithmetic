#!/usr/local/bin env python

def modulo_power(num, exp, mod):
    _exp = exp
    _bin = ''

    while _exp != 0:
        _bin += str(_exp % 2)
        _exp /= 2
    
    pows = [] 

    k = 0 
    for val in _bin:
        if int(val) == 1:
            pows.append((int(val) +1) ** k) 
        k+= 1

    r = 1 # not good?
    for i in pows:
        r*= (num ** i) % mod

    return r % mod 

def modulo_inverse(a, b):
    u = 1
    w = a 
    x = 0
    z = b

    while w != 0:
        if w < z:
            u, x = x, u
            w, z = z, w  

        q = w / z 
        u = u - q * x
        w = w - q * z
    
    if z != 1:
        print "Brak rozwiazania"
        
        return None 

    if x < 0:
        x = x + b 

    print "Rowiazanie: {}".format(x)
    return x 

def euclidean_alghoritm(a, b, nwd, x2, x1, x, y2, y1, y, q, r):
    if r == 0:
        return [nwd, y]
    a = b
    b = r

    x = x2 - q*x1
    x2 = x1
    x1 = x

    y = y2 - q*y1
    y2 = y1
    y1 = y

    nwd = r
    q = a/b
    r = a-q*b

    return euclidean_alghoritm(a, b, nwd, x2, x1, x, y2, y1, y, q, r)

def calculate_euclidean(a, b, print_output=False):
    if a == None:
        raise ValueError("A cannot be None.")
    
    if b == None: 
        raise ValueError("B cannot be None.")

    if b > a:
        tmp = a 
        a = b
        b = tmp

    q = a/b
    r = a - q*b
    nwd = b
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    x = 1
    y = y2 - (q-1)*y1
    
    nwd, y =  euclidean_alghoritm(a, b, nwd, x2, x1, x, y2, y1, y, q, r)

    if print_output == True:
        print ("NWD({}, {}) = {}").format(a, b, nwd)
        
        if nwd == 1:
            print("{} * {} mod {} == 1").format(b, y, a)

    return nwd, y