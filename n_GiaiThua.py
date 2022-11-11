def InputData():
    n = int(input("n="))
    return n


def GiaiThua(n):
    s = 1
    for i in range(1, n+1):
        s = s*i
    return s


def main():
    n = int(input("n="))
    s = GiaiThua(n)
    print("%d" % n, "!=%d" % s)


if __name__ == "__main__":
    main()
