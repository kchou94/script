import configparser

p = configparser.ConfigParser()
p.read('read_sample.ini')

print(p.get('bug_tracker', 'url'))
