from mods import teastory
from core.provider import *
from core import constant
mod_id = "teastory"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 01
loot01 = SingleLootTableBuilder()
loot01.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_cucumber, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_PLAIN.stage_gift], table_id="01", table= loot01)


# 03
loot03 = SingleLootTableBuilder()
loot03.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_chinese_cabbage, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="01", table= loot03)


# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_rice, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 06
loot06 = SingleLootTableBuilder()
loot06.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_tea_plant, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_chili, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_grape, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_bitter_gourd, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift], table_id="06", table= loot06)


# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(SimplePoolEntryBuilder(teastory.blocks.wild_tea_plant, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)
