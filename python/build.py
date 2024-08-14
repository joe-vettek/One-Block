# Not need to change it

import os
from core import util, provider


def dynamic_import(file_path, runs):
    with open(file_path, 'r') as file:
        code = file.read()
    code += "\nruns.extend(run_list)"
    print(file_path)
    exec(code)


provider.root = "../src/main/resources/datapacks"
if __name__ == '__main__':
    # util.delete_dirs(provider.root)
    old=util.readDir(provider.root)
    run_list = []
    for p in os.listdir('modules'):
        dynamic_import(f'modules/{p}', run_list)

    for r in run_list:
        r.run()

    print("\n")
    for o in old:
        if o not in provider.use_path:
            os.remove(o)
            print("Remove",o)

    print("finished")


