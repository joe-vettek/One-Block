from mods import nomansland
from core.provider import *
from core import constant

mod_id = "nomansland"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(nomansland.blocks.pine_log, 2)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(nomansland.blocks.willow_log, 4)
stage04.add_mob(nomansland.entities.billhook_bass, 2,1)
stage04.add_mob(nomansland.entities.goose, 2,1)
stage04.add_mob(nomansland.entities.billhook_bass, 2,1)

sub_provider.add_phase("04", stage04)



# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(nomansland.blocks.maple_log, 2)
stage06.add_block(nomansland.blocks.field_mushroom_block, 1)
stage06.add_mob(nomansland.entities.deer, 2,1)
sub_provider.add_phase("06", stage06)


# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage10.add_block(nomansland.blocks.walnut_log, 5)
sub_provider.add_phase("09", stage10)



# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(nomansland.blocks.budding_quartzite, 4)
sub_provider.add_phase("12", stage12)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
loot03 = MultiPoolLootTableBuilder()
loot03.create_new_pool(1, 2)
loot03.add_entry(SimplePoolEntryBuilder(nomansland.blocks.pine_sapling, weight=6).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(nomansland.blocks.yellow_birch_sapling, weight=6).add_count_function(1, 1))
loot03.create_new_pool(1, 1)
loot03.add_entry(SimplePoolEntryBuilder(nomansland.blocks.frosted_grass, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(nomansland.blocks.autumn_crocus, weight=3).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="03", table=loot03)

# 04
loot04 = MultiPoolLootTableBuilder()
loot04.create_new_pool(1, 2)
loot04.add_entry(SimplePoolEntryBuilder(nomansland.blocks.willow_sapling, weight=4).add_count_function(1, 2))
loot04.create_new_pool(1, 1)
loot04.add_entry(SimplePoolEntryBuilder(nomansland.blocks.pickleweed, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(nomansland.blocks.reeds, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(nomansland.blocks.cattail, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(nomansland.blocks.duckweed, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(nomansland.blocks.water_mosaic, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table=loot04)

# 05
loot05 = MultiPoolLootTableBuilder()
loot05.create_new_pool(1, 2)
loot05.add_entry(SimplePoolEntryBuilder(nomansland.blocks.seashells, weight=1).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(nomansland.blocks.short_beachgrass, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(nomansland.blocks.tall_beachgrass, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="05", table=loot05)

# 06
loot06 = MultiPoolLootTableBuilder()
loot06.create_new_pool(1, 2)
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.maple_sapling, weight=6).add_count_function(2, 4))
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.red_maple_sapling, weight=6).add_count_function(2, 4))
loot06.create_new_pool(0, 1)
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.shelf_mushroom, weight=6).add_count_function(2, 4))
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.field_mushroom, weight=6).add_count_function(2, 4))
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.fiddlehead, weight=6).add_count_function(2, 4))
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.thistle, weight=6).add_count_function(2, 4))
loot06.add_entry(SimplePoolEntryBuilder(nomansland.blocks.rafflesia, weight=6).add_count_function(2, 4))
loot06.add_entry(SimplePoolEntryBuilder(nomansland.items.grilled_mushrooms, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift],
                                table_id=constant.STAGE_FOREST.id,
                                table=loot06)

# 07
loot07 = MultiPoolLootTableBuilder()
loot07.create_new_pool(1, 1)
loot07.add_entry(SimplePoolEntryBuilder(nomansland.blocks.succulent, weight=6).add_count_function(2, 3))
loot07.add_entry(SimplePoolEntryBuilder(nomansland.blocks.barrel_cactus, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="07", table=loot07)

# 09
loot09 = MultiPoolLootTableBuilder()
loot09.create_new_pool(1, 1)
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.walnut_sapling, weight=6).add_count_function(2, 4))
loot09.create_new_pool(0,1)
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.grass_sprouts, weight=6).add_count_function(1, 2))
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.thistle, weight=6).add_count_function(2, 4))
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.aconite, weight=6).add_count_function(2, 4))
loot09.create_new_pool(0,1)
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.red_flowerbed, weight=6).add_count_function(2, 4))
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.blue_flowerbed, weight=6).add_count_function(2, 4))
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.white_flowerbed, weight=6).add_count_function(2, 4))
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.violet_flowerbed, weight=6).add_count_function(2, 4))
loot09.add_entry(SimplePoolEntryBuilder(nomansland.blocks.yellow_flowerbed, weight=6).add_count_function(2, 4))

loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift],
                                table_id=constant.STAGE_VILLAGE.id, table=loot09)


# 10
loot10 = MultiPoolLootTableBuilder()
loot10.create_new_pool(1, 1)
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.pale_cherry_sapling, weight=6).add_count_function(2, 4))
loot10.create_new_pool(1,2)
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.oat_grass, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.red_lupine, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.pink_lupine, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.yellow_lupine, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.blue_lupine, weight=6).add_count_function(1, 2))
loot10.create_new_pool(0,2)
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.starflower, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.wild_mint, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.clover_patch, weight=6).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(nomansland.blocks.ground_ivy, weight=6).add_count_function(1, 2))

loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table=loot10)

# 11
loot11 = MultiPoolLootTableBuilder()
loot11.create_new_pool(1, 1)
loot11.add_entry(SimplePoolEntryBuilder(nomansland.blocks.autumnal_oak_sapling, weight=6).add_count_function(1, 1))
loot11.create_new_pool(0, 1)
loot11.add_entry(SimplePoolEntryBuilder(nomansland.blocks.mycelium_growths, weight=6).add_count_function(2, 4))
loot11.add_entry(SimplePoolEntryBuilder(nomansland.blocks.mycelium_sprouts, weight=4).add_count_function(2, 4))
loot11.add_entry(SimplePoolEntryBuilder(nomansland.blocks.dried_grass, weight=6).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_ISOLATED.stage_gift], table_id="11", table=loot11)

# 12
loot12 = MultiPoolLootTableBuilder()
loot12.create_new_pool(0, 1)
loot12.add_entry(SimplePoolEntryBuilder(nomansland.blocks.beard_moss, weight=6).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_DEPTH.stage_gift],
                                table_id=constant.STAGE_DEPTH.id, table=loot12)
