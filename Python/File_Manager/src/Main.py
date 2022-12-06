import os

# get all list of correct directory
list_dir = os.listdir(".")
list_dir =[each.upper() for each in list_dir]
if len(list_dir) == 1:
    print("This folder looks like Empty")

ext_file = []
folder_name = []
created_folder= {}

# add all file extensions to list
for i in list_dir:
    # check is file or dir
    if os.path.isfile(i):
        # if equal to script name skip
        if i == 'Main.py' or i == "File-Manager.exe":
            continue
        # # split file name to catch extension name
        temp = i.split('.')
        # append extension of file to ext_file list
        ext_file.append(temp[-1])
        # set folder status to 0
        created_folder[temp[-1]] = 0
    else:
        list_dir.remove(i)

# create folder for each type 
for i in ext_file:
    # check if folder create status is false
    if created_folder[i] == 0:
        # added folder created name to folder_name list
        folder_name.append(f"{i}_files")
        # create folder
        os.mkdir(f"{i}_files")
        # set status of folder created to 1
        created_folder[i] = 1

# move files to each folder
for each in list_dir:
    temp = each.split(".")
    # if file is create while program run or 
    # create not folder to file name skip it 
    if temp[-1] not in ext_file:
        continue
    os.rename(each,f"./{temp[-1]}_files/{each}")
