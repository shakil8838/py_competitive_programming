from past.builtins import raw_input

n = int(raw_input())
co = 1
if n <= 150:
    while co <= n:
        print(co, end="")
        co += 1
