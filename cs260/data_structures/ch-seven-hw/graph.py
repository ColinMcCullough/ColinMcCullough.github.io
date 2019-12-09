from cs260.data_structures.ch_six_hw.priorityqueue import PriorityQueue
class Graph:
    def __init__(self):
        self.__vertList = {}
        self.__numVertices = 0

    @property
    def vertList(self):
        return self.__vertList

    @property
    def numVertices(self):
        return self.__numVertices

    @numVertices.setter
    def numVertices(self,new_num):
        self.__numVertices = new_num

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,vertex):
        if vertex in self.vertList:
            return self.vertList[vertex]
        else:
            return None

    def __contains__(self,vertex):
        return vertex in self.vertList

    def addEdge(self,frm,to,weight=0):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].addNeighbor(self.vertList[to], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class Vertex:
    """Vertex Class
        Interface:
            addNeighbor(nbr,weight): connects neighbor
            getConnections(): returns keys to all connections
            getId(): returns ID to vertex
            getWeight(nbr): returns weight between vertex and neighbor
    """    
    def __init__(self,key):
        self.__id = key
        self.__connected_to = {}
        self.__distance = 0
        self.__predecessor = None
        self.__color = 'white'
    
    @property
    def id(self):
        return self.__id

    @property
    def connected_to(self):
        return self.__connected_to
    
    @property
    def distance(self):
        return self.__distance

    @property
    def predecessor(self):
        return self.__predecessor

    @property
    def color(self):
        return self.__color

    @distance.setter
    def distance(self,new_distance):
        self.__distance = new_distance

    @predecessor.setter
    def predecessor(self,new_predecessor):
        self.__predecessor = new_predecessor

    @color.setter
    def color(self,new_color):
        self.__color = new_color
    
    def addNeighbor(self,nbr,weight=0):
        """Adds neighbor vertex, weight is optional param
        Arguments:
            nbr {Vertex} -- [description]
            weight {int} -- (default: {0})
        """        
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    def getConnections(self):
        """Gets list of all connected vertices
        Returns:
            [List] -- All Ids of connected Vertices
        """        
        return self.connected_to.keys()

    def getId(self):
        """Gets Vertex ID
        Returns:
            [Object] -- Id of current Vertex
        """        
        return self.id

    def getWeight(self,nbr):
        """Gets weight between current and neighbor vertices   
        Arguments:
            nbr {[Vertex]} -- Neighbor Vertex        
        Returns:
            [int] -- weight
        """        
        return self.connected_to[nbr]



