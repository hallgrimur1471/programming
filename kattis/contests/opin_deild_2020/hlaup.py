from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    if n % 4 != 0:
        stdout.write("Neibb")
        return

    if n % 100 == 0 and (n % 400 != 0):
        stdout.write("Neibb")
        return

    c = 0
    y = 2024
    while y <= n:
        y += 4
        if y % 100 == 0 and y % 400 != 0:
            continue
        c += 1
    stdout.write(str(c))


if __name__ == "__main__":
    main()
