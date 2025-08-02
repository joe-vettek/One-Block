import json
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
    for i in util.readDir(base_path):
        # file_id = util.get_file_name(i)
        # if file_id.endswith('_entity'):
        #     file_id = file_id[:-len('_entity')]
        a = util.get_multi_json(i)
        for item in a:
            registerName: str = (item["registerName"].replace(":entities/", ":")
                                 .replace("ResourceKey[minecraft:loot_table / ","").replace("]","")
                                 .split(':'))
            type = item["type"]
            mod = registerName[0]
            name = registerName[1].replace("/", "_")
            # skip with mod gennerate
            if "/" in registerName[1]:
                continue
            add_key(map, mod)
            add_key(map[mod], type)
            try:
                # comment = f'[{item["CreativeTabName"]}] ' if item.get('CreativeTabName') is not  None else ''
                comment = item["englishName"] \
                    if item["name"] == item["englishName"] \
                    else item["name"] + ' ' + item["englishName"]
            except:
                comment = item["name"]

            map[mod][type][name] = {'name': (':'.join(registerName)),
                                    'comment': f'# {comment}',
                                    'tags': json.loads(
                                        '["' + item["OredictList"].replace(",", '","')[1:-1] + '"]') if item.get(
                                        "OredictList") is not None else None,
                                    'nbt': None,
                                    }

            # map[mod] = registerName[1]

    for m in map:
        text = f'# {m}\n'
        text += f'from core.api import RegisterEntry,Collections\n'
        ooo = []
        for j in map[m]:
            text += f'\n\nclass {j}(Collections):'
            for c in map[m][j]:
                text += f'\n    {map[m][j][c]["comment"]}'
                text += f'\n    {c} = RegisterEntry("{map[m][j][c]["name"]}")'
            cc = f'{j.lower()}s'.replace("entitys", "entities")
            ooo.append(f'\n{cc} = {j}()')
        text += f"\n\n{''.join(ooo)}"
        with open(f'{outpath}/{m}.py', 'w', encoding='utf-8') as f:
            f.write(text)

    # print(map)
