import math


def InputData():
    print("Giai phuong trinh bac 2:\n")
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    return a, b, c


def SolveEqual(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("Vo so nghiem")
    elif a == 0 and b == 0 and c != 0:
        print("Vo nghiem")
    elif a == 0 and b != 0:
        x = -c/b
        print("Ptb1 x=", str(x))
    else:
        delta = math.pow(b, 2) - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("Nghiem phan biet:\n")
            print("x1=%.3lf" % x1, "x2=%.3lf" % x2)
        elif delta == 0:
            x0 = -b / (2 * a)
            print("Nghiem kep:\n")
            print("x0 = %.2f" % (x0))
        else:
            print("Vo nghiem thuc.")


def main():
    a, b, c = InputData()
    SolveEqual(a, b, c)


if __name__ == "__main__":
    main()
