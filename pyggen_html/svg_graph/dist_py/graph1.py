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
                        print(i, "    ",stats[4*j:4*(j+1)+1])
                    else:
                        print('      ',stats[4*j:4*(j+1)+1])
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
        #TODO: sth wrong here
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

    # TODO: downward and upward ( homology / cohomology ) zips for valid s,t combinations per boundary degree

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
            return " ".join(list(map(lambda x: f"{x: 2d}",line)))
        print("================================================")
        N = len(self.ds)
        for i,d in enumerate(self.ds):
            print()
            for c in d:
                print(f"{i-1: 2d}: ",print_line(c))
        print("------------------------------------------------")
        print("================================================")
        print()
        print("================================================")

complete = Graph()
for _ in range(5):
    complete.add_node()

for i in range(5):
    for j in range(i+1,5):
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