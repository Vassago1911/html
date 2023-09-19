# chain complex from special digraph

class Special_Digraph():
    def __init__(self,):
        self.nodes = tuple()
        self.edges = tuple()
        self.known_morphisms = list()
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
                        self.flags[ix] = self.flags[ix] + [ tuple( list(flag) + list((VV,)) ) ]
            self.flags[ix] = tuple(sorted(self.flags[ix]))

    def get_top_flags(self):
        self.get_my_flags()
        if len(self.flags)>=2:
            return self.flags[len(self.flags)-3]
        else:
            return self.flags

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

    def cone(self):
        tmp = Special_Digraph()
        for _ in range(len(self.nodes)+1):
            tmp.add_node()
        for e in self.edges:
            tmp.add_edge(*e)
        t = tmp.nodes[-1]
        for n in tmp.nodes[:-1]:
            tmp.add_edge(n[0],t[0])
        return tmp

    #def product(self,other):

    # def add_morphism(self,ts:list[int]):
    #TODO: pushout s.t. po((cone,i1),(cone,i2))=suspension(i)

# class DiGraph_Morphism():
#     def __init__(self,g:Special_Digraph,h:Special_Digraph,map:list[int]):

# class Chain_Complex():
#     def __init__(self,graph):
#         self.max_degree = len(graph.nodes) + 1
#         self.simplices = self.calc_flag_cx(graph)

#     def calc_flag_cx(self,graph):
#         pass

# pt = Special_Digraph(); pt.add_node() # pt = pt
# I = Special_Digraph(); I.add_node(); I.add_node(); I.add_node(); I.add_edge(0,1); I.add_edge(0,2) # I = [.<-.->.]
# I = I.suspend(); I = I.suspend(); I = I.suspend();

g = Special_Digraph()
g.add_node()
g.add_node()     #S0
s0 = g

spheres = [s0]
cones = [s0.cone()]
for _ in range(6):
    print()
    print()
    spheres = spheres + [ spheres[-1].suspend() ]
    #cones = cones + [ spheres[-1].cone() ]
    print(spheres[-1].get_top_flags())
    print()
    #print(cones[-1].get_top_flags())

d2 = Special_Digraph()
d2.add_node()
d2.add_node()
d2.add_node()
d2.add_edge(0,1)
d2.add_edge(0,2)
d2.add_edge(1,2)

# d2 = minimal simplicial D^2
# todo d2 x S1 and find, homology knows it's an S1