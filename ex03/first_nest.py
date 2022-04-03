import sys


class Research:
	class Calculations:
		def counts(self, data: [[int]]):
			heads = 0
			tails = 0
			for line in data:
				heads += line[0]
				tails += line[1]
			return heads, tails

		def fractions(self, heads, tails):
			all = heads + tails
			return heads / all, tails / all

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


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise AttributeError("Usage: python3 first_constructor.py data.csv")
	reader = Research(sys.argv[1])
	data = reader.file_reader()
	calculations = reader.Calculations()
	print(data)
	heads, tails = calculations.counts(data)
	print(f"{heads} {tails}")
	head_percent, tail_percent = calculations.fractions(heads, tails)
	print(f"{head_percent} {tail_percent}")
