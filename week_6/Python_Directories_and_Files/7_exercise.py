# import shutil 

# shutil.copy('4.txt', '7.txt')

with open('4.txt', 'r') as f1:
    with open('7.txt', 'w') as f2:
        f2.write(f1.read())
        