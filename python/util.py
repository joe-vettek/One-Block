import json
import os


def save_json(path, js):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(js, f, ensure_ascii=False, indent=2)


def get_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def copy_json(js):
    return json.loads(json.dumps(js))


def readDir(dirPath, filter=None):
    allFiles = []
    __readDir__(dirPath, allFiles)
    return allFiles if filter is None else [i for i in allFiles if i.endswith(filter) or i.endswith(filter.upper())]


def __readDir__(dirPath, allFiles):
    if len(dirPath) == 0:
        print(u'不能为空')
        return
    if dirPath[-1] == '/':
        print(u'文件夹路径末尾不能加/')
        return
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            __readDir__(dirPath + "\\" + f, allFiles)
            # allFiles.append(f)
        return
    else:
        allFiles.append(dirPath)


def create_dir(base_path):
    try:
        os.makedirs(base_path)
    except:
        pass


def delete_dirs(path):
    while os.listdir(path):
        delete_dirs(os.path.join(path,os.listdir(path)[0]))
    os.remove(path)
