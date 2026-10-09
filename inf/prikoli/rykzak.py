W = int(input())
n = int(input())
S = []
P = []
for i in range (n):
    s = input()
    w, p = map(int, s.split())
    S.append(w)
    P.append(p)

M = []
for i in range (n + 1):
    string = []
    for j in range (W + 1):
        if j == 0 or i == 0:
            string.append(0)
        else:
            if j - S[i - 1] >= 0:
                el = max(P[i - 1] + M[i - 1][j - S[i - 1]], M[i - 1][j])
            else:
                el = M[i - 1][j]
            string.append(el)
    M.append(string)
for i in range (n + 1):
    print(M[i])


res = []
cord = [n, W]
while cord[0] > 0:
    i = cord[0]
    j = cord[1]
    if j - S[i - 1] >= 0:
        x = M[i][j]
        x2 = M[i - 1][j]
        x3 = M[i - 1][j - S[i - 1]] + P[i - 1]
        if x == x3:
            res.append(i)
            cord = [i - 1, j - S[i - 1]]
        else:
            cord = [i - 1, j]
    else:
        cord = [i - 1, j]
print(res[::-1])
print(M[-1][-1])