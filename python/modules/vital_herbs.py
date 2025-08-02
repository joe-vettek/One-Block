from mods import vital_herbs
from core.provider import *
from core import constant
mod_id = "vital_herbs"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)


# 03
loot03 = SingleLootTableBuilder()
loot03.add_entry(SimplePoolEntryBuilder(vital_herbs.items.frost_mint, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="01", table= loot03)


# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(vital_herbs.items.fizz_fruit, weight=6).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(vital_herbs.items.tox_kiss, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)

# 05
loot05 = SingleLootTableBuilder()
loot05.add_entry(SimplePoolEntryBuilder(vital_herbs.items.blue_spar, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="05", table= loot05)

# 06
loot06 = SingleLootTableBuilder()
loot06.add_entry(SimplePoolEntryBuilder(vital_herbs.items.bleeding_heart, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(vital_herbs.items.glow_leaf, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(vital_herbs.items.needle_heart, weight=6).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(vital_herbs.items.razor_leaf, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift], table_id="06", table= loot06)

# 07
loot07 = SingleLootTableBuilder()
loot07.add_entry(SimplePoolEntryBuilder(vital_herbs.items.iron_root, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="07", table= loot07)


# 08
loot08 = SingleLootTableBuilder()
loot08.add_entry(SimplePoolEntryBuilder(vital_herbs.items.burst_bud, weight=6).add_count_function(1, 2))
loot08.add_entry(SimplePoolEntryBuilder(vital_herbs.items.mourning_bloom, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_NETHER.stage_gift], table_id="08", table= loot08)

# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(SimplePoolEntryBuilder(vital_herbs.items.crimson_lily, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(vital_herbs.items.sooth_blossom, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)

# 13
loot13 = SingleLootTableBuilder()
loot13.add_entry(SimplePoolEntryBuilder(vital_herbs.items.grim_vine, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_END.stage_gift], table_id="13", table= loot13)


# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_UNDERGROUND.get_phase_id())
stage02.add_block(vital_herbs.blocks.aura_crystal_ore, 10)
stage02.add_block(vital_herbs.blocks.green_slate, 6)
sub_provider.add_phase("02", stage02)

# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage08.set_add_count(2)
stage08.add_mob_limit(vital_herbs.entities.wisp, 2,1,0,2)
sub_provider.add_phase("08", stage08)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(vital_herbs.blocks.deepslate_aura_crystal_ore, 10)
stage12.add_block(vital_herbs.blocks.green_slate, 4)
stage12.add_mob_limit(vital_herbs.entities.lichen_mite, 2,2,0,3)
sub_provider.add_phase("12", stage12)

# all
stageall = SubPhaseTableBuilder(target=constant.STAGE_ALL.get_phase_id())
stageall.add_block(vital_herbs.blocks.deepslate_aura_crystal_ore, 10)
sub_provider.add_phase("all", stageall)