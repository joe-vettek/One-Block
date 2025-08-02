from mods import kaleidoscope_cookery
from core.provider import *
from core import constant
mod_id = "kaleidoscope_cookery"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 03
loot01 = SingleLootTableBuilder()
loot01.add_entry(SimplePoolEntryBuilder(kaleidoscope_cookery.blocks.lettuce_seed, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="01", table= loot01)


# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(kaleidoscope_cookery.blocks.wild_rice, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 06
loot06 = SingleLootTableBuilder()
loot06.add_entry(SimplePoolEntryBuilder(kaleidoscope_cookery.blocks.chili_seed, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="06", table= loot06)


# 09
loot09 = SingleLootTableBuilder()
loot09.add_entry(SimplePoolEntryBuilder(kaleidoscope_cookery.blocks.tomato_seed, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift, constant.STAGE_FOREST.stage_gift], table_id="09", table= loot09)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage09.add_block(kaleidoscope_cookery.blocks.straw_block, 4)
sub_provider.add_phase("09", stage09)