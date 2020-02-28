import os
import search
from shutil import copyfile



#-------------------------------------------------------------------------------------------

source = "Please Enter Source Path Here, Remember to Escape Special Characters!"
destination = "Please Enter Destination Path Here, Remember to Escape Special Characters!"

#-------------------------------------------------------------------------------------------


needed_list = []
needed_list = search.search(source, needed_list, ".pdf")
for l in needed_list:
    copyfile(l, os.path.join(destination, os.path.basename(l)))
