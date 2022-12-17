class ExampleNode:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class ExampleLinkedList:
   def __init__(self):
      self.headval = None

   def printList(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
   def AddAtStart(self,newdata):
      NewNode = ExampleNode(newdata)
      NewNode.nextval = self.headval
      self.headval = NewNode

list = ExampleLinkedList()
list.headval = ExampleNode("Jan")
enode2 = ExampleNode("Feb")
enode3 = ExampleNode("Mar")

list.headval.nextval = enode2
enode2.nextval = enode3

list.AddAtStart("Dec")
list.printList()