import math
import os
import random
import re
import sys


def odd_even(n):
    if n%2==1:
        return "Weird"
    elif n>=2 and n<=5: 
        return "Not Weird"
    elif n>=6 and n<=20:
        return "Weird"
    elif n%2==0 or n>20:
        return "Not Weird"
n=int(input())
print(odd_even(n))