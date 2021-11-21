import os
import shutil 

source=input('enter source folder name')
dest=input('enter dest folder name')
source=source+'/'
dest=dest+'/'
list=os.listdir(source)
for i in list:
    shutil.copy((source+i),dest)
    1