import sys
from itertools import permutations
input = sys.stdin.readline

maximum = -1e9
minimum = 1e9

n = int(input())
num = list(map(int, input().split()))
tools_num = list(map(int, input().split()))
tools_arr = ['+', '-', '*', '/']
tools = []


