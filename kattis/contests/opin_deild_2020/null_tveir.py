from sys import stdin, stdout


def ok(n):
    s = set(str(n))
    if len(s) == 1:
        return "0" in s or "2" in s
    else:
        return len(s) == 2 and "0" in s and "2" in s


def main():
    n = int(stdin.readline())
    c = 0
    for i in range(0, n + 1):
        c += ok(i)
    stdout.write(str(c))


if __name__ == "__main__":
    main()
