class Chains_of_Flag_Complex():
    def __init__(self,graph):


class Chain():
    def __init__(self,basis,coeffs=[]):
        self.basis = sorted(basis)
        self.dim = -1 if len(self.basis) == 0 else len(self.basis[0])
        for b in self.basis:
            assert len(b) == self.dim, "dimension inconsistent chain basis, please fix"
        if ( len(coeffs) != len(basis) ):
            self.chain = { b: 0 for b in self.basis }
        else:
            self.chain = { b: coeffs[i] for i,b in enumerate(self.basis) }
    def __repr__(self):
        nonzero_keys = list(filter( lambda x: x[1]!=0, self.chain.items()))
        if len(nonzero_keys) == 0:
            return "0"
        else:
            return f"{'+'.join(list(map(lambda x: f'{x[1]}*{x[0]}' if x[1]!=1 else f'{x[0]}'  ,nonzero_keys)))}"
    def __add__(self,other):
        res = { b: self.chain[b]+other.chain[b] for b in self.basis }
        coeffs = [ res[b] for b in self.basis ]
        return Chain(self.basis,coeffs)
    def __sub__(self,other):
        res = { b: self.chain[b]-other.chain[b] for b in self.basis }
        coeffs = [ res[b] for b in self.basis ]
        return Chain(self.basis,coeffs)
    def coeff_of(self,b):
        if b in self.basis:
            return self.chain[b]
        return 0
    @property
    def basic_chains(self):
        return [ Chain(
            sorted(self.basis),
            coeffs = \
            [ 1 if i == j else 0 for i,b in enumerate(sorted(self.basis)) ] )
        for j in range(len(self.basis)) ]
    def basic_boundaries(self)->list[list[int]]:
        basis = self.basis
        basic_boundaries = []
        for b in basis:
            for j,_ in enumerate(b):
                basic_boundaries = sorted(set( basic_boundaries + [ b[:j]+b[j+1:], ] ))
        from numpy import zeros as default
        D = default((len(basis),len(basic_boundaries))).T
        for i,b in enumerate(basis):
            for j,_ in enumerate(b):
                db = b[:j]+b[j+1:]; sign = (-1)**j
                D[basic_boundaries.index(db),i]=sign
        return { "d":D, "basis_s": basis, "basis_t": basic_boundaries }

class Graph():
    def __init__(self,):
        self.nodes = []
        self.edges = []
        self._flags = dict()
        self._flags[-1] = [(),]
        self._flags[0] = []
        self._flags[1] = []

    def add_node(self):
        self.nodes = self.nodes + [ (len(self.nodes),) ]
        self._flags[0] = self.nodes
        self.gen_flags()

    def add_edge(self,i,j):
        if i==j:
            return
        if i>j:
            i,j = j,i
        self.edges = sorted(set(self.edges + [(i,j)]))
        self._flags[1] = self.edges
        self.gen_flags()

    def show_flags(self):
        self.gen_flags()
        for i,stats in enumerate(self._flags):
            if len(stats) > 8:
                for j in range(len(stats)//4):
                    if j == 0:
                        print(i, "    ",stats[4*j:4*(j+1)])
                    else:
                        print('      ',stats[4*j:4*(j+1)])
            else:
                print(i, "    ", stats)

    def gen_flags(self):
        def get_all_sup1_flags(flag):
            res = []
            candidate_nodes = [ v[0] for v in self.nodes if ( v not in flag and v[0] > max(flag) ) ]
            for node in candidate_nodes:
                node_valid = True;
                for s in flag:
                    if (s,node) in self.edges:
                        continue
                    else:
                        node_valid = False;
                        #print(f"breaking {flag} {node} {(s,node)}")
                        break
                if node_valid:
                    res = res + [ tuple(list(flag)+[node]) ]
            return res

        def sth_sth(n_1_flags):
            n_flags = []
            if len(n_1_flags) > 1:
                for flag in n_1_flags:
                    n_flags = n_flags + get_all_sup1_flags(flag)
            return n_flags

        #self._flags[-1] = [(),]
        self._flags = []
        self._flags = self._flags + [ self.nodes, ]
        # => self._flags[0] = vertices/nodes
        self._flags = self._flags + [ self.edges, ]
        # => self._flags[1] = edges
        max_degree = len(self.nodes)
        for i in range(2,max_degree+10):
            if (len(self._flags[i-1])>0):
                self._flags = self._flags + [ sth_sth(self._flags[i-1]) ]
            else:
                break
            #print(self._flags[i])
        self.calc_boundaries()
        #TODO: besser kaltstarten, nur ne kante oder knoten mehr heisst nicht, noch mal alles

    def bdy(self,ss,ts):
        #TODO: sth wrong here; or is there!?
        def signed_b(s):
            return tuple( ( (-1)**i, s[:i]+s[i+1:]) for i in range(len(s)) )

        D_tmp = [ [0 for _ in range(len(ts)) ] for _ in range(len(ss)) ]
        #print(ss,ts)
        for i in range(len(ss)):
            s = ss[i]
            bs = signed_b(s)
            for j in range(len(ts)):
                t = ts[j]
                # parity of index = sign; (0,1,2,3) -signed_b-> [(1,2,3),(0,2,3),(0,1,3),(0,1,2)]
                # gives sign
                hit_list = list(filter(lambda x: x[1] == t, bs))
                c = 0
                for x0,x1 in hit_list:
                    c += x0
                D_tmp[i][j] = c
        return D_tmp

    def calc_boundaries(self):
        fgs = list(reversed(self._flags))
        downward_chain = list( zip( fgs[:-1], fgs[1:] ) )
        self.ds = list()
        for ss,ts in downward_chain:
            if len(ss) == 0:
                self.ds = [[ len(self.nodes)*[0,],],]
            else:
                self.ds = self.ds + [self.bdy(ss,ts),]
        for i,d in enumerate(self.ds):
            self.ds[i] = list(zip(*d))
        self.ds = self.ds + [[len(self.ds[-1])*[1,]]]
        self.ds = list(reversed(self.ds))

    def print_boundaries(self):
        def print_line(line):
            return " ".join(list(map(lambda x: f"{x: 2d}" if x!=0 else "  ",line)))
        print("================================================")
        N = len(self.ds)
        for i,d in enumerate(self.ds):
            print(" -- ")
            print("bases:")
            if i-1 == -1:
                print("-1: ()")
            elif i-1>=0:
                print(f"{i-1}: {sorted(self._flags[i-1])}")
            print(f"{i}: {sorted(self._flags[i])}")
            print()
            for c in d:
                print(f"| {i-1: 2d}: ",print_line(c), " |")
        print("------------------------------------------------")
        print("================================================")
        print()
        print("================================================")

complete = Graph()
degree = 5
for _ in range(degree):
    complete.add_node()

for i in range(degree):
    for j in range(i+1,degree):
        complete.add_edge(i,j)

complete.show_flags()
complete.print_boundaries()

moebius_candidate = Graph()

for _ in range(8):
    moebius_candidate.add_node()

edges = [ (0,2),(0,3),(0,4),(0,6),
          (1,2),(1,4),(1,5),
          (2,3),(2,5),(2,7),
          (3,4),(3,7),
          (4,5),(4,6),
          (5,6),(5,7),
        ]
for e in edges:
    moebius_candidate.add_edge(*e)

moebius_candidate.show_flags()
moebius_candidate.print_boundaries()

torus = Graph()
degree = 16
for _ in range(degree):
    torus.add_node()

edges = \
[
    (0,4),(0,14),(0,6),(0,15),(0,9),(0,13),(0,5),(0,12),
    (1,9),(1,15),(1,10),(1,14),(1,4),(1,12),(1,8),(1,13),
    (2,7),(2,12),(2,5),(2,13),(2,11),(2,15),(2,6),(2,14),
    (3,11),(3,13),(3,8),(3,12),(3,7),(3,14),(3,10),(3,15),
    (4,12),(4,14),
    (5,12),(5,13),
    (6,14),(6,15),
    (7,12),(7,14),
    (8,12),(8,13),
    (9,13),(9,15),
    (10,14),(10,15),
    (11,13),(11,15),
]

for e in edges:
    torus.add_edge(*e)

torus.show_flags()
torus.print_boundaries()