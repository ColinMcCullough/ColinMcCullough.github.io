from graph import Graph
from cs260.data_structures.ch_three_hw.queue import Queue

def buildGraph(wordFile,length = 4):
    """
    Arguments:
        wordFile {txt file} -- text file of words
        length {int} -- length of word to graph (default: {4})
    
    Returns:
        [Graph] -- build graph
    """    
    d = {}
    graph = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        if len(word) == length:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    graph.addEdge(word1,word2)
    return graph

def breadth_first_search(graph,start):
    """Creates connections between starting word and all
    subsuquent words
    Arguments:
        graph {Graph} -- graph
        start {Vertex} -- starting vertex
    """    
    start.distance = 0
    start.predecessor = None
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for neighbor in currentVert.getConnections():
            if neighbor.color == 'white':
                neighbor.color = 'gray'
                neighbor.distance = currentVert.distance + 1
                neighbor.predecessor = currentVert
                vertQueue.enqueue(neighbor)
        currentVert.color = 'black'

def traverse(final_word):
    """
    Arguments:
        final_word {Vertex} -- Vertex to search back from 
    """    
    while final_word.predecessor:
        print(final_word.getId())
        final_word = final_word.predecessor
    print(final_word.getId())

def show_path(start_word,end_word):
    """Shows path graph takes to get from start_word to end_word
    Arguments:
        start_word {String} -- [description]
        to_word {String} -- [description]
    """    
    graph = buildGraph("c:/Users/Colin McCullough/Desktop/Colin/CS160/Repos/ColinMcCullough.github.io/cs260/data_structures/ch-seven-hw/wordladder.txt",len(start_word))
    breadth_first_search(graph,graph.vertList[start_word])
    traverse(graph.vertList[end_word])

show_path('funny','aaron')