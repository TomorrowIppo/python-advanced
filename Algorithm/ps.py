import sys

input = sys.stdin.readline

n = int(input())
pattern = input().strip()

prefix, suffix = pattern.split('*')
p_len = len(prefix)
s_len = len(suffix)

for _ in range(n):
    inp_str = input().strip()

    if len(inp_str) < (p_len + s_len):
        print("NE")
        continue

    if inp_str[:p_len] == prefix and inp_str[-s_len:] == suffix:
        print("DA")
    else:
        print("NE")