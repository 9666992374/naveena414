import sys

S = sys.stdin.read()
S = S.split()
S = [int(i) for i in S]
n1 = S[0]
n2 = S[1]
n3 = S[2]
if(n1>=n2) and (n1>=n3):
     print(n1)
elif(n2>=n1) and (n2>=n3):
     print(n2)
else:
     print(n3)
