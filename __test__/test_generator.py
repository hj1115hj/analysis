def squares(n=10):

    for i in range(n+1):
        yield i**2

#squares(10)

for x in  squares(10):
    print(x)


