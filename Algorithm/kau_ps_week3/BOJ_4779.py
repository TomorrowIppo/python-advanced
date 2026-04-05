import sys

input = sys.stdin.readline

ls = [
    "-",
    "- -",
]

for i in range(1, 13):
    ls.append(ls[i - 1] + " "*pow(3, i-1) + ls[i - 1])

while True:
    try:
        N = int(input())

        rst = ls[N]
        print(rst)
    except:
        break