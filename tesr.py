x = None
y = None
z = None


def yuju1(x, z):
    z /= y

def yuju2(z):
    z += 1


def yuju3(z, y):
    z += y


if x > 0 & y > 0:
    yuju1(x,z)
    if x > 1 | z >1:
        yuju2(z)
    yuju3(z, y)
else:
    if x > 1 | z >1:
        yuju2(z)
    yuju3(z, y)