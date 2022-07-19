if __name__ == "__main__":
    inputLen = int(input())
    agre_num = 0
    sol_count = 0

    for iddx in range(inputLen):
        theList = input().split()
        for idx in theList:
            agre_num += int(idx)
        if agre_num >= 2:
            sol_count += 1
            agre_num = 0
        else:
            agre_num = 0

    print(sol_count)
