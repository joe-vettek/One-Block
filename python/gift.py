import os
from core import util

base_path = "cache"

# loot_provider.add_loot(table_id="00-gift", table=LootTableBuilder()

for i in os.listdir((base_path)):
    if not "gift" in i:
        path = f"{base_path}/{i}"
        js = util.get_json(path)
        name = i.split(".")[0]
        print(f"\n# {name}")
        print(f"{name}= LootTableBuilder()")
        print(f'loot_provider.add_loot(table_id="{name}", table={name})')
        count=0
        for c in js["pools"]:
            count+=1
            LootPoolBuildername=f"lootbuilder_{name}_"+str(count)
            print(f'{LootPoolBuildername}=LootPoolBuilder(CountBuilder({c["rolls"]["min"]}, {c["rolls"]["max"]}),CountBuilder({c["bonus_rolls"]["min"]}, {c["bonus_rolls"]["max"]}))')
            for j in c["entries"]:
                if len(j["functions"])==1:
                    print(f'{LootPoolBuildername}.add_entry_item("{j["name"]}", 1, {j["functions"][0]["count"]["min"]}, {j["functions"][0]["count"]["max"]})')
                else:
                    try:
                        print(f'{LootPoolBuildername}.add_entry_item("{j["name"]}", 1, {j["functions"][0]["count"]["min"]}, {j["functions"][0]["count"]["max"]}, {j["functions"][1]["tag"]})')
                    except:
                        print(f'{LootPoolBuildername}.add_entry_item("{j["name"]}", 1, {j["functions"][0]["count"]["min"]}, {j["functions"][0]["count"]["max"]}, tag=None,enchantments={j["functions"][1]["enchantments"]})')
            print(f'musical.add_pool({LootPoolBuildername})\n')
