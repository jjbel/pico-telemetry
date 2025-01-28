from pathlib import Path
from pprint import pprint

lines = open('sample_data_trimmed1.csv', 'r').read().splitlines()
data = [line.split(',') for line in lines]
data = [(values[9], values[10], values[11], values[12]) for values in data]
data = [[string[:6] for string in row] for row in data]
data = [','.join(values) for values in data]
data = data[:250]
data = '\n'.join(data)

print(data)
Path('sample_data_trimmed2.csv').write_text(data)
