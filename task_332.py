# inspired by http://uneex.ru/FrBrGeorge/News/2017-02-01
from math import sqrt, ceil

def task_332():
    n = int(input("Enter any natural number: "))
    try:
        if not n.isdigit():
            raise ValueError
        sqrt_n = int(sqrt(n))
        if n == sqrt_n*sqrt_n:
            return f'x = 0, y = 0, z = 0, t = {sqrt_n}'
        Y = x = ceil(sqrt(n)/2) # the smallest integer greater than or equal to N
        x_squared = x**2
        while x_squared <= n:
            while Y and (Y-1)*(Y-1)*3 >= n - x_squared:
                Y -= 1
            y = Z = Y
            y_squared = y**2
            while (y <= x) and (x_squared + y_squared <= n):
                while Z and (Z-1)*(Z-1)*2 >= n - x_squared - y_squared:
                    Z -= 1
                z = t = Z
                z_squared = z**2
                while (z <= y) and (x_squared + y_squared + z_squared <= n):
                    while t**2 > n - x_squared - y_squared - z_squared:
                        t -= 1
                    if x_squared + y_squared + z_squared + t**2 == n:
                        return f'x = {x}, y = {y}, z = {z}, t = {t}'
                    z += 1
                    z_squared = z*z
                y += 1
                y_squared = y*y
            x += 1
            x_squared = x*x
    except ValueError:
        print('Please, enter a number next time')
        return None
