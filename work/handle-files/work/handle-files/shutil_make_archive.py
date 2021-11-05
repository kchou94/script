import tarfile
import shutil
import sys

shutil.make_archive('test', 'gztar', root_dir='..', base_dir='handle-files')

print('Archive contents:')
with tarfile.open('test.tar.gz', 'r:gz') as tar:
    for names in tar.getnames():
        print(names)
