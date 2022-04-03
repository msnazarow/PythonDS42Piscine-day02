class Research:
	def file_reader(self) -> str:
		file_name = 'data.csv'
		with open(file_name) as file:
			return file.read()


if __name__ == '__main__':
	print(Research().file_reader())