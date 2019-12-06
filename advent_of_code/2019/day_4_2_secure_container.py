#!/usr/bin/env python3.7


def main():
    start, end = list(map(int, input().split("-")))
    num_valid_passwords = calculate_number_of_valid_passwords(start, end)
    print(f"There are {num_valid_passwords} valid passwords.")


def calculate_number_of_valid_passwords(start, end):
    num_valid_passwords = 0

    for i in range(start, end + 1):
        if not has_two_strike(i):
            continue
        if not is_never_decreasing(i):
            continue
        num_valid_passwords += 1

    return num_valid_passwords


def has_two_strike(n):
    strike = 0
    last = None
    for c in str(n):
        if c == last:
            strike += 1
        elif c != last and strike == 2:
            return True
        else:
            strike = 1
        last = c

    if strike == 2:
        return True
    return False


def is_never_decreasing(n):
    n_str = str(n)
    for i in range(len(n_str) - 1):
        if n_str[i] > n_str[i + 1]:
            return False
    return True


if __name__ == "__main__":
    main()


class TestHasTwoStrike:
    def test_returns_true_if_has_two_strike(self):
        assert has_two_strike(122345)
        assert has_two_strike(112233)
        assert has_two_strike(111122)

    def test_returns_false_if_does_not_have_two_strike(self):
        assert not has_two_strike(1232456)
        assert not has_two_strike(123444)


class TestIsNeverDecreasing:
    def test_returns_true_if_never_decreasing(self):
        assert is_never_decreasing(1111123)
        assert is_never_decreasing(135679)

    def returns_false_if_decreasing(self):
        assert not is_never_decreasing(223450)
