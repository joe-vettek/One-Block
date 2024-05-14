# just for simple case
import os
from os.path import exists, join

from core import util, constant

base_path = "../src/main/resources/data"

# if __name__ == '__main__':
#     pass
#     for d in os.listdir(base_path):
#         # mod_id = d.split("-")[-1]
#         mod_id=d
#         print(mod_id)
#         out_path = f"output/{mod_id}.py"
#
#         py_text = f'from core.provider import *\nfrom core import constant'
#         py_text += f'\nmod_id = "{mod_id}"\nrun_list = []\n\nrun_list.append(DataPackProvider(mod_id))'
#
#         phases_path = f'{base_path}/{mod_id}/oneblock/phases'
#         if exists(phases_path):
#             py_text += "\n"
#             py_text += f'\nsub_provider=PhaseProvider(mod_id)\nrun_list.append(sub_provider)'
#             for p in os.listdir(phases_path):
#                 py_text += f"\n\n# {p.split('.')[0]}"
#                 j = util.get_json(join(phases_path, p))
#                 stage_name = "stage" + p.split(".")[0]
#                 py_text += f'\n{stage_name} = PhaseTableBuilder(count={j["count"]},end_gift="{j.get("end_gift")}")'
#                 for l in j["list"]:
#                     try:
#                         if l["type"] == constant.TYPE_BLOCK:
#                             py_text += f'\n{stage_name}.add_block("{l["id"]}", {l["weight"]})'
#                         elif l["type"] == constant.TYPE_MOB:
#                             py_text += f'\n{stage_name}.add_mob("{l["id"]}", {l["weight"]}, {l["count"]})'
#                     except:
#                         print(l)
#                 py_text += f'\nsub_provider.add_phase("{p.split(".")[0]}", {stage_name})'
#                 py_text += "\n"
#
#         loot_path = f'{base_path}/{mod_id}/loot_tables'
#         if exists(loot_path) and mod_id !="ija-one-block":
#             py_text += "\n"
#             py_text += f'\nloot_provider = ModifiedLootTableProvider(mod_id)\nrun_list.append(loot_provider)'
#             for p in os.listdir(loot_path):
#                 py_text += f"\n\n# {p.split('.')[0]}"
#                 j = util.get_json(join(loot_path, p))
#                 loot_name = ("loot" + p.split(".")[0]).replace("-","_")
#                 py_text += f'\n{loot_name} = SingleLootTableBuilder()'
#                 for l in j["pools"][0]["entries"]:
#                     min = l["functions"][0]["count"]["min"]
#                     max = l["functions"][0]["count"]["max"]
#                     py_text += f'\n{loot_name}.add_entry(PoolEntryBuilder("{l["name"]}", weight={l["weight"]}).add_count_function({min}, {max}))'
#                 py_text += f'\nloot_provider.add_modified_loot(target=[constant.{constant.get_stage_by_sid(p.split("-")[0].split(".")[0])}.stage_gift], table_id="{p.split(".")[0]}", table= {loot_name})'
#                 py_text += "\n"
#         elif exists(loot_path):
#             py_text += "\n"
#             py_text += f'\nloot_provider = LootTableProvider(mod_id)\nrun_list.append(loot_provider)'
#             for p in os.listdir(loot_path):
#                 py_text += f"\n\n# {p.split('.')[0]}"
#                 j = util.get_json(join(loot_path, p))
#                 loot_name = ("loot" + p.split(".")[0]).replace("-","_")
#                 py_text += f'\n{loot_name} = SingleLootTableBuilder()'
#                 for l in j["pools"][0]["entries"]:
#                     min = l["functions"][0]["count"]["min"]
#                     max = l["functions"][0]["count"]["max"]
#                     py_text += f'\n{loot_name}.add_entry(PoolEntryBuilder("{l["name"]}", weight={l["weight"]}).add_count_function({min}, {max}))'
#                 py_text += f'\nloot_provider.add_loot( table_id="{p.split(".")[0]}", table= {loot_name})'
#                 py_text += "\n"
#         util.save_text(out_path, py_text, True)
