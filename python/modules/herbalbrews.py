from core.provider import *
from core import constant
mod_id = "herbalbrews"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 06
loot06 = SingleLootTableBuilder()
loot06.add_entry(PoolEntryBuilder("herbalbrews:wild_coffee_plant", weight=6).add_count_function(2, 4))
loot06.add_entry(PoolEntryBuilder("herbalbrews:wild_yerba_mate_plant", weight=6).add_count_function(2, 4))
loot06.add_entry(PoolEntryBuilder("herbalbrews:hibiscus", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift], table_id="06", table= loot06)


# 07
loot07 = SingleLootTableBuilder()
loot07.add_entry(PoolEntryBuilder("herbalbrews:wild_rooibos_plant", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="07", table= loot07)


# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(PoolEntryBuilder("herbalbrews:lavender", weight=6).add_count_function(2, 4))
loot10.add_entry(PoolEntryBuilder("herbalbrews:tea_blossom", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)
