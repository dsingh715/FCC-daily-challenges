perfect_cubes = []

def count_perfect_cubes(a, b):
    if b>a:
        for i in range(a,b+1):
            y = abs(i)
            if round(y ** (1 / 3)) ** 3 == y:
                perfect_cubes.append(y)
    else:
        for i in range(b,a+1):
            y = abs(i)
            if round(y ** (1 / 3)) ** 3 == y:
                perfect_cubes.append(y)
    
    a = len(perfect_cubes)
    return a

count_perfect_cubes(9214, -8127)
