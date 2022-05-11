# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sympy as sp
from sympy.utilities.lambdify import lambdify


def Bisection_Method(polynomial3, start_point, end_point, epsilon):
    iterations_counter = 0
    error_range = -(math.log((epsilon / abs(start_point-end_point)), math.e)) / math.log(2, math.e)
    while end_point - start_point > epsilon:
        iterations_counter += 1
        if iterations_counter - 1 > error_range:
            print("This polynomial does not converge on Bisection Method  ")
            return
        mid = (start_point + end_point) / 2
        end_val = polynomial3(end_point)
        mid_val = polynomial3(mid)
        if end_val * mid_val > 0:
            end_point = mid
        else:
            start_point = mid
    if round(polynomial(mid)) != 0:
        return
    print(f'After {iterations_counter} iterations, the root is:')
    return mid

def Newton_Raphson(polynomial3, start_point, end_point, epsilon):
    iterations_counter = 0
    x_r1 = (start_point + end_point) / 2
    while abs(polynomial3(x_r1)) > epsilon:
        iterations_counter += 1
        x_r = x_r1
        x_r1 = x_r - (polynomial3(x_r) / polynomial_derivative(x_r))


    print(f'After {iterations_counter} iterations, the root is:')
    return x_r1




def general_function(polynomial2, start_point, end_point, choice):
    arr_roots = []
    index = 0
    x0, x1 = start_point, start_point
    while x1 < end_point:
        x1 += 0.1
        x1 = round(x1, 1)
        val_x0 = polynomial2(x0)
        val_x1 = polynomial2(x1)
        if val_x0 * val_x1 < 0:
            #root = Bisection_Method(polynomial2, x0, x1, e)
            root = Newton_Raphson(polynomial2, x0, x1, e)
            if root in arr_roots or root is None:
                return
            else:
                arr_roots.append(root)
                print(arr_roots[index])
                index += 1
        x0 = x1
    return arr_roots


# Press the green button in the gutter to run the script.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    e = 0.001
    x = sp.symbols('x')
    polynomial = 4 * x ** 3 - 48 * x + 5
    polynomial_derivative = polynomial.diff(x)#do a derivative
    polynomial_derivative2 = polynomial_derivative.diff(x)
    polynomial_derivative = lambdify(x, polynomial_derivative)#define the polynomial_derivative as a function of x like math
    polynomial = lambdify(x, polynomial)

    """print("Press the range")
    start = input("start point: ")
    end = input("end point: ")
    print("Press the method you want to display on your polynomial:"
          "1-Bisection method"
          "2-Raphson-Newton method"
          "3- Secant method")
    choice = int(input(""))"""
    general_function(polynomial, 3, 4, 1)
    general_function(polynomial_derivative, 3, 4, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
