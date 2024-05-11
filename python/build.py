# Not need to change it

import os
from core import util


def dynamic_import(file_path, runs):
    with open(file_path, 'r') as file:
        code = file.read()
    code += "\nruns.extend(run_list)"
    exec(code)


if __name__ == '__main__':
    util.delete_dirs('datapacks')

    run_list = []
    for p in os.listdir('modules'):
        dynamic_import(f'modules/{p}', run_list)

    for r in run_list:
        r.run()

    print("\nfinished")