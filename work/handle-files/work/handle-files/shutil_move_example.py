import shutil

# change path
shutil.move('/Users/kchou/Downloads/sample.txt',
            '/Users/kchou/Downloads/tmp1/sample.txt')

# rename
shutil.move('sample.txt', 'sample_renamed.txt')
