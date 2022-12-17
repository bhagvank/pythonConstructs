
Example_Tuple1 = (3, 'Hello', 4, 'Java Code Geeks')
print("\nTuple with combination of different Datatypes: ")
print(Example_Tuple1)

Example_Tuple1 = (2, 1, 4, 7)
Example_Tuple2 = ('java', 'java code geek')
Example_Tuple3 = (Example_Tuple1, Example_Tuple2)
print("\nTuple which is nested tuples: ")
print(Example_Tuple3)

Example_Tuple1 = ('Java Code Geeks',) * 4
print("\nTuple after 4 repetitions: ")
print(Example_Tuple1)

Example_Tuple1 = ('Java Code Geeks')
n = 7
print("\nTuple consisting of elements in a loop")
for i in range(int(n)):
	Example_Tuple1 = (Example_Tuple1,)
	print(Example_Tuple1)
