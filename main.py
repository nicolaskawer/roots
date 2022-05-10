# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def calc_polynomial_in_point(polynomial1, point):
    value = 0
    for i in range(len(polynomial1)):
        if i == (len(polynomial1) - 1):
            value += polynomial1[i]
            break
        value += (point ** (len(polynomial1) - i - 1)) * (polynomial1[i])
    return value


def Bisection_Method(polynomial3, start_point, end_point, epsilon):
    iterations_counter = 0
    error_range = -(math.log((epsilon / abs(start_point-end_point)), math.e)) / math.log(2, math.e)
    while end_point - start_point > epsilon:
        iterations_counter += 1
        if iterations_counter - 1 > error_range:
            print("This polynomial does not converge on Bisection Method  ")
            return
        mid = (start_point + end_point) / 2
        end_val = calc_polynomial_in_point(polynomial3, end_point)
        mid_val = calc_polynomial_in_point(polynomial3, mid)
        if end_val * mid_val > 0:
            end_point = mid
        else:
            start_point = mid
    if round(calc_polynomial_in_point(polynomial, mid)) != 0:
        return
    print(f'After {iterations_counter} iterations, the root is:')
    return mid


def general_function(polynomial2, start_point, end_point, choice):
    arr_roots = []
    index = 0
    x0, x1 = start_point, start_point
    while x1 < end_point:
        x1 += 0.1
        x1 = round(x1, 1)
        val_x0 = calc_polynomial_in_point(polynomial2, x0)
        val_x1 = calc_polynomial_in_point(polynomial2, x1)
        if val_x0 * val_x1 < 0:
            root = Bisection_Method(polynomial2, x0, x1, e)
            if root in arr_roots or root is None:
                continue
            else:
                arr_roots.append(root)
                print(arr_roots[index])
                index += 1
        x0 = x1
    return arr_roots


def create_derive(polynomial_to_derive):
    for i in range(len(polynomial_to_derive)):
        if i == len(polynomial_to_derive) - 1:
            polynomial_to_derive[i] = 0
        polynomial_to_derive[i] = (len(polynomial_to_derive) - i - 1) * polynomial_to_derive[i]
    polynomial_to_derive.remove(polynomial_to_derive[len(polynomial_to_derive)-1])
    return polynomial_to_derive

# Press the green button in the gutter to run the script.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    size = int(input("Enter the biggest power of the polynomial: "))
    e = 0.00000000001
    arr = []
    print("press the coefficient of: ")
    for i in range(size+1):
        num = int(input(f'X^{size-i}= '))
        arr.append(num)
    polynomial = tuple(arr)
    polynomial_derivative = tuple(create_derive(arr))
    print(polynomial_derivative)
    """print("Press the range")
    start = input("start point: ")
    end = input("end point: ")
    print("Press the method you want to display on your polynomial:"
          "1-Bisection method"
          "2-Raphson-Newton method"
          "3- Secant method")
    choice = int(input(""))"""
    general_function(polynomial, -3, 2, 1)
    general_function(polynomial_derivative, -3, 2, 1)













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
