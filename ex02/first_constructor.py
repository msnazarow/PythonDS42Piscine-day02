import sys


class Research:
	def __init__(self, path: str):
		self.path: str = path

	def file_reader(self) -> str:
		with open(self.path) as file:
			data = file.read()
			self.validate(data.strip().split('\n'))
			return data

	def validate(self, data):
		for i, line in enumerate(data):
			if i == 0:
				if len(line.split(',')) != 2:
					raise ValueError("Correct header: head,tail")
			else:
				elems = line.split(',')
				if len(elems) != 2:
					raise ValueError("Correct line: 1,0")
				if elems[0] == elems[1]:
					raise ValueError("Correct line: 1,0")
				if not (elems[0] in ['0', '1'] and elems[1] in ['0', '1']):
					raise ValueError("Correct line: 1,0")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise AttributeError("Usage: python3 first_constructor.py data.csv")
	print(Research(sys.argv[1]).file_reader())
