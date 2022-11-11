def InputData():
    print("Nhap 2 so a , b: \n")
    a = float(input("a="))
    b = float(input("b="))
    return a, b


def Tong(a, b):
    c = a + b
    return c


def Hieu(a, b):
    c = a - b
    return c


def Tich(a, b):
    c = a * b
    return c


def Thuong(a, b):
    if b == 0:
        print("Division by zero")
        exit()
    c = a / b
    return c


def main():
    a, b = InputData()
    c = Tong(a, b)
    print(a, " + ", b, "=", c)
    c = Hieu(a, b)
    print(a, " - ", b, "=", c)
    c = Tich(a, b)
    print(a, " * ", b, "=", c)
    c = Thuong(a, b)
    print(a, " / ", b, "=", c)


if __name__ == "__main__":
    main()
