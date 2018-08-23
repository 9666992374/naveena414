import sys

S = sys.stdin.read()
S = S.split()
S = [int(i) for i in S]
n1 = S[0]
n2 = S[1]
c=(n1**n2)
print(c)
