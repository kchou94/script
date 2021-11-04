import os

directory_name = 'test'
print('Creating', directory_name)
os.makedirs(directory_name)

file_name = os.path.join(directory_name, 'test.txt')
print('Creating', file_name)
with open(file_name, 'wt') as f:
    f.write('test file')

print('Cleaning up')
os.unlink(path=file_name)
os.rmdir(path=directory_name)
