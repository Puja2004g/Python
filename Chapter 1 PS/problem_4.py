# import the required module
import os

# provide the path
path = "/"

# check if the path exists
if os.path.exists(path):
    # list the items of the directory
    for items in os.listdir(path):
        print(items)
        
# if path doesn't exists 
else:
    print("Path doesn't exists")