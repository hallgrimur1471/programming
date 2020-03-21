def main():
    v, a, t = map(float, input().split(" "))
    print((v * t) + (0.5 * a * t * t))


if __name__ == "__main__":
    main()
