class ExampleNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insertNode(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = ExampleNode(data)
            else:
               self.left.insertNode(data)
         elif data > self.data:
               if self.right is None:
                  self.right = ExampleNode(data)
               else:
                  self.right.insertNode(data)
         else:
              self.data = data
   def findbyvalue(self, lkpval):
      if lkpval < self.data:
         if self.left is None:
            return str(lkpval)+" element Not Found"
         return self.left.findbyvalue(lkpval)
      elif lkpval > self.data:
            if self.right is None:
               return str(lkpval)+"element Not Found"
            return self.right.findbyvalue(lkpval)
      else:
            print(str(self.data) + ' is found here')

   def PrintExampleTree(self):
      if self.left:
         self.left.PrintExampleTree()
      print( self.data),
      if self.right:
         self.right.PrintExampleTree()
rootNode = ExampleNode(2)
rootNode.insertNode(7)
rootNode.insertNode(15)
rootNode.insertNode(4)
print(rootNode.findbyvalue(5))
print(rootNode.findbyvalue(15))