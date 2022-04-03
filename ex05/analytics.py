from random import randint

class Research:
	class Calculations:
		def __init__(self, data: [[int]]):
			self.data = data

		def counts(self):
			heads = 0
			tails = 0
			for line in self.data:
				heads += line[0]
				tails += line[1]
			return heads, tails

		def fractions(self, heads, tails):
			all = heads + tails
			return heads / all, tails / all

	class Analytics(Calculations):
		def _predict_random(self, n: int):
			for i in range(n):
				head = randint(0, 1)
				yield [head, 1 - head]

		def predict_random(self, n: int):
			return list(self._predict_random(n))

		def predict_last(self):
			return self.data[-1]

		def save_file(self, data, file_name, file_extension):
			with open(f"{file_name}.{file_extension}", 'w') as file:
				file.write(data)

	def __init__(self, path: str):
		self.path: str = path

	def file_reader(self, has_header=True) -> [str]:
		with open(self.path) as file:
			data = file.read().strip().split('\n')
			if has_header:
				self.validate_header(data[0].split(','))
			data = list(map(lambda x: list(map(int, x.split(','))), data[1:]))
			self.validate_data(data)
			return data

	def validate_header(self, elems: [str]):
		if len(elems) != 2:
			raise ValueError("Correct header: head,tail")

	def validate_data(self, data):
		for elems in data:
			if len(elems) != 2:
				raise ValueError("Correct line: 1,0")
			if elems[0] == elems[1]:
				raise ValueError("Correct line: 1,0")
			if not (elems[0] in [0, 1] and elems[1] in [0, 1]):
				raise ValueError("Correct line: 1,0")

