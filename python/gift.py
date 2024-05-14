import os
from core import util

base_path = "../src/main/resources/data/oneblock/loot_tables"

# loot_provider.add_loot(table_id="00-gift", table=LootTableBuilder()

for i in os.listdir((base_path)):
    if "gift" in i:
        path = f"{base_path}/{i}"
        js = util.get_json(path)
        name = i.split(".")[0]
        print(f"\n# {name}")
        print(f'loot_provider.add_loot(table_id="{name}", table=LootTableBuilder()')
        for c in js["pools"]:
            j=c["entries"][0]
            print(f'.add_pool(LootPoolBuilder(CountBuilder(1, 1),CountBuilder(0, 0)).add_entry_item("{j["name"]}", 1, {j["functions"][0]["count"]["min"]}, {j["functions"][0]["count"]["max"]}))')

        print(')\n')
