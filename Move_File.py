import os
import shutil

from_dir = "/Users/jaidevkaleeswaran/Downloads"
to_dir = "/Users/jaidevkaleeswaran/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)

    if extension == '':
        continue
    if extension == [ '.txt', '.doc', '.docx' , '.pdf']:
        path1 = from_dir + '/' + name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + name

        if os.path.exists(path2):
            print("Moving" + name + "...")

            shutil.move(path1, path3)
        
        else:
            os.mkdir(path2)
            print("Moving" + name + "...")
            shutil.move(path1, path3)

