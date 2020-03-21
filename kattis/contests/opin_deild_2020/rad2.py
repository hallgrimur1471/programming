def update(i, b, ps):
    to_delete = list()
    orig_i = i
    for p in ps:
        stop = False
        i = orig_i
        for c in b:
            if p[i] != "?" and p[i] != c:
                to_delete.append(p)
                stop = True
            else:
                p[i] = c
            if stop:
                break
            i += 1
    new_ps = []
    for p in ps:
        if p not in to_delete:
            new_ps.append(p)
    return new_ps


def main():
    n, m = map(int, input().split(" "))
    s = ["?"] * n
    posib = list()
    posib.append(s)
    for _ in range(m):
        i, b = input().split(" ")
        i = int(i) - 1
        ps1 = update(i, b, posib)
        ps2 = update(i, "".join(list(reversed(b))), posib)

        new_ps = ps1
        for p in ps2:
            if p not in ps1:
                new_ps.append(p)
        possib = new_ps
    if not possib:
        print("Villa")
    else:
        for p in possib:
            for i, c in enumerate(p):
                if c == "?":
                    p[i] = "T"
            print("".join(p))
            return


if __name__ == "__main__":
    main()
