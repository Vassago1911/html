# from sympy import diff
# from sympy import solve
# from sympy.abc import a,b,c,d,t,u,v
# exprn = ((a-c)+t*u)**2+((b-d)+t*v)**2
# d_exprn = diff(exprn,t)

# equation = [ d_exprn ]
# t_exprn = solve(equation,t,dict=True)[0][t]

# # t_exprn == (-a*u - b*v + c*u + d*v)/(u**2 + v**2)
# exprn.subs(t,t_exprn)

# es ist n konvexes problem, which means, ich kann auf minimum
# testen mit vier tests
def g(x,v,t):
    return [ x_ + t * v_ for x_,v_ in zip(x,v) ]

def dist(x,y):
    return (sum([ (x_-y_)**2 for x_,y_ in zip(x,y) ]))**.5

def min_of_pt_on_segment(x,v,c):
    if ( dist( c, g(x,v,-.1) ) < dist( c, g(x,v,0) ) ):
        return False
    if ( dist( c, g(x,v,1) ) > dist( c, g(x,v,1.1) ) ):
        return False
    return True

x = [1,2,3]
v = [1,0,0]

cs = [ [0+i,3,6] for i in range(0,10)  ]

for c in cs:
    print(min_of_pt_on_segment(x,v,c))