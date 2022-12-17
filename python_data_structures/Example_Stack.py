class ExampleStack:
   def __init__(self):
      self.stack = []

   def addElement(self, dataval):
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
        
   def removeElement(self):
      if len(self.stack) <= 0:
         return ("No element is there in the Stack")
      else:
         return self.stack.pop()

Stack = ExampleStack()
Stack.addElement("Jan")
Stack.addElement("Feb")
Stack.addElement("Mar")
Stack.addElement("Apr")
Stack.addElement("May")
print(Stack.removeElement())
print(Stack.removeElement())