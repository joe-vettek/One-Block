from mods import regions_unexplored
from core.provider import *
from core import constant

mod_id = "regions_unexplored"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.set_add_count(30)
stage03.add_block(regions_unexplored.blocks.ashen_log, 5)
stage03.add_block(regions_unexplored.blocks.larch_log, 5)
stage03.add_block(regions_unexplored.blocks.maple_log, 5)
stage03.add_block(regions_unexplored.blocks.pine_log, 5)
stage03.add_block(regions_unexplored.blocks.redwood_log, 5)
stage03.add_block(regions_unexplored.blocks.silver_birch_log, 5)
stage03.add_block(regions_unexplored.blocks.small_oak_log, 5)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(regions_unexplored.blocks.willow_log, 5)
stage04.add_block(regions_unexplored.blocks.magnolia_log, 5)
stage04.add_block(regions_unexplored.blocks.cypress_log, 5)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(regions_unexplored.blocks.blackwood_log, 10)
stage05.add_block(regions_unexplored.blocks.eucalyptus_log, 5)
stage05.add_block(regions_unexplored.blocks.palm_log, 5)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(regions_unexplored.blocks.bamboo_log, 6)
sub_provider.add_phase("06", stage06)

# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_block(regions_unexplored.blocks.joshua_log, 5)
stage07.add_block(regions_unexplored.blocks.kapok_log, 5)
stage07.add_block(regions_unexplored.blocks.socotra_log, 5)
stage07.add_block(regions_unexplored.blocks.baobab_log, 5)
sub_provider.add_phase("07", stage07)

# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage08.set_add_count(50)
stage08.add_block(regions_unexplored.blocks.cobalt_log, 4)
stage08.add_block(regions_unexplored.blocks.raw_redstone_block, 3)
stage08.add_block(regions_unexplored.blocks.brimsprout_nylium, 3)
stage08.add_block(regions_unexplored.blocks.cobalt_nylium, 3)
stage08.add_block(regions_unexplored.blocks.glistering_nylium, 3)
stage08.add_block(regions_unexplored.blocks.glistering_wart, 3)
stage08.add_block(regions_unexplored.blocks.overgrown_bone_block, 3)
stage08.add_block(regions_unexplored.blocks.mycotoxic_moss, 3)
stage08.add_block(regions_unexplored.blocks.chalk_grass_block, 3)
stage08.add_block(regions_unexplored.blocks.chalk, 3)
stage08.add_block(regions_unexplored.blocks.argillite_grass_block, 3)
stage08.add_block(regions_unexplored.blocks.argillite, 3)
stage08.add_block(regions_unexplored.blocks.cobalt_obsidian, 3)
stage08.add_block(regions_unexplored.blocks.ash, 3)
stage08.add_block(regions_unexplored.blocks.volcanic_ash, 3)
sub_provider.add_phase("08", stage08)

# # 09
# stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
# sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(regions_unexplored.blocks.mauve_log, 4)
sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_block(regions_unexplored.blocks.dead_log, 8)
stage11.add_block(regions_unexplored.blocks.brimwood_log, 8)
sub_provider.add_phase("11", stage11)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(regions_unexplored.blocks.alpha_log, 5)
stage12.add_block(regions_unexplored.blocks.alpha_grass_block, 2)
stage12.add_block(regions_unexplored.blocks.prismoss, 2)
stage12.add_block(regions_unexplored.blocks.deepslate_prismoss, 2)
stage12.add_block(regions_unexplored.blocks.deepslate_grass_block, 2)
sub_provider.add_phase("12", stage12)

# 01
loot01 = MultiPoolLootTableBuilder()
loot01.create_new_pool(0, 1)
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.orange_coneflower, weight=4).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.purple_coneflower, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.white_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.light_gray_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.gray_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.red_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.orange_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.yellow_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.lime_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.green_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cyan_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.light_blue_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.blue_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.purple_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.magenta_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.pink_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.brown_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.black_snowbelle, weight=2).add_count_function(1, 1))
loot01.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.hyacinth_flowers, weight=2).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_PLAIN.stage_gift],
                                table_id=constant.STAGE_PLAIN.id, table=loot01)
# 02
loot02 = MultiPoolLootTableBuilder()
loot02.create_new_pool(0, 1)
loot02.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cave_hyssop, weight=4).add_count_function(1, 1))
loot02.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.stone_bud, weight=4).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_PLAIN.stage_gift],
                                table_id=constant.STAGE_PLAIN.id, table=loot02)

# 03
loot03 = MultiPoolLootTableBuilder()
loot03.create_new_pool(2, 4)
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.ashen_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.larch_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.golden_larch_sapling, weight=2).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.maple_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.orange_maple_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.red_maple_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.maple_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.pine_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.redwood_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.silver_birch_sapling, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.small_oak_sapling, weight=3).add_count_function(1, 1))
loot03.create_new_pool(0, 1)
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.ashen_shrub, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.larch_shrub, weight=4).add_count_function(1, 2))
loot03.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.golden_larch_shrub, weight=2).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.maple_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.orange_maple_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.red_maple_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.maple_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.pine_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.redwood_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.silver_birch_shrub, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.birch_shrub, weight=4).add_count_function(1, 2))
loot03.create_new_pool(0, 1)
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.ashen_grass, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.bladed_grass, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.bladed_tall_grass, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dead_steppe_shrub, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.frozen_grass, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.medium_grass, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.bleeding_heart, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift],
                                table_id=constant.STAGE_COLD.id, table=loot03)

# 04
loot04 = MultiPoolLootTableBuilder()
loot04.create_new_pool(1, 2)
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cypress_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.magnolia_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.blue_magnolia_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.pink_magnolia_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.white_magnolia_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.willow_sapling, weight=4).add_count_function(1, 2))
loot04.create_new_pool(0, 1)
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cypress_shrub, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.magnolia_shrub, weight=4).add_count_function(1, 2))
loot04.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.blue_magnolia_shrub, weight=4).add_count_function(1, 2))
loot04.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.pink_magnolia_shrub, weight=4).add_count_function(1, 2))
loot04.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.white_magnolia_shrub, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.willow_shrub, weight=4).add_count_function(1, 2))
loot04.create_new_pool(0, 1)
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.duckweed, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.flowering_lily_pad, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.day_lily, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.blue_magnolia_flowers, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.pink_magnolia_flowers, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.white_magnolia_flowers, weight=4).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift],
                                table_id=constant.STAGE_SWAMP.id, table=loot04)
# 05
loot05 = MultiPoolLootTableBuilder()
loot05.create_new_pool(1, 2)
loot05.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.blackwood_sapling, weight=4).add_count_function(1, 2))
loot05.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.eucalyptus_sapling, weight=4).add_count_function(1, 2))
loot05.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.palm_sapling, weight=4).add_count_function(1, 2))
loot05.create_new_pool(0, 1)
loot05.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.blackwood_shrub, weight=4).add_count_function(1, 2))
loot05.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.eucalyptus_shrub, weight=4).add_count_function(1, 2))
loot05.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.palm_shrub, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift],
                                table_id=constant.STAGE_OCEAN.id, table=loot05)

# 06
loot06 = MultiPoolLootTableBuilder()
loot06.create_new_pool(1, 1)
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.bamboo_sapling, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.kapok_sapling, weight=4).add_count_function(1, 1))
loot06.create_new_pool(0, 1)
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dark_oak_shrub, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.kapok_shrub, weight=4).add_count_function(1, 1))
loot06.create_new_pool(0, 1)
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.kapok_vines, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.spanish_moss, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.poppy_bush, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.salmon_poppy_bush, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.tsubaki, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.waratah, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift],
                                table_id=constant.STAGE_FOREST.id, table=loot06)

# 07
loot07 = MultiPoolLootTableBuilder()
loot07.create_new_pool(0, 1)
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.joshua_sapling, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.socotra_sapling, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.baobab_sapling, weight=3).add_count_function(1, 1))
loot07.create_new_pool(0, 1)
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.joshua_shrub, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.socotra_shrub, weight=4).add_count_function(1, 1))
loot07.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.small_desert_shrub, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.baobab_shrub, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.acacia_shrub, weight=3).add_count_function(1, 1))
loot07.create_new_pool(0, 1)
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.barrel_cactus, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.sandy_grass, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.small_desert_shrub, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.steppe_grass, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.steppe_shrub, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.sandy_tall_grass, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.steppe_tall_grass, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.windswept_grass, weight=3).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.hyacinth_flowers, weight=6).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift],
                                table_id=constant.STAGE_HOT.id, table=loot07)

# 08
loot08 = MultiPoolLootTableBuilder()
loot08.create_new_pool(0, 1)
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cobalt_sapling, weight=4).add_count_function(1, 1))
loot08.create_new_pool(0, 1)
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.blackstone_cluster, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.glistering_ivy, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.hanging_earlight_fruit, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.saguaro_cactus, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.corpse_flower, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.pointed_redstone, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.redstone_bulb, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.redstone_bud, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.glistering_fern, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.mycotoxic_grass, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cobalt_earlight, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.glister_bulb, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.glister_spire, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.mycotoxic_daisy, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.tall_cobalt_earlight, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.tall_cobalt_earlight, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.tall_cobalt_earlight, weight=4).add_count_function(1, 1))


loot_provider.add_modified_loot(target=[constant.STAGE_NETHER.stage_gift],
                                table_id=constant.STAGE_NETHER.id, table=loot08)

# 09
loot09 = MultiPoolLootTableBuilder()
loot09.create_new_pool(0, 1)
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.apple_oak_sapling, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.flowering_sapling, weight=4).add_count_function(1, 2))
loot09.create_new_pool(0, 1)
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.oak_shrub, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.flowering_shrub, weight=4).add_count_function(1, 2))
loot09.create_new_pool(0, 1)
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.daisy, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dorcel, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.hibiscus, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.hyssop, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.mallow, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.blue_lupine, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.pink_lupine, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.purple_lupine, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.yellow_lupine, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.barley, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift],
                                table_id=constant.STAGE_VILLAGE.id, table=loot09)

# 10
loot10 = MultiPoolLootTableBuilder()
loot10.create_new_pool(0, 1)
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.mauve_sapling, weight=4).add_count_function(1, 2))
loot10.create_new_pool(0, 1)
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.mauve_shrub, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.cherry_shrub, weight=4).add_count_function(1, 2))
loot10.create_new_pool(0, 1)
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.clover, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.aster, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.felicia_daisy, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.fireweed, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.white_trillium, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.meadow_sage, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.tassel, weight=4).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift],
                                table_id=constant.STAGE_TRAVEL.id, table=loot10)
# 11
loot11 = MultiPoolLootTableBuilder()
loot11.create_new_pool(1, 2)
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dead_sapling, weight=4).add_count_function(1, 2))
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dead_pine_sapling, weight=4).add_count_function(1, 2))
loot11.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.enchanted_birch_sapling, weight=4).add_count_function(1, 2))
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.brimwood_sapling, weight=4).add_count_function(1, 2))
loot11.create_new_pool(0, 1)
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dead_shrub, weight=4).add_count_function(1, 2))
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.dead_pine_shrub, weight=4).add_count_function(1, 2))
loot11.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.enchanted_birch_shrub, weight=4).add_count_function(1, 2))
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.brimwood_shrub, weight=4).add_count_function(1, 2))
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.elephant_ear, weight=4).add_count_function(1, 2))
loot11.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.wilting_trillium, weight=4).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_ISOLATED.stage_gift],
                                table_id=constant.STAGE_ISOLATED.id, table=loot11)
# 12
loot12 = MultiPoolLootTableBuilder()
loot12.create_new_pool(0, 1)
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.alpha_sapling, weight=4).add_count_function(1, 2))
loot12.create_new_pool(0, 1)
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.spanish_moss, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.blue_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.green_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.pink_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.yellow_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.tall_blue_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.tall_green_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.tall_pink_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.tall_yellow_bioshroom, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.prismarite_cluster, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.large_prismarite_cluster, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.hanging_prismarite, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.prismoss_sprout, weight=4).add_count_function(1, 2))
loot12.add_entry(
    SimplePoolEntryBuilder(regions_unexplored.blocks.brimsprout, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.glistering_sprout, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.glistering_bloom, weight=4).add_count_function(1, 2))

loot12.create_new_pool(0, 1)
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.alpha_dandelion, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.alpha_rose, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.alpha_dandelion, weight=4).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(regions_unexplored.blocks.alpha_dandelion, weight=4).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_DEPTH.stage_gift],
                                table_id=constant.STAGE_DEPTH.id, table=loot12)
