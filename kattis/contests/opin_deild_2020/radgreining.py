def main():
    n, m = map(int, input().split(" "))
    s = ["?"] * n
    for _ in range(m):
        i, b = input().split(" ")
        i = int(i) - 1
        for c in b:
            if s[i] != "?" and s[i] != c:
                print("Villa")
                return
            else:
                s[i] = c
            i += 1
    print("".join(s))


if __name__ == "__main__":
    main()
