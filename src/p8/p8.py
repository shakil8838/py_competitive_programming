if __name__ == "__main__":
    loop = int(input())
    count = 0
    while count < loop:
        innn = input()
        if len(innn) <= 10:
            print(innn)
        else:
            print(f"{innn[0]}{len(innn) - 2}{innn[len(innn) - 1]}")
        count += 1
