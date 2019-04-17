#!/usr/bin/python3

def solve(n, m, h, v, f):
    sums = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(m):
            sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + int(f[i][j] == '@')
    if sums[n][m] % ((h + 1) * (v + 1)) != 0:
        return False
    each = sums[n][m] // ((h + 1) * (v + 1))
    if each == 0:
        return True
    li = -1
    vlines = [-1]
    for i in range(m):
        if sums[n][i + 1] - sums[n][li + 1] == each * (h + 1):
            li = i
            vlines.append(i)
    lj = -1
    cnth = 0
    hlines = [-1]
    for i in range(n):
        if sums[i + 1][m] - sums[lj + 1][m] == each * (v + 1):
            lj = i
            hlines.append(i)
    if len(vlines) < v + 2 or len(hlines) < h + 2:
        return False
    for i in range(1, v + 2):
        for j in range(1, h + 2):
            if sums[hlines[j] + 1][vlines[i] + 1] - sums[hlines[j - 1] + 1][vlines[i] + 1] - sums[hlines[j] + 1][vlines[i - 1] + 1] + sums[hlines[j - 1] + 1][vlines[i - 1] + 1] != each:
                return False
    return True


t = int(input())
for testcase in range(1, t + 1):
    n, m, h, v = map(int, input().split())
    s = [input() for i in range(n)]
    if solve(n, m, h, v, s):
        print("Case #{}: POSSIBLE".format(testcase))
    else:
        print("Case #{}: IMPOSSIBLE".format(testcase))