class Calculator:

      def __init__(self):
      	self.data = []

      def sum(self,int1,int2):

	      self.data.append(int1);
	      self.data.append(int2);
	      return int1+int2;


def random(intarr1):
	from random import randint
	rand = randint(0,len(intaar1)-1)
	output = intarr1[rand]
	return output
print("executing main")

calculator = Calculator()

sum = calculator.sum(3,4)

print(str(sum))