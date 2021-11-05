import tarfile
import time

with tarfile.open('test.tar', 'r') as tar:
    for file_info in tar.getmembers():
        print(file_info.name)
        print("Size: ", file_info.size, 'bytes')
        print("Type: ", file_info.type)
        print()
