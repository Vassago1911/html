import numpy as np

r,R = 7/8,1

def point_sequence(N:int=24):
    def basic_root(N:int=24):
        return np.exp(2*np.pi*1/N*1j)
    roots = [ basic_root(2*N)*basic_root(N)**i for i in range(N) ]
    r_roots = [ r*ro for ro in roots ]
    R_roots = [ R*ro for ro in roots ]
    tmp = list(map(list,  zip(r_roots,R_roots)))
    tmp = sum(tmp,start=[])
    return tmp

def plot_points(zs):
    xs = list(map(lambda x: x.real,zs))
    ys = list(map(lambda x: x.imag,zs))
    import matplotlib.pyplot as plt
    plt.scatter(xs,ys); plt.show()

def plot_lines(zs):
    xs = list(map(lambda x: x.real,zs))
    ys = list(map(lambda x: x.imag,zs))
    L = len(xs)
    lines = list()
    for i,x0 in enumerate(xs):
        y0 = ys[i]
        x1, y1 = xs[(i+1)%L], ys[(i+1)%L]
        x2, y2 = xs[(i+2)%L], ys[(i+2)%L]
        x3, y3 = xs[(i+3)%L], ys[(i+3)%L]
        x4, y4 = xs[(i+4)%L], ys[(i+4)%L]
        if i%4 == 0:
            lines = lines + [ [(x0,y0),(x1,y1)],
                              [(x1,y1),(x3,y3)],
                              [(x2,y2),(x3,y3)],
                              [(x2,y2),(x4,y4)],
                               ]
    from matplotlib import collections as mc
    import matplotlib.pyplot as plt
    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = plt.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    #plt.scatter(xs,ys);
    plt.show()

ps = point_sequence(42)

plot_lines(ps)

ps = ps[2:] + [ps[0],ps[1]]

plot_lines(ps)