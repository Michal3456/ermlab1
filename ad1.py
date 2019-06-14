import math

print("Enter square function:")
print("In format ax^2+bx+c dla a,b,c=R")
__ar = []
__ar.append(int(input("Enter (integer) a:")))
__ar.append(int(input("Enter (integer) b:")))
__ar.append(int(input("Enter (integer) c:")))
def second_I(tmp):
    if tmp == 0:
        return __ar[0]
    elif tmp == 1:
        return __ar[1]
    elif tmp == 2:
        return __ar[2]
def fix_delta(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    return delta
def fix_x1_x2(delta, a, b, c, tmp):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if tmp == 1:
        return x1
    elif tmp == 2:
        return x2
    else:
        return 444
def write_x1_x2_or_x0():
    delta=fix_delta(second_I(0), second_I(1), second_I(2))
    if delta < 0:
        stn = "x1 = absence delta negative\nx2 = absence delta negative"
    if delta > 0:
        x1 = fix_x1_x2(delta, second_I(0), second_I(1), second_I(2), 1)
        x2 = fix_x1_x2(delta, second_I(0), second_I(1), second_I(2), 2)
        stn = "x1 = %.2f\nx2 = %.2f" % (x1, x2)
    elif delta==0:
        x1 = fix_x1_x2(delta, second_I(0), second_I(1), second_I(2), 1)
        stn = "x0 = %.2f" % x1
    print(stn)

write_x1_x2_or_x0()