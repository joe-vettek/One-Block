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
stage05.add_block(biomesoplenty.blocks.white_sand, 5)
stage05.add_block(biomesoplenty.blocks.white_sandstone, 5)
stage05.add_block(biomesoplenty.blocks.dried_salt, 5)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(biomesoplenty.blocks.mahogany_log, 10)
# stage06.add_block(biomesoplenty.blocks.maple_sapling, 10)
# stage06.add_block(biomesoplenty.blocks.orange_autumn_sapling, 10)
# stage06.add_block(biomesoplenty.blocks.yellow_autumn_sapling, 10)
sub_provider.add_phase("06", stage06)

# 07
stage06 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage06.add_block(biomesoplenty.blocks.orange_sand, 5)
stage06.add_block(biomesoplenty.blocks.orange_sandstone, 5)
sub_provider.add_phase("06", stage06)

# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage08.add_block(biomesoplenty.blocks.hellbark_log, 8)
stage08.add_block(biomesoplenty.blocks.porous_flesh, 8)
stage08.add_block(biomesoplenty.blocks.rose_quartz_block, 8)
stage08.add_block(biomesoplenty.blocks.brimstone, 8)
sub_provider.add_phase("08", stage08)

# # 09
# stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
# # stage09.add_block(biomesoplenty.blocks.flowering_oak_sapling, 14)
# sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(biomesoplenty.blocks.jacaranda_log, 10)
stage10.add_block(biomesoplenty.blocks.black_sand, 5)
stage10.add_block(biomesoplenty.blocks.black_sandstone, 5)
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
stage12.add_block(biomesoplenty.blocks.glowing_moss_block, 4)
stage12.add_block(biomesoplenty.blocks.glowing_moss_block, 4)
stage12.add_block(biomesoplenty.blocks.spider_egg, 1)
# stage12.add_block(biomesoplenty.blocks.origin_sapling, 8)
sub_provider.add_phase("12", stage12)

# 01
loot01 = MultiPoolLootTableBuilder()
loot01.create_new_pool(0, 1)
loot01.add_entry(PoolEntryBuilder(biomesoplenty.blocks.toadstool, weight=4).add_count_function(1, 1))
loot01.add_entry(PoolEntryBuilder(biomesoplenty.blocks.rose, weight=2).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_PLAIN.stage_gift],
                                table_id=constant.STAGE_PLAIN.id, table=loot01)

# 02
loot02 = MultiPoolLootTableBuilder()
loot02.create_new_pool(0, 1)
loot02.add_entry(PoolEntryBuilder(biomesoplenty.blocks.webbing, weight=4).add_count_function(1, 1))
loot02.add_entry(PoolEntryBuilder(biomesoplenty.blocks.stringy_cobweb, weight=2).add_count_function(1, 1))
loot02.add_entry(PoolEntryBuilder(biomesoplenty.blocks.hanging_cobweb, weight=2).add_count_function(1, 1))
loot02.add_entry(PoolEntryBuilder(biomesoplenty.blocks.glowworm_silk, weight=2).add_count_function(1, 1))

loot_provider.add_modified_loot(target=[constant.STAGE_PLAIN.stage_gift],
                                table_id=constant.STAGE_PLAIN.id, table=loot02)

# 03
loot03 = MultiPoolLootTableBuilder()
loot03.create_new_pool(1, 2)
loot03.add_entry(PoolEntryBuilder(biomesoplenty.blocks.fir_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(PoolEntryBuilder(biomesoplenty.blocks.redwood_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(PoolEntryBuilder(biomesoplenty.blocks.rainbow_birch_sapling, weight=4).add_count_function(1, 1))
loot03.create_new_pool(0, 1)
loot03.add_entry(PoolEntryBuilder(biomesoplenty.blocks.toadstool, weight=4).add_count_function(1, 2))
loot03.add_entry(PoolEntryBuilder(biomesoplenty.blocks.violet, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift],
                                table_id=constant.STAGE_COLD.id, table=loot03)

# 04
loot04 = MultiPoolLootTableBuilder()
loot04.create_new_pool(1, 2)
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.willow_sapling, weight=4).add_count_function(1, 2))
loot04.create_new_pool(1, 2)
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.waterlily, weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.huge_lily_pad, weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.reed, weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.pink_daffodil, weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.cattail, weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder(biomesoplenty.blocks.willow_vine, weight=2).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift],
                                table_id=constant.STAGE_SWAMP.id, table=loot04)
# 05
loot05 = MultiPoolLootTableBuilder()
loot05.create_new_pool(1, 2)
loot05.add_entry(PoolEntryBuilder(biomesoplenty.blocks.palm_sapling, weight=4).add_count_function(1, 2))
loot05.create_new_pool(0, 1)
loot05.add_entry(PoolEntryBuilder(biomesoplenty.blocks.watergrass, weight=4).add_count_function(1, 2))
loot05.add_entry(PoolEntryBuilder(biomesoplenty.blocks.dune_grass, weight=4).add_count_function(1, 2))
loot05.add_entry(PoolEntryBuilder(biomesoplenty.blocks.pink_hibiscus, weight=4).add_count_function(1, 2))
loot05.add_entry(PoolEntryBuilder(biomesoplenty.blocks.sea_oats, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift],
                                table_id=constant.STAGE_OCEAN.id, table=loot05)

# 06
loot06 = MultiPoolLootTableBuilder()
loot06.create_new_pool(1, 2)
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.mahogany_sapling, weight=4).add_count_function(1, 2))
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.maple_sapling, weight=4).add_count_function(1, 2))
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.yellow_autumn_sapling, weight=4).add_count_function(1, 2))
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.orange_autumn_sapling, weight=4).add_count_function(1, 2))
loot06.create_new_pool(1, 1)
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.sprout, weight=4).add_count_function(1, 2))
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.goldenrod, weight=6).add_count_function(1, 2))
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.bush, weight=5).add_count_function(1, 2))
loot06.add_entry(PoolEntryBuilder(biomesoplenty.blocks.orange_cosmos, weight=5).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift],
                                table_id=constant.STAGE_FOREST.id, table=loot06)

# 07
loot07 = MultiPoolLootTableBuilder()
loot07.create_new_pool(0, 1)
loot07.add_entry(PoolEntryBuilder(biomesoplenty.blocks.wildflower, weight=4).add_count_function(1, 1))
loot07.add_entry(PoolEntryBuilder(biomesoplenty.blocks.desert_grass, weight=4).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift],
                                table_id=constant.STAGE_HOT.id, table=loot07)

# 08
loot08 = MultiPoolLootTableBuilder()
loot08.create_new_pool(0, 1)
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.hellbark_sapling, weight=4).add_count_function(1, 2))
loot08.create_new_pool(1, 2)
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.bramble, weight=4).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.bramble_leaves, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.blackstone_spines, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.brimstone_bud, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.hair, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.brimstone_cluster, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.blackstone_bulb, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.burning_blossom, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.items.blood_bucket, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.flesh_tendons, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.pus_bubble, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.brimstone_fumarole, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.rose_quartz_cluster, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.large_rose_quartz_bud, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.medium_rose_quartz_bud, weight=2).add_count_function(1, 2))
loot08.add_entry(PoolEntryBuilder(biomesoplenty.blocks.small_rose_quartz_bud, weight=2).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_NETHER.stage_gift],
                                table_id=constant.STAGE_NETHER.id, table=loot08)

# 09
loot09 = MultiPoolLootTableBuilder()
loot09.create_new_pool(0, 1)
loot09.add_entry(PoolEntryBuilder(biomesoplenty.blocks.flowering_oak_sapling, weight=4).add_count_function(1, 2))
loot09.create_new_pool(0, 1)
loot09.add_entry(PoolEntryBuilder(biomesoplenty.blocks.huge_clover_petal, weight=4).add_count_function(1, 2))
loot09.add_entry(PoolEntryBuilder(biomesoplenty.blocks.clover, weight=4).add_count_function(1, 2))
loot09.add_entry(PoolEntryBuilder(biomesoplenty.blocks.blue_hydrangea, weight=4).add_count_function(1, 2))
loot09.add_entry(PoolEntryBuilder(biomesoplenty.blocks.barley, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift],
                                table_id=constant.STAGE_VILLAGE.id, table=loot09)

# 10
loot10 = MultiPoolLootTableBuilder()
loot10.create_new_pool(0, 1)
loot10.add_entry(PoolEntryBuilder(biomesoplenty.blocks.jacaranda_sapling, weight=4).add_count_function(1, 2))
loot10.create_new_pool(0, 1)
loot10.add_entry(PoolEntryBuilder(biomesoplenty.blocks.lavender, weight=4).add_count_function(1, 2))
loot10.add_entry(PoolEntryBuilder(biomesoplenty.blocks.tall_lavender, weight=3).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift],
                                table_id=constant.STAGE_TRAVEL.id, table=loot10)
# 11
loot11 = MultiPoolLootTableBuilder()
loot11.create_new_pool(1, 2)
loot11.add_entry(PoolEntryBuilder(biomesoplenty.blocks.umbran_sapling, weight=4).add_count_function(1, 2))
loot11.add_entry(PoolEntryBuilder(biomesoplenty.blocks.magic_sapling, weight=4).add_count_function(1, 2))
loot11.add_entry(PoolEntryBuilder(biomesoplenty.blocks.dead_sapling, weight=4).add_count_function(1, 2))
loot11.create_new_pool(0, 1)
loot11.add_entry(PoolEntryBuilder(biomesoplenty.blocks.dead_branch, weight=4).add_count_function(1, 2))
loot11.add_entry(PoolEntryBuilder(biomesoplenty.blocks.dead_grass, weight=4).add_count_function(1, 2))
loot11.add_entry(PoolEntryBuilder(biomesoplenty.blocks.wilted_lily, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_ISOLATED.stage_gift],
                                table_id=constant.STAGE_ISOLATED.id, table=loot11)
# 12
loot12 = MultiPoolLootTableBuilder()
loot12.create_new_pool(0, 1)
loot12.add_entry(PoolEntryBuilder(biomesoplenty.blocks.origin_sapling, weight=4).add_count_function(1, 2))
loot12.add_entry(PoolEntryBuilder(biomesoplenty.blocks.glowshroom, weight=4).add_count_function(1, 2))
loot12.create_new_pool(0, 1)
loot12.add_entry(PoolEntryBuilder(biomesoplenty.blocks.spanish_moss, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_DEPTH.stage_gift],
                                table_id=constant.STAGE_DEPTH.id, table=loot12)
