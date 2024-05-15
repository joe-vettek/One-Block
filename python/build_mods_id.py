import os
from os.path import exists, join

from core import util, constant

base_path = "IconRendererOutput2"
outpath = "mods"

map = {}


def add_key(d: dict, key):
    if d.get(key) is None:
        d[key] = {}


if __name__ == '__main__':
    util.delete_dirs(outpath)
    for i in util.readDir(base_path):
        # file_id = util.get_file_name(i)
        # if file_id.endswith('_entity'):
        #     file_id = file_id[:-len('_entity')]
        a = util.get_multi_json(i)
        for item in a:
            registerName: str = item["registerName"].replace(":entities/",":").split(':')
            type=item["type"]
            mod = registerName[0]
            name=registerName[1]
            add_key(map,mod)
            add_key(map[mod],type)
            try:
                comment=item["englishName"] \
                    if item["name"] ==item["englishName"] \
                    else item["name"]+' '+item["englishName"]
            except:
                comment=item["name"]
            map[mod][type][name]= {'name':':'.join(registerName),
                                   'comment':f'# {comment}'}
            # map[mod] = registerName[1]

    for m in map:
        text=f'# {m}\n'
        for j in map[m]:
            text+=f'\n\nclass {j}s:'
            for c in map[m][j]:
                text+=f'\n    {map[m][j][c]["comment"]}'
                text+=f'\n    {c} = "{map[m][j][c]["name"]}"'

        with open(f'{outpath}/{m}.py','w',encoding='utf-8') as f:
            f.write(text)


    # print(map)
