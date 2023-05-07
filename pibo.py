def pibo(a):
    pibo = [0, 1]
    while True:
        if pibo[-1] > a:
            break
        b = pibo[-2] + pibo[-1]
        pibo.append(b)
    pibo.pop(-1)
    return pibo
print(pibo())