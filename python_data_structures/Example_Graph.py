class ExampleGraph:
   def __init__(self,graphdict=None):
      if graphdict is None:
         graphdict = {}
      self.graphdict = graphdict
   def getPoints(self):
      return list(self.graphdict.keys())
      
   def addPoint(self, point):
      if point not in self.graphdict:
         self.graphdict[point] = []

egraph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"],
   "f" : ["e"]
}
graph = ExampleGraph(egraph_elements)
graph.addPoint("g")
print(graph.getPoints())