class ExampleHashMap:


	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range(self.size)]


	def set_value(self, key, val):
		

		hashed_key = hash(key) % self.size
		

		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break

		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))


	def get_value(self, key):
		

		hashed_key = hash(key) % self.size
		
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break


		if found_key:
			return record_val
		else:
			return "No record is found"


	def delete_value(self, key):
		

		hashed_key = hash(key) % self.size
		

		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return


	def __str__(self):
		return "".join(str(item) for item in self.hash_table)


hash_map = ExampleHashMap(30)

hash_map.set_value('george@gmail.com', 'x1')
print(hash_map)
print()

hash_map.set_value('jack@gmail.com', 'y1')
print(hash_map)
print()

print(hash_map.get_value('jack@gmail.com'))
print()

hash_map.delete_value('jack@gmail.com')
print(hash_map)
