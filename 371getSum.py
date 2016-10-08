def getSum(a, b):
    p, g, i = a ^ b, a & b, 1
    while True:
        if (g << 1) >> i == 0:
            return a ^ b ^ (g << 1)
        if ((p | g) << 2) >> i == ~0:
            return a ^ b ^ ((p | g) << 1)
        p, g, i = p & (p << i), (p & (g << i)) | g, i << 1

print getSum(3,2)