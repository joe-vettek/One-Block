from mods import biomesoplenty
from core.provider import *
from core import constant

mod_id = "biomesoplenty"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(biomesoplenty.blocks.fir_log, 5)
stage03.add_block(biomesoplenty.blocks.redwood_log, 5)
# stage03.add_block(biomesoplenty.blocks.rainbow_birch_sapling, 5)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(biomesoplenty.blocks.willow_log, 10)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(biomesoplenty.blocks.palm_log, 10)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(biomesoplenty.blocks.mahogany_log, 10)
# stage06.add_block(biomesoplenty.blocks.maple_sapling, 10)
# stage06.add_block(biomesoplenty.blocks.orange_autumn_sapling, 10)
# stage06.add_block(biomesoplenty.blocks.yellow_autumn_sapling, 10)
sub_provider.add_phase("06", stage06)

# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage08.add_block(biomesoplenty.blocks.hellbark_log, 8)
sub_provider.add_phase("08", stage08)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
# stage09.add_block(biomesoplenty.blocks.flowering_oak_sapling, 14)
sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(biomesoplenty.blocks.jacaranda_log, 10)
sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_block(biomesoplenty.blocks.umbran_log, 8)
stage11.add_block(biomesoplenty.blocks.magic_log, 8)
stage11.add_block(biomesoplenty.blocks.dead_log, 8)
sub_provider.add_phase("11", stage11)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(biomesoplenty.blocks.origin_grass_block, 5)
# stage12.add_block(biomesoplenty.blocks.origin_sapling, 8)
sub_provider.add_phase("12", stage12)

# forest
loot_forest = LootTableBuilder()
loot_forest_pool_sapling = LootPoolBuilder(CountBuilder(1, 2))
loot_forest_pool_sapling.add_entry_item(biomesoplenty.blocks.mahogany_sapling, weight=4, min=1, max=2)
loot_forest_pool_sapling.add_entry_item(biomesoplenty.blocks.maple_sapling, weight=4, min=1, max=2)
loot_forest_pool_sapling.add_entry_item(biomesoplenty.blocks.yellow_autumn_sapling, weight=4, min=1, max=2)
loot_forest_pool_sapling.add_entry_item(biomesoplenty.blocks.orange_autumn_sapling, weight=4, min=1, max=2)

loot_forest.add_pool(loot_forest_pool_sapling)
loot_forest_pool_flower = LootPoolBuilder(CountBuilder(0, 1))
loot_forest_pool_sapling.add_entry_item(biomesoplenty.blocks.sprout, weight=4, min=1, max=2)
loot_forest.add_pool(loot_forest_pool_flower)
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift],
                                table_id=constant.STAGE_FOREST.id, table=loot_forest)
