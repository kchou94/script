import shutil
import os
import tarfile

print('creating archive')
shutil.make_archive('test', 'tar', root_dir='..', base_dir='handle-files',)

print('\nArchive contents:')
with tarfile.open('test.tar', 'r') as tar:
    for names in tar.getnames():
        print(names)

os.system('touch test.txt')
print('adding test.txt')
with tarfile.open('test.tar', mode='a') as tar:
    tar.add('test.txt')

print('contents:',)
with tarfile.open('test.tar', 'r') as tar:
    print([names for names in tar.getnames()])
