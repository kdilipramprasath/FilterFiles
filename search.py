import os

def search(directory_path, needed_list, extension):
    directory_list = os.listdir(directory_path)
    for direct in directory_list:
        temp = os.path.join(directory_path, direct)
        if os.path.isdir(temp):
            search(temp, needed_list, extension)
        else:
            ext = os.path.splitext(direct)[1]
            if ext == extension:
                needed_list.append(temp)
    return needed_list




