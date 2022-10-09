from distutils import extension
import os
import shutil

from_dir="C:/Users/vpkarmani/Downloads"
to_dir="C:/Users/vpkarmani/Dekstop/Document_files"

list_of_files =os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name,extension=os.path.splitext(file_name)
    