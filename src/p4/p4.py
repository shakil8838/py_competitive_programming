from past.builtins import raw_input

if __name__ == '__main__':
    n = int(raw_input())

    if 0 < n <= 20:
        for i in range(0, n):
            out = i ** 2
            print(out)
