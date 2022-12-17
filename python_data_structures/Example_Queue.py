class ExampleQueue:
   def __init__(self):
      self.queue = list()

   def addtoqueue(self,dataval):
      if dataval not in self.queue:
       self.queue.insert(0,dataval)
       return True
      return False

   def removefromqueue(self):
      if len(self.queue)>0:
         return self.queue.pop()
      return ("No elements are there in Queue!")

Queue = ExampleQueue()
Queue.addtoqueue("Jack")
Queue.addtoqueue("George")
Queue.addtoqueue("John")
Queue.addtoqueue("Kate")
print(Queue.removefromqueue())
print(Queue.removefromqueue())