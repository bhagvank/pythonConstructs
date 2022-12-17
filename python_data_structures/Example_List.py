
Example_List = []
print("Initial blank Example_List: ")
print(Example_List)


Example_List.append(1)
Example_List.append(2)
Example_List.append(7)
print("\nExample_List after Addition of Three elements: ")
print(Example_List)


for i in range(1, 4):
	Example_List.append(i)
print("\nExample_List after Addition of elements from 1-3: ")
print(Example_List)


Example_List.append((4, 5))
print("\nExample_List after Addition of a Tuple: ")
print(Example_List)


Example_List2 = ['For', 'JavaCodeGeeks']
Example_List.append(Example_List2)
print("\nExample_List after Addition of a Example_List: ")
print(Example_List)
