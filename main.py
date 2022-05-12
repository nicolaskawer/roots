# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from sympy.utilities.lambdify import lambdify
import sympy as sp

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


def Newton_Raphson(polynomial4, start_point, end_point, epsilon):
    iterations_counter = 0
    if counter_calls == 0:
        derivative = my_polynomial.diff(x)
        derivative = lambdify(x, derivative)
    else:
        derivative = my_polynomial_derivative.diff(x)
        derivative = lambdify(x, derivative)
    x_r1 = (start_point + end_point) / 2
    while abs(polynomial4(x_r1)) > epsilon:
        iterations_counter += 1
        x_r = x_r1
        if derivative(x_r) == 0:
            print("Cannot divide by zero!")
            return
        x_r1 = x_r - (polynomial4(x_r) / derivative(x_r))
    print(f'After {iterations_counter} iterations, the root is:')
    return x_r1


def general_function(polynomial2, start_point, end_point, choice):
    index = 0
    count = 0
    x0, x1 = start_point, start_point
    while x1 < end_point:
        x1 += 0.1
        x1 = round(x1, 1)
        if (x0 == 0 or x1 == 0) and count == 0:
            count += 1
            if x0 == 0:
                sum_x0 = polynomial(x0)
                if sum_x0 == 0:
                    if sum_x0 in arr_roots:
                        continue
                    else:
                        arr_roots.append(x0)
                        print("Special root:")
                        print(x0)
                        index += 1
            else:
                sum_x1 = polynomial(x1)
                if sum_x1 == 0:
                    if sum_x1 in arr_roots:
                        continue
                    else:
                        arr_roots.append(x1)
                        print("Special root:")
                        print(x1)
                        index += 1
        else:
            val_x0 = polynomial2(x0)
            val_x1 = polynomial2(x1)
            if val_x0 * val_x1 < 0:
                if choice == 1:
                    root = Bisection_Method(polynomial2, x0, x1, e)
                elif choice == 2:
                    root = Newton_Raphson(polynomial2, x0, x1, e)
                elif choice == 3:
                    root = secant_method(polynomial2, x0, x1, e)
                else:
                    print("Wrong choice!!\nNext time don't try to deal with us and press correct choice!! Bye")
                    exit(1)
                if root in arr_roots or root is None:
                    return
                else:
                    arr_roots.append(root)
                    print(arr_roots[index])
                    index += 1
        x0 = x1
    return arr_roots


def secant_method(polynomial5, start_point, end_point, epsilon):
    x_r0 = start_point
    x_r1 = end_point
    iterations_counter = 0
    while abs(polynomial5(x_r0)) > epsilon:
        iterations_counter += 1
        helper = x_r1
        if polynomial5(x_r1) - polynomial5(x_r0) == 0:
            print("Cannot divide by zero!")
            return
        x_r1 = (x_r0 * polynomial5(x_r1) - x_r1 * polynomial5(x_r0)) / (polynomial5(x_r1) - polynomial5(x_r0))
        x_r0 = helper

    if round(polynomial(x_r0)) != 0:
        return
    print(f'After {iterations_counter} iterations, the root is:')
    return x_r0


# Press the green button in the gutter to run the script.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    e = 0.001
    arr_roots = []
    x = sp.symbols('x')
    my_polynomial = 1 * x ** 4 + 1 * x ** 3 - 3 * x ** 2
    my_polynomial_derivative = my_polynomial.diff(x)  # do a derivative
    polynomial_derivative = lambdify(x, my_polynomial_derivative)  # define the polynomial_derivative as a function of x like math
    polynomial = lambdify(x, my_polynomial)
    print("Press the range:")
    start = int(input("start point [the lower point]: "))
    end = int(input("end point [[the lower point]: "))
    print("Press the method you want to display on your polynomial:"
          "\n1-Bisection method"
          "\n2-Raphson-Newton method"
          "\n3- Secant method")
    choice = int(input(""))
    counter_calls = 0
    general_function(polynomial, start, end, choice)
    counter_calls += 1
    general_function(polynomial_derivative, start, end, choice)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
