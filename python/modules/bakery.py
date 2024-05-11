from core.provider import *
from core import constant

mod_id = "bakery"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)
# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(PoolEntryBuilder("bakery:strawberry_seeds", weight=6).add_count_function(1, 2))
loot10.add_entry(PoolEntryBuilder("bakery:oat_seeds", weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table=loot10)
