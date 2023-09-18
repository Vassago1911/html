class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = []
        self._flags = dict()
        self._flags[-1] = [(),]
        self._flags[0] = list()

    def add_node(self):
        self.nodes = self.nodes + [(len(self.nodes),)]
        self._flags[0] = sorted(set( self._flags[0] + [ (len(self.nodes),) ] ))

    def add_edge(self,i,j):
        if ( i>j ):
            j,i = i,j
        if ( (i,) in self.nodes ) and ( (j,) in self.nodes ) and ( (i,j) not in self.edges ) :
            self.edges = sorted(set( self.edges + [(i,j),] ))
            self._flags[1] = self.edges

    def gen_flags(self):
        def get_2flags_with_edge(st):
            s,t=st
            res = []
            candidates = list(filter(lambda x: x[0]==t,self.edges))
            #print(candidates)
            for _,u in candidates:
                if (s,u) in self.edges:
                    res = res + [ (s,t,u) ]
            return res
        def get_3flags_with_2flag(stu):
            s,t,u = stu
            my_edges = [ (s,t),(t,u),(s,u) ]
            res=[]
            candidates = list(filter(lambda x: x[0]==u,self.edges))
            for _,v in candidates:
                if (s,v) in self.edges\
                and (t,v) in self.edges\
                and (u,v) in self.edges:
                    res = res + [ (s,t,u,v) ]
            return res
        # def get_4flags_with_3flag(stuv):
        #     s,t,u,v = stuv
        #     res=[]
        #     candidates = list(filter(lambda x: x[0]==t,self.edges))
        #     for _,z in candidates:
        #         if (s,v) in self.edges\
        #         and (t,v) in self.edges\
        #         and (u,v) in self.edges:
        #             res = res + [ (s,t,u,v) ]
        #     return res

        self._flags[2] = list()
        self._flags[3] = list()
        # self._flags[4] = list()

        for flag in self._flags[1]:
            self._flags[2] = self._flags[2] + get_2flags_with_edge(flag)

        for flag in self._flags[2]:
            self._flags[3] = self._flags[3] + get_3flags_with_2flag(flag)

        # for flag in self._flags[3]:
        #     self._flags[4] = list()#self._flags[4] + get_4flags_with_3flag(flag)

    @property
    def flags(self):
        if self._flags != None:
            return self._flags
        else:
            self.gen_flags()
            return self._flags

complete_graph = Graph()
for _ in range(5):
    complete_graph.add_node()
edges = [ (i,j) for i in range(len(complete_graph.nodes)) for j in range(len(complete_graph.nodes)) if j > i ]
for e in edges:
    complete_graph.add_edge(*e)
print(complete_graph.flags)

# moebius_candidate = Graph()

# for _ in range(8):
#     moebius_candidate.add_node()

# edges = [ (0,2),(0,3),(0,4),(0,6),(1,2),(1,4),(1,5),(2,3),(2,5),(2,7),(3,4),(3,7),(4,5),(4,6),(5,6),(5,7),]
# for e in edges:
#     moebius_candidate.add_edge(*e)

# print(moebius_candidate.flags)