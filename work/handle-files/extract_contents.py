import tarfile
import os

os.mkdir('work')

with tarfile.open('test.tar', 'r') as t:
    t.extractall('work')

print(os.listdir('work'))
