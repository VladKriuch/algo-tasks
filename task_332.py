from math import sqrt

def main():
    number = int(input('Enter the number: '))
    for k in range(1, 5):
        decompose = to_sum_of_squares(number, k)
        if decompose:
            for i, n in enumerate(decompose):
                decompose[i] = int(sqrt(n))
            print(f'x = {decompose[0]}, y = {decompose[1]}, z = {decompose[2]}, t = {decompose[3]}')
            break

def to_sum_of_squares(n:int, k:'squares count:int')->list:
    if (n < 0) or (k <= 0):
        return []
    maximum = round(sqrt(n))
    if n == maximum*maximum:
        return [n]
    for c in range(1, maximum+1):
        decomposition = to_sum_of_squares((n-c*c), k-1)
        if decomposition:
            return [c*c]+decomposition
