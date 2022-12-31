<<<<<<< HEAD

def pibo(a):
    pibo = [0, 1]
    while True:
        if pibo[-1] > a:
            break
        b = pibo[-2] + pibo[-1]
        pibo.append(b)
    pibo.pop(-1)
    return pibo
=======

def pibo(a):
    pibo = [0, 1]
    while True:
        if pibo[-1] > a:
            break
        b = pibo[-2] + pibo[-1]
        pibo.append(b)
    pibo.pop(-1)
    return pibo
>>>>>>> 45f89869a0318eeb74cd1d754218da8d81b3c112
print(pibo())