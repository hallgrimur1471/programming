from sys import stdin, stdout


def solve(x, y, k, g):
    while k:
        if g[x][y] == "v":
            x += 1
        elif g[x][y] == "^":
            x -= 1
        elif g[x][y] == "<":
            y -= 1
        elif g[x][y] == ">":
            y += 1
        k -= 1
    return (x + 1, y + 1)


def main():
    n, m = map(int, stdin.readline().split(" "))
    g = []
    for line in range(n):
        g.append(stdin.readline().rstrip())
    q = int(stdin.readline())
    for _ in range(q):
        x, y, k = map(int, stdin.readline().split(" "))
        ans = solve(x - 1, y - 1, k, g)
        print("{} {}".format(ans[0], ans[1]))


if __name__ == "__main__":
    main()
