# import json
# import os
# from os.path import exists, join
#
# from core import util, constant
#
# base_path = "IconRendererOutput2"
# check_path = "mods"
# see_path = "modules"
# map = {}
#
#
# def add_key(d: dict, key):
#     if d.get(key) is None:
#         d[key] = {}
#
#
# if __name__ == '__main__':
#
#     for i in util.readDir(base_path):
#         # file_id = util.get_file_name(i)
#         # if file_id.endswith('_entity'):
#         #     file_id = file_id[:-len('_entity')]
#         a = util.get_multi_json(i)
#         for item in a:
#             registerName: str = item["registerName"].replace(":entities/", ":").split(':')
#             type = item["type"]
#             mod = registerName[0]
#             name = registerName[1]
#             add_key(map, mod)
#             add_key(map[mod], type)
#             try:
#                 # comment = f'[{item["CreativeTabName"]}] ' if item.get('CreativeTabName') is not  None else ''
#                 comment = item["englishName"] \
#                     if item["name"] == item["englishName"] \
#                     else item["name"] + ' ' + item["englishName"]
#             except:
#                 comment = item["name"]
#
#             map[mod][type][name] = {'name': ':'.join(registerName)}
#
#             # map[mod] = registerName[1]
#
#     for i in util.readDir(see_path):
#         txt = util.get_text(i)
#         mods=[]
#         for m in map:
#             for type in map[m]:
#                 cc = f'{type.lower()}s'.replace("entitys", "entities")
#                 for name in map[m][type]:
#                     id = f'"{map[m][type][name]["name"]}"'
#                     if id in txt:
#                         txt = txt.replace(id, f'{m}.{cc}.{name}')
#                         mods.append(m)
#
#
#         if len(mods)>0:
#             mods=set(mods)
#             for m in mods:
#                 txt=f"from mods import {m}\n"+txt
#             # print(txt)
#
#         util.save_text(i,txt)
#     # print(map)
