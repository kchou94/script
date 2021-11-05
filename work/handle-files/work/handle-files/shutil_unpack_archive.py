import pathlib
import sys
import shutil
import tempfile

with tempfile.TemporaryDirectory() as d:
    shutil.unpack_archive(
        'test.tar.gz', extract_dir='/Users/kchou/Downloads/tmp',)

    prefix_len = len(d) + 1

    for extracted in pathlib.Path(d).rglob('*'):
        print(str(extracted)[prefix_len:])
