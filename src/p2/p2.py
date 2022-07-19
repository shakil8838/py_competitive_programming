import math
import os
import random
import re
import sys

from past.builtins import raw_input

if __name__ == '__main__':
    n = int(input())
    if n != 0 and n <= 100:
        if n % 2 == 1:
            print("Weird")
        elif n % 2 == 0:
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            else:
                print("Not Weird")
