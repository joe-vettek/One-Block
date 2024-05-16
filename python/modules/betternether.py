from mods import betternether
from core.provider import *
from core import constant

mod_id = "betternether"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage08.set_add_count(100)
stage08.add_block(betternether.blocks.anchor_tree_log, 5)
stage08.add_block(betternether.blocks.mushroom_fir_log, 5)
stage08.add_block(betternether.blocks.nether_sakura_log, 5)
stage08.add_block(betternether.blocks.rubeus_log, 5)
stage08.add_block(betternether.blocks.stalagnate_log, 5)
stage08.add_block(betternether.blocks.wart_log, 5)
stage08.add_block(betternether.blocks.willow_log, 5)

stage08.add_block(betternether.blocks.sepia_bone_grass, 5)
stage08.add_block(betternether.blocks.cincinnasite_ore, 5)
stage08.add_block(betternether.blocks.nether_ruby_ore, 5)

stage08.add_block(betternether.blocks.netherrack_moss, 5)
stage08.add_block(betternether.blocks.nether_mycelium, 5)
stage08.add_block(betternether.blocks.jungle_grass, 5)
stage08.add_block(betternether.blocks.mushroom_grass, 5)
stage08.add_block(betternether.blocks.sepia_mushroom_grass, 5)
stage08.add_block(betternether.blocks.swampland_grass, 5)
stage08.add_block(betternether.blocks.ceiling_mushrooms, 5)

stage08.add_mob(betternether.entities.firefly, 2, 1)
stage08.add_mob(betternether.entities.naga, 2, 1)
stage08.add_mob(betternether.entities.skull, 2, 1)
stage08.add_mob(betternether.entities.flying_pig, 2, 1)
stage08.add_mob(betternether.entities.hydrogen_jellyfish, 2, 1)
stage08.add_mob(betternether.entities.jungle_skeleton, 2, 1)
sub_provider.add_phase("08", stage08)

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 08
loot08 = MultiPoolLootTableBuilder()
loot08.create_new_pool(1, 2)
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.anchor_tree_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.giant_mold_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(
    SimplePoolEntryBuilder(betternether.blocks.jellyfish_mushroom_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.mushroom_fir_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.nether_sakura_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.rubeus_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.soul_lily_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.willow_sapling, weight=4).add_count_function(1, 1))
loot08.create_new_pool(1, 3)
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.stalagnate_seed, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.willow_torch, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.wart_seed, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.eye_seed, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.ink_bush_seed, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.black_apple_seed, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.agave, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.barrel_cactus, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.nether_cactus, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.lumabus_seed, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.golden_lumabus_seed, weight=4).add_count_function(1, 1))

loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.geyser, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.netherrack_stalactite, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.glowstone_stalactite, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.blackstone_stalactite, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.basalt_stalactite, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.bone_stalactite, weight=4).add_count_function(1, 1))

loot08.create_new_pool(2, 4)
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.black_vine, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.blooming_vine, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.golden_vine, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.whispering_gourd_vine, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.nether_grass, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.swamp_grass, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.soul_grass, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.jungle_plant, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.bone_grass, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.black_bush, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.egg_plant, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.magma_flower, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.feather_fern, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.moss_cover, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.neon_equisetum, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.hook_mushroom, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.wall_moss, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.wall_mushroom_brown, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.nether_cactus, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.wall_mushroom_red, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.jungle_moss, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.nether_reed_stem, weight=4).add_count_function(1, 1))

loot08.create_new_pool(1, 1)
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.bone_mushroom, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.orange_mushroom, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.red_mold, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.gray_mold, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.lucis_spore, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.giant_mold_sapling, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.gray_mold, weight=4).add_count_function(1, 1))
loot08.add_entry(SimplePoolEntryBuilder(betternether.blocks.gray_mold, weight=4).add_count_function(1, 1))

loot_provider.add_modified_loot(target=[constant.STAGE_NETHER.stage_gift],
                                table_id=constant.STAGE_NETHER.id, table=loot08)
