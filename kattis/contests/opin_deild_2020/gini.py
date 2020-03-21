from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    y = [0] * n
    for i in range(n):
        y[i] = int(stdin.readline())
    y.sort()
    nom = 0
    den = 0
    for i in range(1, n + 1):
        nom += i * y[i - 1]
        den += y[i - 1]
    nom *= 2
    den *= n
    fraction = float(nom) / den
    ans = fraction - ((float(n) + 1) / (n))
    stdout.write(str(ans))


if __name__ == "__main__":
    main()
