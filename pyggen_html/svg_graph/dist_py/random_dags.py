from random import randint as r

node_count = r(4,8)

V = list(range(node_count))
E = list()

for v in V:
    for w in [ w for w in V if w > v]:
        if r(0,32) > 15:
            E += [(v,w),]

F = list()

for v,w in E:
    for _,u in [ (t,u) for t,u in E if t==w and (v,u) in E ]:
        F += [(v,w,u)]

S = list()

for v,w,u in F:
    for _,x in [ (t,x) for t,x in E \
                 if u==t and
                   (u,x) in E and
                   (v,x) in E and
                   (w,x) in E ]:
        S += [(v,w,u,x)]

H = list()

for a,b,c,d in S:
    for _,e in [ (z,x) for z,x in E \
        if d == z and
        (a,x) in E and
        (b,x) in E and
        (c,x) in E and
        (d,x) in E
     ]:
     H += [(a,b,c,d,e)]

print(V)
print(E)
print(F)
print(S)
print(H)