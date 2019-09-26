import os


def get_all_files(dir):
    files_ = []
    list = [i for i in os.listdir(dir)]
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if not os.path.isdir(path):
            files_.append(path)
    return files_
