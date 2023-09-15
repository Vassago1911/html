# from graph vertices to some connections by closest neighbours
# py test

vertices = [[892, 444]
,[1559, 1064]
,[646, 1583]
,[448, 684]
,[1049, 320]
,[1495, 609]
,[1653, 764]
,[1542, 1660]
,[1007, 1116]
,[1214, 538]
,[728, 787]
,[1178, 1003]
,[824, 1445]
,[634, 1102]
,[899, 606]
,[573, 419]
,[298, 1055]
,[1009, 1182]
,[1054, 1426]
,[523, 1665]
,[401, 1487]
,[1571, 412]
,[453, 1318]
,[1589, 977]
,[1249, 1487]
,[695, 365]
,[150, 778]
,[211, 1252]
,[960, 1837]]

def dist(v,w):
    return int( ( (v[0]-w[0])**2 + (v[1]-w[1])**2 )**.5 )

def get_distance_matrix(vertices):
    d = dict()
    for v in vertices:
        d[tuple(v)] = dict()
        for w in vertices:
            d[tuple(v)][tuple(w)] = dist(v,w)
    return d

def get_n_closest_neighbours(vertices, n=4):
    d = get_distance_matrix(vertices)
    rks = dict()
    for k in d:
        rks[k] = sorted(list(d[k].items()),key=lambda t: t[1] )
        rks[k] = list(filter(lambda x: x[0]!=k, rks[k]))
        rks[k] = rks[k][:n]
    return rks

r = get_n_closest_neighbours(vertices)