# chain complex from special digraph

class Special_Digraph():
    def __init__(self,):
        self.nodes = tuple()
        self.edges = tuple()
        self.still_special()

    def still_special(self):
        for i,j in self.edges:
            assert i<j, "somehow an evil edge has entered"
        self.get_my_flags()

    def get_my_flags(self):
        self.flags = dict()
        self.flags[-1] = ((),)
        self.flags[0] = self.nodes
        self.flags[1] = self.edges
        # max_degree = len(self.nodes) + 1
        ix = len(self.flags) - 2
        while len( self.flags[ ix ] ) > 0:
            starting_flags = self.flags[ix]
            edges = self.flags[1]
            nodes = self.flags[0]

            ix = ix + 1
            self.flags[ix] = []
            for VV in nodes:
                VV = VV[0]
                for flag in starting_flags:
                    valid = True
                    for v in flag:
                        if (v,VV) not in edges:
                            valid = False
                            break
                    if valid:
                        self.flags[ix] = self.flags[ix] + [ tuple( sorted(list(flag) + list((VV,))) ) ]
            self.flags[ix] = tuple(self.flags[ix])

    def add_node(self):
        self.nodes = tuple(sorted(list(self.nodes) + [(len(self.nodes),)]))
        self.still_special()

    def add_edge(self,i,j):
        if  ( (i,) in self.nodes ) \
        and ( (j,) in self.nodes ) \
        and ( i < j ):
            self.edges = tuple(sorted(list(self.edges) + [(i,j)]))
        else:
            print(f"edge add failed {i} {j}")
        self.still_special()

    def suspend(self):
        tmp = Special_Digraph()
        for _ in range(len(self.nodes)+2):
            tmp.add_node()
        for e in self.edges:
            tmp.add_edge(*e)
        for t in tmp.nodes[-2:]:
            for n in tmp.nodes[:-2]:
                tmp.add_edge(n[0],t[0])
        return tmp

class Chain_Complex():
    def __init__(self,graph):
        self.max_degree = len(graph.nodes) + 1
        self.simplices = self.calc_flag_cx(graph)

    def calc_flag_cx(self,graph):
        pass

g = Special_Digraph()
g.add_node()
g.add_node()
#S0
g = g.suspend() #S1
g = g.suspend() #S2
g = g.suspend() #S3
