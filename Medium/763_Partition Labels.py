from collections import defaultdict

S = "ababcbacadefegdehijhklij"

lst = []

last_i = 0
ct = []
cur_ct = 0

d = {}
l1 = []
for i in range(len(S) + 1):
    ss = set(S[last_i:i])
    if ss not in lst:
        lst.append(ss)
        last_i = i
        cur_ct = i - last_i
    else:
        if lst.index(ss) not in d:
            d[lst.index(ss)] = i
        else:
            ii = 0 if len(l1) == 0 else l1[-1]
            l1.append(i - ii)

        print(lst.index(ss), i)
l1.append(len(S) - sum(l1))

print(l1)
# not working


cache = defaultdict(lambda:None)
Max = -1
for i in range(len(S)):
    if cache[S[i]] == None:
        cache[S[i]] = [i,i]
    else:
        cache[S[i]][1] = i

l=sorted(cache.values())

left = l[0]
res = []
for i in range(1,len(l)):
    if left[1] >= l[i][0]:
        left[1] = max(l[i][1], left[1])
    else:
        res.append(left[1] - left[0] + 1)
        left = l[i]
res.append(left[1] - left[0] + 1)
print(res)
