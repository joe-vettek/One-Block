from mods import bloomingnature
from core.provider import *
from core import constant

mod_id = "bloomingnature"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)
# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(bloomingnature.blocks.fir_log, 5)
stage03.add_block(bloomingnature.blocks.larch_log, 5)
stage03.add_block(bloomingnature.blocks.aspen_log, 5)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(bloomingnature.blocks.ebony_log, 5)
stage04.add_block(bloomingnature.blocks.swamp_oak_log, 5)
stage04.add_block(bloomingnature.blocks.swamp_cypress_log, 5)
stage04.add_block(bloomingnature.blocks.marsh_block, 5)
stage04.add_mob(bloomingnature.entities.pelican, 1, 1)
stage04.add_mob(bloomingnature.entities.muddy_pig, 2, 1)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage05.add_block(bloomingnature.blocks.fan_palm_log, 5)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(bloomingnature.blocks.forest_moss, 5)
stage06.add_mob(bloomingnature.entities.red_wolf, 2, 1)
stage06.add_mob(bloomingnature.entities.raccoon, 2, 1)
stage06.add_mob(bloomingnature.entities.turkey, 2, 1)
stage06.add_mob(bloomingnature.entities.owl, 2, 1)
stage06.add_mob(bloomingnature.entities.termite, 2, 1)
sub_provider.add_phase("06", stage06)

# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_block(bloomingnature.blocks.baobab_log, 5)
stage07.add_block(bloomingnature.blocks.quicksand, 4)
stage07.add_mob(bloomingnature.entities.wandering_gardener, 2, 1)
stage07.add_entry(PhaseEntryBuilder(constant.TYPE_MOB, bloomingnature.entities.termite, 2, 1)
                  .add_preprocessing(PhaseEntryBuilder(constant.TYPE_BLOCK, bloomingnature.blocks.termite_mound)))
stage07.add_mob(bloomingnature.entities.deer, 2, 1)
stage07.add_mob(bloomingnature.entities.boar, 2, 1)
stage07.add_mob(bloomingnature.entities.bison, 2, 1)
sub_provider.add_phase("07", stage07)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(bloomingnature.blocks.chestnut_log, 4)
stage10.add_block(bloomingnature.blocks.travertin, 2)
stage10.add_mob(bloomingnature.entities.squirrel, 2, 1)
sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_mob(bloomingnature.entities.mossy_sheep, 2, 1)
sub_provider.add_phase("11", stage11)

# 03
loot03 = MultiPoolLootTableBuilder()
loot03.create_new_pool(1, 2)
loot03.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.fir_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.larch_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.aspen_sapling, weight=4).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift],
                                table_id=constant.STAGE_COLD.id, table=loot03)

# 04
loot04 = MultiPoolLootTableBuilder()
loot04.create_new_pool(1, 2)
loot04.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.ebony_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.swamp_cypress_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.swamp_oak_sapling, weight=4).add_count_function(1, 2))
loot04.create_new_pool(1, 2)
loot04.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.cardinal, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.reed, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.cattail, weight=4).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift],
                                table_id=constant.STAGE_SWAMP.id, table=loot04)
# 05
loot05 = MultiPoolLootTableBuilder()
loot05.create_new_pool(0, 1)
loot05.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.fan_palm_sprout, weight=4).add_count_function(1, 2))
loot05.create_new_pool(0, 1)
loot05.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.beach_bush, weight=4).add_count_function(1, 2))
loot05.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.beach_grass, weight=4).add_count_function(1, 2))
loot05.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.beach_bush_tall, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift],
                                table_id=constant.STAGE_OCEAN.id, table=loot05)

# 06
loot06 = MultiPoolLootTableBuilder()
loot06.create_new_pool(1, 1)
loot06.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.goatsbeard, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.white_orchid, weight=4).add_count_function(1, 2))
loot06.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.daphne, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift],
                                table_id=constant.STAGE_FOREST.id, table=loot06)

# 07
loot07 = MultiPoolLootTableBuilder()
loot07.create_new_pool(0, 1)
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.baobab_sapling, weight=4).add_count_function(1, 1))
loot07.create_new_pool(0, 1)
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.freesia_yellow, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.freesia_pink, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.genisteae, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.bird_of_paradise, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.bottlebrushes, weight=4).add_count_function(1, 1))
loot07.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.hyssop, weight=4).add_count_function(1, 1))

loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift],
                                table_id=constant.STAGE_HOT.id, table=loot07)

# 09
loot09 = MultiPoolLootTableBuilder()
loot09.create_new_pool(0, 1)
loot09.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.golden_rod, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.wild_sunflower, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.joe_pye, weight=4).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.begonie, weight=5).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift],
                                table_id=constant.STAGE_VILLAGE.id, table=loot09)

# 10
loot10 = MultiPoolLootTableBuilder()
loot10.create_new_pool(0, 1)
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.chestnut_sapling, weight=4).add_count_function(1, 2))
loot10.create_new_pool(1, 2)
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.lupine_blue, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.lupine_purple, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.tall_lupine_blue, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.tall_lupine_purple, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.foxglove_white, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.foxglove_pink, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.bluebell, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.mountain_snowbell, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.mountain_laurel, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.tall_mountain_laurel, weight=4).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(bloomingnature.blocks.mountain_laurel, weight=4).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift],
                                table_id=constant.STAGE_TRAVEL.id, table=loot10)
