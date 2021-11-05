import glob

file_match = glob.glob('*.txt')
print(file_match)

file_match = glob.glob('[0-9].py')
print(file_match)

file_match = glob.glob('**/*.py', recursive=True)
print(file_match)

file_match = glob.glob('**/', recursive=True)
print(file_match)
