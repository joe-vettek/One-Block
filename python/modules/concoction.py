from mods import concoction
from core.provider import *
from core import constant
mod_id = "concoction"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 01
loot01 = SingleLootTableBuilder()
loot01.add_entry(SimplePoolEntryBuilder(concoction.blocks.sunflower_seeds, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_PLAIN.stage_gift], table_id="01", table= loot01)


# 03
loot03 = SingleLootTableBuilder(rolls_min=1, rolls_max=2)
loot03.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_beetroot, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="01", table= loot03)


# 04
loot04 = SingleLootTableBuilder(rolls_min=1, rolls_max=2)
loot04.add_entry(SimplePoolEntryBuilder(concoction.blocks.rice, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 06
loot06 = SingleLootTableBuilder()
loot06.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_cabbage, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_carrot, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_onion, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_spicy_pepper, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift], table_id="06", table= loot06)


# 07
loot07 = SingleLootTableBuilder(rolls_min=1, rolls_max=2)
loot07.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_cotton, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="07", table= loot07)

# 08
loot08 = SingleLootTableBuilder(rolls_min=1, rolls_max=2)
loot08.add_entry(SimplePoolEntryBuilder(concoction.blocks.reapper_seeds, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_NETHER.stage_gift], table_id="08", table= loot08)


# 09
loot09 = SingleLootTableBuilder(rolls_min=1, rolls_max=2)
loot09.add_entry(SimplePoolEntryBuilder(concoction.blocks.sunflower_seeds, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_tomato, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift], table_id="09", table= loot09)


# 10
loot10 = SingleLootTableBuilder(rolls_min=1, rolls_max=2)
loot10.add_entry(SimplePoolEntryBuilder(concoction.blocks.corn_seeds, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(concoction.blocks.wild_potato, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)
