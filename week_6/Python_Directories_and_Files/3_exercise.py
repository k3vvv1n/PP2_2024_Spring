import os

#path = r"C:\pp2\week_4"
#path.replace('\\', '/')

if os.path.exists('C:\pp2\week_4'):
    print("Path exists")
    print("Filename:", os.path.basename('C:\pp2\week_4'))
    print("Directory:", os.path.dirname('C:\pp2\week_4'))
else:
    print("This path doesn't exist")
