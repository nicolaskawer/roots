# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calc_polynomial(polynomial1,point):
        sum1 = 0
        for i in range(size + 1):
            if(i == size):
                sum1 += polynomial1[i]
                break

            sum1 += (point ** (size - i)) * (polynomial1[i])
        return sum1
def Bisection_Method(polynomial, start_point, end_point, e):
    mid = 10000
    index = 0
    while abs(start_point - mid) > e:
        index += 1
        mid = (start_point + end_point) / 2
        sum_first = calc_polynomial(polynomial, start_point)
        sum_mid = calc_polynomial(polynomial, mid)
        if sum_first * sum_mid < 0:
            start_point = mid
        else:
            end_point = mid
    print(f'There was a {index}iterations')
    return mid

def general_function(polynomial, start_point, end_point, flag):
    g = 0.1
    arr = []
    index = 0
    num0, num1 = start_point, start_point
    while num1 < end_point:

        num1 += 0.1
        if num0 == 0 or num1 == 0:
            if num0 == 0:
                sum_x0 = calc_polynomial(polynomial, num0)
                if sum_x0 == 0:
                    if sum_x0 in arr:
                        continue
                    else:
                        arr.append(num0)
                        print("This case in itself no need to run it")
                        print(num0)
                        index += 1
            else:
                sum_x1 = calc_polynomial(polynomial, num1)
                if sum_x1 == 0:
                    if sum_x1 in arr:
                        continue
                    else:
                        arr.append(num1)
                        print("This case in itself no need to run it")
                        print(num1)
                        index += 1
        else:
            sum_x0 = calc_polynomial(polynomial, num0)
            sum_x1 = calc_polynomial(polynomial, num1)
            if sum_x0 * sum_x1 <= 0:
                slice1 = Bisection_Method(polynomial, num0, num1, e)
                if slice1 in arr:
                    continue
                else:
                    arr.append(slice1)
                    print(arr[index])
                    index += 1
        num0 = num1

    return arr










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    size = int(input("Enter the biggest power of the polynomial: "))
    e = 0.0001
    arr = []
    print("press the coefficient of: ")
    for i in range(size+1):
        num = int(input(f'X^{size-i}= '))
        arr.append(num)
    polynomial = tuple(arr)
    print("press the range")
    general_function(polynomial, -1, 2, 3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
