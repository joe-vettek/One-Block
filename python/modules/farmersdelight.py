from mods import farmersdelight
from core.provider import *
from core import constant
mod_id = "farmersdelight"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
loot03 = SingleLootTableBuilder()
loot03.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_potatoes, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="03", table= loot03)


# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_rice, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 05
loot05 = SingleLootTableBuilder()
loot05.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_beetroots, weight=6).add_count_function(1, 2))
loot05.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_cabbages, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="05", table= loot05)


# 07
loot07 = SingleLootTableBuilder()
loot07.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_tomatoes, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="07", table= loot07)


# 09
loot09 = SingleLootTableBuilder()
loot09.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_carrots, weight=6).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(farmersdelight.blocks.wild_onions, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift, constant.STAGE_FOREST.stage_gift], table_id="09", table= loot09)
