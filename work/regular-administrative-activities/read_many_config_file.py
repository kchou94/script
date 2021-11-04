import glob
import configparser

p = configparser.ConfigParser()
files = ['hello.ini', 'bye.ini', 'read_sample.ini', 'welcome.ini']
files_found = p.read(files)
files_missing = set(files) - set(files_found)
print('Files found:', sorted(files_found))
print('Files missing:', sorted(files_missing))
