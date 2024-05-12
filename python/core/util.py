import json
import os
import time


def save_json(path, js, make_dirs=False, replace_anyway=False):
    if make_dirs:
        create_dir(os.path.dirname(path))
    if not replace_anyway and os.path.isfile(path):
        if get_text(path) == json.dumps(js, ensure_ascii=False, indent=2):
            # print("skip for ", path)
            pass
    with open(path, "w", encoding="utf-8") as f:
        json.dump(js, f, ensure_ascii=False, indent=2)


def save_text(path, py_text, make_dirs=False, replace_anyway=False):
    if make_dirs:
        create_dir(os.path.dirname(path))
    if not replace_anyway:
        if get_text(path) == py_text:
            # print("skip for ", path)
            pass
    with open(path, "w", encoding="utf-8") as f:
        f.write(py_text)


def get_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def copy_json(js):
    return json.loads(json.dumps(js))


def stanard_path(path):
    return os.path.realpath(os.path.normpath(path))


def readDir(dirPath, filter=None):
    dirPath = stanard_path(dirPath)
    allFiles = []
    __readDir__(dirPath, allFiles)
    return allFiles if filter is None else [i for i in allFiles if i.endswith(filter) or i.endswith(filter.upper())]


def __readDir__(dirPath, allFiles):
    if len(dirPath) == 0:
        return
    if dirPath[-1] == '/':
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
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)


def is_basic_type(var):
    basic_types = (int, float, bool, str, bytes, type(None))
    return isinstance(var, basic_types)


def is_convertible_to_list(var):
    try:
        list(var)
        return True
    except TypeError:
        return False


def is_function(var):
    basic_types = (int, float, bool, str, bytes, type(None))
    return isinstance(var, basic_types)


def to_dict(self):
    if not is_basic_type(self):
        result = {}
        for d in [s for s in dir(self) if not s.startswith("__")]:
            var = getattr(self, d)
            if not is_basic_type(var) and is_convertible_to_list(var):
                result[d] = []
                for v in list(var):
                    result[d].append(to_dict(v))
            elif not callable(var):
                result[d] = var
    else:
        result = self
    return result


def num(i):
    return str(i) if i > 9 else f"0{i}"


def test_time(func):
    def wrapper(*agrs):
        start = time.time()
        result = func(*agrs)
        end = time.time()
        print(f"Cost time: {int((end - start) * 1000)} ms")
        return result

    return wrapper
