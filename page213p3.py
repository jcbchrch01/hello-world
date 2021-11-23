def radialpattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)
