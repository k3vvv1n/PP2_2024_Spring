import os

path = r'C:\pp2\week_6\Python_Directories_and_Files\4.txt'

with open(path, 'r') as a:  
    lines = a.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))