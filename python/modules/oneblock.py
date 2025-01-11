from mods import minecraft
from core.provider import *
from core import constant

mod_id = "oneblock"
run_list = []

aa = DataPackProvider(mod_id)
aa.get_datapack_name = (lambda: "oneblock")
run_list.append(aa)

sub_provider = PhaseProvider(mod_id)
sub_provider.get_datapack_name = (lambda: "oneblock")
run_list.append(sub_provider)

loot_provider = ModifiedLootTableProvider(mod_id)
loot_provider.get_datapack_name = (lambda: "oneblock")
run_list.append(loot_provider)

config_provider = ConfigProvider(mod_id)
config_provider.get_datapack_name = (lambda: "oneblock")
run_list.append(config_provider)

config_provider.add_config(ConfigTableBuilder(
    [constant.STAGE_00.get_phase_id(), constant.STAGE_PLAIN.get_phase_id(), constant.STAGE_UNDERGROUND.get_phase_id(),
     constant.STAGE_COLD.get_phase_id(), constant.STAGE_SWAMP.get_phase_id(), constant.STAGE_OCEAN.get_phase_id(),
     constant.STAGE_FOREST.get_phase_id(), constant.STAGE_HOT.get_phase_id(), constant.STAGE_NETHER.get_phase_id(),
     constant.STAGE_VILLAGE.get_phase_id(), constant.STAGE_TRAVEL.get_phase_id(),
     constant.STAGE_ISOLATED.get_phase_id(), constant.STAGE_DEPTH.get_phase_id(), constant.STAGE_END.get_phase_id(),
     constant.STAGE_ALL.get_phase_id()]))

# 00
stage00 = PhaseTableBuilder(count=47, end_gift=constant.STAGE_00.end_gift)
stage00.add_entry(PhaseEntryBuilder(constant.TYPE_BLOCK, minecraft.blocks.dirt).set_precedence(2, 2))
stage00.add_entry(PhaseEntryBuilder(constant.TYPE_BLOCK, minecraft.blocks.grass_block).set_precedence(precedence_end=5))
stage00.add_block(minecraft.blocks.grass_block, 19)
stage00.add_block(minecraft.blocks.oak_log, 13)
stage00.add_block(minecraft.blocks.gravel, 5)
stage00.add_mob(minecraft.entities.pig, 1, 1)
stage00.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_00.stage_gift))
stage00.add_chest_gift(constant.GIFT_WATER_BUCKET, min_times=1, max_times=1)
sub_provider.add_phase("00", stage00)

# 01
stage01 = PhaseTableBuilder(count=240, end_gift=constant.STAGE_PLAIN.end_gift)
stage01.add_block(minecraft.blocks.grass_block, 88)
stage01.add_block(minecraft.blocks.clay, 19)
stage01.add_block(minecraft.blocks.oak_log, 17)
stage01.add_block(minecraft.blocks.birch_log, 11)
stage01.add_block(minecraft.blocks.melon, 10)
stage01.add_block(minecraft.blocks.podzol, 9)
stage01.add_block(minecraft.blocks.pumpkin, 6)
stage01.add_mob(minecraft.items.chicken, 1, 1)
stage01.add_mob(minecraft.entities.sheep, 1, 1)
stage01.add_mob(minecraft.entities.cow, 1, 1)
stage01.add_mob(minecraft.entities.pig, 1, 1)
stage01.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_PLAIN.stage_gift))
stage01.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_PLAIN.variety_gift))
sub_provider.add_phase("01", stage01)

# 02
stage02 = PhaseTableBuilder(count=390, end_gift=constant.STAGE_UNDERGROUND.end_gift)
stage02.add_block(minecraft.blocks.stone, 97)
stage02.add_block(minecraft.blocks.gravel, 37)
stage02.add_block(minecraft.blocks.dirt, 33)
stage02.add_block(minecraft.blocks.granite, 18)
stage02.add_block(minecraft.blocks.diorite, 17)
stage02.add_block(minecraft.blocks.andesite, 17)
stage02.add_block(minecraft.blocks.coal_ore, 11)
stage02.add_block(minecraft.blocks.iron_ore, 13)
stage02.add_block(minecraft.blocks.copper_ore, 17)
stage02.add_block(minecraft.blocks.oak_log, 12)
stage02.add_block(minecraft.blocks.birch_log, 9)
stage02.add_mob(minecraft.items.rabbit, 1, 1)
stage02.add_mob(minecraft.entities.zombie, 2, 2)
stage02.add_mob(minecraft.entities.spider, 2, 1)
stage02.add_mob(minecraft.entities.creeper, 3, 1)
stage02.add_mob(minecraft.entities.mooshroom, 1, 1)
stage02.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_UNDERGROUND.stage_gift))
stage02.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_UNDERGROUND.variety_gift))
sub_provider.add_phase("02", stage02)

# 03
stage03 = PhaseTableBuilder(count=470, end_gift=constant.STAGE_COLD.end_gift)
stage03.add_block(minecraft.blocks.grass_block, 77)
stage03.add_block(minecraft.blocks.stone, 69)
stage03.add_block(minecraft.blocks.snow_block, 44)
stage03.add_block("minecraft:powder_snow", 22)
stage03.add_block(minecraft.blocks.spruce_log, 24)
stage03.add_block(minecraft.blocks.packed_ice, 17)
stage03.add_block(minecraft.blocks.andesite, 16)
stage03.add_mob(minecraft.entities.stray, 7, 1)
stage03.add_block(minecraft.blocks.granite, 14)
stage03.add_block(minecraft.blocks.gravel, 14)
stage03.add_block(minecraft.blocks.diorite, 13)
stage03.add_block(minecraft.blocks.iron_ore, 10)
stage03.add_block(minecraft.blocks.copper_ore, 17)
stage03.add_block(minecraft.blocks.dark_oak_log, 10)
stage03.add_block(minecraft.blocks.coal_ore, 10)
stage03.add_mob(minecraft.entities.fox, 1, 1)
stage03.add_block(minecraft.blocks.birch_log, 5)
stage03.add_block(minecraft.blocks.gold_ore, 5)
stage03.add_mob(minecraft.entities.wolf, 1, 1)
stage03.add_mob(minecraft.entities.polar_bear, 1, 1)
stage03.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_COLD.stage_gift))
stage03.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_COLD.variety_gift))
sub_provider.add_phase("03", stage03)

# 04
stage04 = PhaseTableBuilder(count=420, end_gift=constant.STAGE_SWAMP.end_gift)
stage04.add_block(minecraft.blocks.sand, 10)
stage04.add_block(minecraft.blocks.mangrove_log, 20)
stage04.add_block(minecraft.blocks.mud, 15)
stage04.add_block(minecraft.blocks.muddy_mangrove_roots, 5)
stage04.add_block(minecraft.blocks.gravel, 8)
stage04.add_block(minecraft.blocks.clay, 5)
stage04.add_block(minecraft.blocks.iron_ore, 6)
stage04.add_block(minecraft.blocks.diorite, 3)
stage04.add_block(minecraft.blocks.stone, 4)
stage04.add_block(minecraft.blocks.coal_ore, 7)
stage04.add_block(minecraft.blocks.gold_ore, 4)
stage04.add_block(minecraft.blocks.copper_ore, 3)
stage04.add_block(minecraft.blocks.dark_oak_log, 2)
stage04.add_block(minecraft.blocks.oak_log, 6)
stage04.add_mob(minecraft.entities.frog, 2, 1)
stage04.add_mob(minecraft.entities.tadpole, 1, 1)
stage04.add_mob(minecraft.entities.salmon, 4, 1)
stage04.add_mob(minecraft.entities.squid, 1, 1)
stage04.add_mob("minecraft:bogged", 2)
stage04.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_SWAMP.stage_gift))
sub_provider.add_phase("04", stage04)

# 05
stage05 = PhaseTableBuilder(count=700, end_gift=constant.STAGE_OCEAN.end_gift)
stage05.add_block(minecraft.blocks.sand, 79)
stage05.add_block(minecraft.blocks.prismarine, 77)
stage05.add_block(minecraft.blocks.prismarine_bricks, 49)
stage05.add_block(minecraft.blocks.dark_prismarine, 45)
stage05.add_block(minecraft.blocks.sea_lantern, 14)
stage05.add_block(minecraft.blocks.sponge, 13)
stage05.add_block(minecraft.blocks.iron_ore, 13)
stage05.add_block(minecraft.blocks.copper_ore, 3)
stage05.add_block(minecraft.blocks.diorite, 13)
stage05.add_block(minecraft.blocks.clay, 12)
stage05.add_block(minecraft.blocks.fire_coral_block, 12)
stage05.add_block(minecraft.blocks.coal_ore, 12)
stage05.add_block(minecraft.blocks.gold_ore, 12)
stage05.add_block(minecraft.blocks.dark_oak_log, 11)
stage05.add_block(minecraft.blocks.horn_coral_block, 11)
stage05.add_block(minecraft.blocks.stone, 10)
stage05.add_block(minecraft.blocks.tube_coral_block, 10)
stage05.add_block(minecraft.blocks.bubble_coral_block, 10)
stage05.add_block(minecraft.blocks.brain_coral_block, 10)
stage05.add_block(minecraft.blocks.oak_log, 9)
stage05.add_mob(minecraft.entities.guardian, 6, 1)
stage05.add_mob(minecraft.entities.cod, 4, 2)
stage05.add_mob(minecraft.entities.tropical_fish, 4, 2)
stage05.add_mob(minecraft.entities.salmon, 3, 2)
stage05.add_mob(minecraft.entities.drowned, 4, 1)
stage05.add_mob(minecraft.entities.turtle, 1, 1)
stage05.add_mob(minecraft.entities.dolphin, 1, 1)
stage05.add_mob(minecraft.entities.elder_guardian, 2, 2)
stage05.add_mob(minecraft.entities.pufferfish, 2, 2)
stage05.add_mob(minecraft.entities.squid, 1, 1)
stage05.add_block(minecraft.blocks.diamond_ore, 2)
stage05.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_OCEAN.stage_gift))
stage05.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_OCEAN.variety_gift))
stage05.add_chest_gift(constant.GIFT_MUSICAL, min_times=1, max_times=1)
sub_provider.add_phase("05", stage05)

# 06
stage06 = PhaseTableBuilder(count=570, end_gift=constant.STAGE_FOREST.end_gift)
stage06.add_block(minecraft.blocks.cobblestone, 212)
stage06.add_block(minecraft.blocks.mossy_cobblestone, 128)
stage06.add_block(minecraft.blocks.jungle_log, 70)
stage06.add_block(minecraft.blocks.grass_block, 41)
stage06.add_block(minecraft.blocks.redstone_ore, 17)
stage06.add_block(minecraft.blocks.iron_ore, 13)
stage06.add_block(minecraft.blocks.copper_ore, 6)
stage06.add_block(minecraft.blocks.coal_ore, 9)
stage06.add_block(minecraft.blocks.gold_ore, 8)
stage06.add_mob(minecraft.entities.witch, 6, 1)
stage06.add_mob(minecraft.entities.ocelot, 1, 1)
stage06.add_mob(minecraft.entities.vex, 6, 1)
stage06.add_mob(minecraft.entities.parrot, 2, 6)
stage06.add_mob(minecraft.entities.horse, 1, 1)
stage06.add_block(minecraft.blocks.diamond_ore, 3)
stage06.add_mob(minecraft.entities.panda, 1, 1)
stage06.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_FOREST.stage_gift))
stage06.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_FOREST.variety_gift))
stage06.add_chest_gift(constant.GIFT_ODD, min_times=1, max_times=1)
stage06.add_chest_gift(constant.GIFT_MUSICAL, min_times=1, max_times=1)
sub_provider.add_phase("06", stage06)


# 07
stage07 = PhaseTableBuilder(count=610, end_gift=constant.STAGE_HOT.end_gift)
stage07.add_block(minecraft.blocks.red_sand, 103)
stage07.add_block(minecraft.blocks.red_sandstone, 81)
stage07.add_block(minecraft.blocks.terracotta, 40)
stage07.add_block(minecraft.blocks.sandstone, 36)
stage07.add_block(minecraft.blocks.sand, 31)
stage07.add_block(minecraft.blocks.acacia_log, 25)
stage07.add_block(minecraft.blocks.brown_terracotta, 24)
stage07.add_block(minecraft.blocks.orange_terracotta, 23)
stage07.add_block(minecraft.blocks.red_terracotta, 23)
stage07.add_block(minecraft.blocks.yellow_terracotta, 23)
stage07.add_block(minecraft.blocks.redstone_ore, 20)
stage07.add_block(minecraft.blocks.light_gray_terracotta, 17)
stage07.add_block(minecraft.blocks.white_terracotta, 17)
stage07.add_mob(minecraft.entities.husk, 16, 2)
stage07.add_block(minecraft.blocks.emerald_ore, 13)
stage07.add_block(minecraft.blocks.iron_ore, 11)
stage07.add_block(minecraft.blocks.coal_ore, 10)
stage07.add_block(minecraft.blocks.copper_ore, 15)
stage07.add_block(minecraft.blocks.lapis_ore, 8)
stage07.add_mob(minecraft.entities.pillager, 6, 1)
stage07.add_mob(minecraft.entities.vindicator, 4, 1)
stage07.add_mob(minecraft.entities.donkey, 1, 1)
stage07.add_mob(minecraft.entities.villager, 3, 1)
stage07.add_mob(minecraft.entities.fox, 1, 1)
stage07.add_block(minecraft.blocks.diamond_ore, 4)
stage07.add_mob(minecraft.entities.llama, 2, 1)
stage07.add_mob(minecraft.entities.wandering_trader, 1, 1)
stage07.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_HOT.stage_gift))
stage07.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_HOT.variety_gift))
stage07.add_chest_gift(constant.GIFT_ODD, min_times=1, max_times=1)
stage07.add_chest_gift(constant.GIFT_MUSICAL, min_times=1, max_times=1)
sub_provider.add_phase("07", stage07)

# 08
stage08 = PhaseTableBuilder(count=790, end_gift=constant.STAGE_NETHER.end_gift)
stage08.add_block(minecraft.blocks.netherrack, 95)
stage08.add_block(minecraft.blocks.blackstone, 80)
stage08.add_block(minecraft.blocks.soul_sand, 49)
stage08.add_block(minecraft.blocks.nether_bricks, 47)
stage08.add_block(minecraft.blocks.basalt, 37)
stage08.add_block(minecraft.blocks.red_nether_bricks, 37)
stage08.add_block(minecraft.blocks.magma_block, 31)
stage08.add_block(minecraft.blocks.warped_nylium, 30)
stage08.add_block(minecraft.blocks.crimson_nylium, 29)
stage08.add_block(minecraft.blocks.soul_soil, 21)
stage08.add_block(minecraft.blocks.glowstone, 19)
stage08.add_block(minecraft.blocks.nether_quartz_ore, 18)
stage08.add_block(minecraft.blocks.shroomlight, 17)
stage08.add_block(minecraft.blocks.nether_wart_block, 17)
stage08.add_block(minecraft.blocks.warped_wart_block, 17)
stage08.add_block(minecraft.blocks.gilded_blackstone, 16)
stage08.add_block(minecraft.blocks.nether_gold_ore, 12)
stage08.add_block(minecraft.blocks.obsidian, 12)
stage08.add_mob(minecraft.entities.magma_cube, 9, 1)
stage08.add_mob(minecraft.entities.blaze, 6, 1)
stage08.add_mob(minecraft.entities.hoglin, 6, 1)
stage08.add_mob(minecraft.entities.piglin, 6, 1)
stage08.add_mob(minecraft.entities.ghast, 4, 1)
stage08.add_mob(minecraft.entities.wither_skeleton, 4, 1)
stage08.add_block(minecraft.blocks.ancient_debris, 4)
stage08.add_block(minecraft.blocks.crying_obsidian, 3)
stage08.add_mob(minecraft.entities.strider, 2, 2)
stage08.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_NETHER.stage_gift))
stage08.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_NETHER.variety_gift))
stage08.add_chest_gift(constant.GIFT_ODD, min_times=1, max_times=1)
sub_provider.add_phase("08", stage08)

# 09
stage09 = PhaseTableBuilder(count=730, end_gift=constant.STAGE_VILLAGE.end_gift)
stage09.add_block(minecraft.blocks.quartz_block, 213)
stage09.add_block(minecraft.blocks.grass_block, 69)
stage09.add_block(minecraft.blocks.oak_log, 50)
stage09.add_mob(minecraft.entities.slime, 16, 1)
stage09.add_mob(minecraft.entities.bee, 2, 1)
stage09.add_block(minecraft.blocks.gold_ore, 15)
stage09.add_block(minecraft.blocks.lapis_ore, 15)
stage09.add_block(minecraft.blocks.iron_ore, 13)
stage09.add_block(minecraft.blocks.copper_ore, 13)
stage09.add_block(minecraft.blocks.emerald_ore, 12)
stage09.add_block(minecraft.blocks.honeycomb_block, 10)
stage09.add_block(minecraft.blocks.redstone_ore, 8)
stage09.add_mob(minecraft.entities.cat, 1, 1)
stage09.add_block(minecraft.blocks.diamond_ore, 6)
stage09.add_mob(minecraft.entities.phantom, 3, 1)
stage09.add_mob(minecraft.entities.mule, 2, 1)
stage09.add_block(minecraft.blocks.slime_block, 4)
stage09.add_block(minecraft.blocks.honey_block, 4)
stage09.add_mob(minecraft.entities.zombie_horse, 1, 1)
stage09.add_mob(minecraft.entities.skeleton_horse, 1, 1)
stage09.add_block(minecraft.blocks.bee_nest, 1)
stage09.add_block(minecraft.blocks.beehive, 1)
stage09.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_VILLAGE.stage_gift))
stage09.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_VILLAGE.variety_gift))
stage09.add_chest_gift(constant.GIFT_RARE, min_times=1, max_times=1)
sub_provider.add_phase("09", stage09)

# 10
stage10 = PhaseTableBuilder(count=750, end_gift=constant.STAGE_TRAVEL.end_gift)
stage10.add_block(minecraft.blocks.dripstone_block, 80)
stage10.add_block(minecraft.blocks.grass_block, 50)
stage10.add_block(minecraft.blocks.coarse_dirt, 20)
stage10.add_mob(minecraft.entities.allay, 1, 1)
stage10.add_mob(minecraft.entities.camel, 2, 1)
stage10.add_block(minecraft.blocks.cherry_log, 29)
stage10.add_block(minecraft.blocks.lapis_ore, 15)
stage10.add_block(minecraft.blocks.iron_ore, 13)
stage10.add_block(minecraft.blocks.emerald_ore, 12)
stage10.add_block(minecraft.blocks.copper_ore, 13)
stage10.add_block(minecraft.blocks.moss_block, 16)
stage10.add_block(minecraft.blocks.rooted_dirt, 8)
stage10.add_block(minecraft.blocks.oak_log, 6)
stage10.add_mob(minecraft.entities.goat, 1, 1)
stage10.add_mob(minecraft.entities.axolotl, 2, 2)
stage10.add_mob("minecraft:breeze", 2)
stage10.add_block(minecraft.blocks.stone, 8)
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_ARCHAEOLOGY, minecraft.blocks.suspicious_sand, 8).set_loot_table(
        "minecraft:archaeology/desert_pyramid"))
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_ARCHAEOLOGY, minecraft.blocks.suspicious_sand, 7).set_loot_table(
        "minecraft:archaeology/desert_well"))
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_ARCHAEOLOGY, minecraft.blocks.suspicious_sand, 6).set_loot_table(
        "minecraft:archaeology/ocean_ruin_warm"))
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_ARCHAEOLOGY, minecraft.blocks.suspicious_gravel, 8).set_loot_table(
        "minecraft:archaeology/ocean_ruin_cold"))
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_ARCHAEOLOGY, minecraft.blocks.suspicious_gravel, 12).set_loot_table(
        "minecraft:archaeology/trail_ruins_common"))
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_ARCHAEOLOGY, minecraft.blocks.suspicious_gravel, 3).set_loot_table(
        "minecraft:archaeology/trail_ruins_rare"))
stage10.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_TRAVEL.stage_gift))
stage10.add_chest_gift(constant.GIFT_RARE, min_times=1, max_times=1)
stage10.add_chest_gift(constant.GIFT_MUSICAL, min_times=1, max_times=1)
sub_provider.add_phase("10", stage10)

# 11
stage11 = PhaseTableBuilder(count=780, end_gift=constant.STAGE_ISOLATED.end_gift)
stage11.add_block(minecraft.blocks.stone_bricks, 139)
stage11.add_block(minecraft.blocks.mossy_stone_bricks, 112)
stage11.add_block(minecraft.blocks.mycelium, 84)
stage11.add_block(minecraft.blocks.cracked_stone_bricks, 59)
stage11.add_block(minecraft.blocks.chiseled_stone_bricks, 59)
stage11.add_block(minecraft.blocks.light_gray_concrete_powder, 58)
stage11.add_block(minecraft.blocks.gravel, 39)
stage11.add_block(minecraft.blocks.coal_ore, 16)
stage11.add_block(minecraft.blocks.iron_ore, 15)
stage11.add_block(minecraft.blocks.copper_ore, 8)
stage11.add_mob(minecraft.entities.skeleton, 14, 1)
stage11.add_block(minecraft.blocks.dark_oak_log, 14)
stage11.add_block(minecraft.blocks.bone_block, 13)
stage11.add_mob(minecraft.entities.cave_spider, 12, 1)
stage11.add_mob(minecraft.entities.silverfish, 12, 1)
stage11.add_block(minecraft.blocks.redstone_ore, 12)
stage11.add_block(minecraft.blocks.emerald_ore, 5)
stage11.add_block(minecraft.blocks.lapis_ore, 5)
stage11.add_block(minecraft.blocks.diamond_ore, 5)
stage11.add_mob(minecraft.entities.evoker, 4, 1)
stage11.add_mob(minecraft.entities.creeper, 4, 1)
stage11.add_block(minecraft.blocks.jack_o_lantern, 3)
stage11.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_ISOLATED.stage_gift))
stage11.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_ISOLATED.variety_gift))
stage11.add_chest_gift(constant.GIFT_RARE, min_times=1, max_times=1)
stage11.add_chest_gift(constant.GIFT_ODD, min_times=1, max_times=1)
sub_provider.add_phase("11", stage11)

# 12
stage12 = PhaseTableBuilder(count=750, end_gift=constant.STAGE_DEPTH.end_gift)
stage12.add_block(minecraft.blocks.deepslate, 150)
stage12.add_block(minecraft.blocks.cobbled_deepslate, 69)
stage12.add_block(minecraft.blocks.tuff, 20)
stage12.add_block(minecraft.blocks.oak_log, 3)
stage12.add_block(minecraft.blocks.reinforced_deepslate, 5)
stage12.add_block(minecraft.blocks.sculk_catalyst, 7)
stage12.add_block(minecraft.blocks.sculk, 20)
stage12.add_block(minecraft.blocks.budding_amethyst, 6)
stage12.add_block(minecraft.blocks.amethyst_block, 10)
stage12.add_block(minecraft.blocks.smooth_basalt, 12)
stage12.add_block(minecraft.blocks.calcite, 10)
stage12.add_mob(minecraft.entities.zombie, 2, 3)
stage12.add_mob(minecraft.entities.skeleton, 2, 1)
stage12.add_block(minecraft.blocks.deepslate_gold_ore, 15)
stage12.add_block(minecraft.blocks.deepslate_lapis_ore, 15)
stage12.add_block(minecraft.blocks.deepslate_iron_ore, 13)
stage12.add_block(minecraft.blocks.deepslate_emerald_ore, 12)
stage12.add_block(minecraft.blocks.deepslate_copper_ore, 3)
stage12.add_block(minecraft.blocks.deepslate_redstone_ore, 8)
stage12.add_mob(minecraft.entities.creeper, 2, 1)
stage12.add_block(minecraft.blocks.deepslate_diamond_ore, 6)
stage12.add_mob(minecraft.entities.spider, 2, 1)
stage12.add_mob(minecraft.entities.glow_squid, 3, 1)
stage12.add_mob(minecraft.entities.warden, 1, 1)
stage12.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_DEPTH.stage_gift))
stage12.add_chest_gift(constant.GIFT_RARE, min_times=1, max_times=1)
stage12.add_chest_gift(constant.GIFT_MUSICAL, min_times=1, max_times=1)
sub_provider.add_phase("12", stage12)

# 13
stage13 = PhaseTableBuilder(count=850, end_gift=constant.STAGE_END.end_gift)
stage13.add_entry(PhaseEntryBuilder(type_c=constant.TYPE_TEMPLATE, id_c="oneblock:end_portal")
.set_precedence(1, 1)
.set_offset(-2, -4, -2)
.add_preprocessing(PhaseEntryBuilder(type_c=constant.TYPE_BLOCK, id_c=minecraft.blocks.end_stone))
.add_preprocessing(
    PhaseEntryBuilder(type_c=constant.TYPE_SOUND, id_c="minecraft:block.end_portal.spawn"))
)
stage13.add_block(minecraft.blocks.end_stone, 219)
stage13.add_block(minecraft.blocks.end_stone_bricks, 160)
stage13.add_block(minecraft.blocks.purpur_block, 124)
stage13.add_block(minecraft.blocks.purpur_pillar, 115)
stage13.add_mob(minecraft.entities.endermite, 6, 2)
stage13.add_mob(minecraft.entities.enderman, 10, 1)
stage13.add_block(minecraft.blocks.iron_ore, 15)
stage13.add_block(minecraft.blocks.coal_ore, 15)
stage13.add_block(minecraft.blocks.gold_ore, 12)
stage13.add_block(minecraft.blocks.obsidian, 11)
stage13.add_block(minecraft.blocks.redstone_ore, 8)
stage13.add_block(minecraft.blocks.diamond_ore, 6)
stage13.add_block(minecraft.blocks.lapis_ore, 5)
stage13.add_block(minecraft.blocks.emerald_ore, 3)
stage13.add_mob(minecraft.entities.shulker, 2, 2)
stage13.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_END.stage_gift))
stage13.add_entry(
    PhaseEntryBuilder(constant.TYPE_GIFT, minecraft.blocks.chest, weight=2).set_loot_table(
        constant.STAGE_END.variety_gift))
stage13.add_chest_gift(constant.GIFT_RARE, min_times=1, max_times=1)
stage13.add_chest_gift(constant.GIFT_ODD, min_times=1, max_times=1)
stage13.add_chest_gift(constant.GIFT_MUSICAL, min_times=1, max_times=1)
sub_provider.add_phase("13", stage13)

# all
stageall = PhaseTableBuilder(count=-1)
stage13.add_entry(PhaseEntryBuilder(type_c=constant.TYPE_BLOCK, id_c=minecraft.blocks.grass_block)
.add_preprocessing(
    PhaseEntryBuilder(type_c=constant.TYPE_SOUND, id_c="minecraft:music.overworld.cherry_grove")))
stageall.add_block(minecraft.blocks.grass_block, 294)
stageall.add_block(minecraft.blocks.end_stone, 219)
stageall.add_block(minecraft.blocks.quartz_block, 213)
stageall.add_block(minecraft.blocks.cobblestone, 212)
stageall.add_block(minecraft.blocks.stone, 176)
stageall.add_block(minecraft.blocks.end_stone_bricks, 160)
stageall.add_block(minecraft.blocks.stone_bricks, 139)
stageall.add_block(minecraft.blocks.mossy_cobblestone, 128)
stageall.add_block(minecraft.blocks.purpur_block, 124)
stageall.add_block(minecraft.blocks.purpur_pillar, 115)
stageall.add_block(minecraft.blocks.mossy_stone_bricks, 112)
stageall.add_block(minecraft.blocks.sand, 110)
stageall.add_block(minecraft.blocks.red_sand, 103)
stageall.add_block(minecraft.blocks.iron_ore, 103)
stageall.add_block(minecraft.blocks.oak_log, 101)
stageall.add_block(minecraft.blocks.netherrack, 95)
stageall.add_block(minecraft.blocks.gravel, 95)
stageall.add_block(minecraft.blocks.coal_ore, 89)
stageall.add_block(minecraft.blocks.mycelium, 84)
stageall.add_block(minecraft.blocks.red_sandstone, 81)
stageall.add_block(minecraft.blocks.blackstone, 80)
stageall.add_block(minecraft.blocks.prismarine, 77)
stageall.add_block(minecraft.blocks.jungle_log, 70)
stageall.add_block(minecraft.blocks.redstone_ore, 65)
stageall.add_block(minecraft.blocks.cracked_stone_bricks, 59)
stageall.add_block(minecraft.blocks.chiseled_stone_bricks, 59)
stageall.add_block(minecraft.blocks.light_gray_concrete_powder, 58)
stageall.add_mob(minecraft.entities.endermite, 8, 1)
stageall.add_block(minecraft.blocks.gold_ore, 52)
stageall.add_block(minecraft.blocks.soul_sand, 49)
stageall.add_block(minecraft.blocks.prismarine_bricks, 49)
stageall.add_block(minecraft.blocks.nether_bricks, 47)
stageall.add_block(minecraft.blocks.dark_prismarine, 45)
stageall.add_block(minecraft.blocks.snow_block, 44)
stageall.add_block(minecraft.blocks.diorite, 43)
stageall.add_block(minecraft.blocks.terracotta, 40)
stageall.add_block(minecraft.blocks.basalt, 37)
stageall.add_block(minecraft.blocks.red_nether_bricks, 37)
stageall.add_block(minecraft.blocks.sandstone, 36)
stageall.add_block(minecraft.blocks.dark_oak_log, 35)
stageall.add_block(minecraft.blocks.emerald_ore, 33)
stageall.add_block(minecraft.blocks.lapis_ore, 33)
stageall.add_block(minecraft.blocks.dirt, 33)
stageall.add_block(minecraft.blocks.andesite, 33)
stageall.add_block(minecraft.blocks.granite, 32)
stageall.add_block(minecraft.blocks.magma_block, 31)
stageall.add_block(minecraft.blocks.clay, 31)
stageall.add_block(minecraft.blocks.warped_nylium, 30)
stageall.add_block(minecraft.blocks.crimson_nylium, 29)
stageall.add_block(minecraft.blocks.diamond_ore, 26)
stageall.add_block(minecraft.blocks.acacia_log, 25)
stageall.add_block(minecraft.blocks.birch_log, 25)
stageall.add_block(minecraft.blocks.brown_terracotta, 24)
stageall.add_block(minecraft.blocks.spruce_log, 24)
stageall.add_block(minecraft.blocks.obsidian, 23)
stageall.add_block(minecraft.blocks.orange_terracotta, 23)
stageall.add_block(minecraft.blocks.red_terracotta, 23)
stageall.add_block(minecraft.blocks.yellow_terracotta, 23)
stageall.add_block(minecraft.blocks.soul_soil, 21)
stageall.add_block(minecraft.blocks.glowstone, 19)
stageall.add_mob(minecraft.entities.enderman, 10, 1)
stageall.add_block(minecraft.blocks.nether_quartz_ore, 18)
stageall.add_block(minecraft.blocks.shroomlight, 17)
stageall.add_block(minecraft.blocks.nether_wart_block, 17)
stageall.add_block(minecraft.blocks.warped_wart_block, 17)
stageall.add_block(minecraft.blocks.light_gray_terracotta, 17)
stageall.add_block(minecraft.blocks.white_terracotta, 17)
stageall.add_block(minecraft.blocks.packed_ice, 17)
stageall.add_mob(minecraft.entities.slime, 10, 1)
stageall.add_mob(minecraft.entities.bee, 2, 1)
stageall.add_block(minecraft.blocks.gilded_blackstone, 16)
stageall.add_mob(minecraft.entities.husk, 16, 1)
stageall.add_mob(minecraft.entities.skeleton, 15, 1)
stageall.add_block(minecraft.blocks.sea_lantern, 14)
stageall.add_mob(minecraft.entities.stray, 14, 1)
stageall.add_block(minecraft.blocks.bone_block, 13)
stageall.add_block(minecraft.blocks.sponge, 13)
stageall.add_mob(minecraft.entities.cave_spider, 12, 1)
stageall.add_mob(minecraft.entities.silverfish, 12, 1)
stageall.add_block(minecraft.blocks.nether_gold_ore, 12)
stageall.add_block(minecraft.blocks.fire_coral_block, 12)
stageall.add_block(minecraft.blocks.horn_coral_block, 11)
stageall.add_block(minecraft.blocks.honeycomb_block, 10)
stageall.add_block(minecraft.blocks.tube_coral_block, 10)
stageall.add_block(minecraft.blocks.bubble_coral_block, 10)
stageall.add_block(minecraft.blocks.brain_coral_block, 10)
stageall.add_mob(minecraft.entities.fox, 2, 1)
stageall.add_block(minecraft.blocks.melon, 10)
stageall.add_mob(minecraft.entities.magma_cube, 9, 1)
stageall.add_block(minecraft.blocks.podzol, 9)
stageall.add_mob(minecraft.items.rabbit, 2, 1)
stageall.add_mob(minecraft.entities.cat, 1, 1)
stageall.add_mob(minecraft.entities.blaze, 6, 1)
stageall.add_mob(minecraft.entities.hoglin, 6, 1)
stageall.add_mob(minecraft.entities.piglin, 6, 1)
stageall.add_mob(minecraft.entities.pillager, 6, 1)
stageall.add_mob(minecraft.entities.witch, 6, 1)
stageall.add_mob(minecraft.entities.ocelot, 6, 1)
stageall.add_mob(minecraft.entities.vex, 6, 1)
stageall.add_mob(minecraft.entities.parrot, 6, 1)
stageall.add_mob(minecraft.entities.guardian, 6, 1)
stageall.add_mob(minecraft.entities.creeper, 6, 1)
stageall.add_mob(minecraft.entities.zombie, 6, 1)
stageall.add_block(minecraft.blocks.pumpkin, 6)
stageall.add_mob(minecraft.entities.evoker, 4, 1)
stageall.add_mob(minecraft.entities.phantom, 4, 1)
stageall.add_mob(minecraft.entities.mule, 4, 1)
stageall.add_block(minecraft.blocks.slime_block, 4)
stageall.add_block(minecraft.blocks.honey_block, 4)
stageall.add_mob(minecraft.entities.ghast, 4, 1)
stageall.add_mob(minecraft.entities.wither_skeleton, 4, 1)
stageall.add_block(minecraft.blocks.ancient_debris, 4)
stageall.add_mob(minecraft.entities.vindicator, 4, 1)
stageall.add_mob(minecraft.entities.donkey, 4, 1)
stageall.add_mob(minecraft.entities.villager, 4, 1)
stageall.add_mob(minecraft.entities.llama, 4, 1)
stageall.add_mob(minecraft.entities.horse, 4, 1)
stageall.add_mob(minecraft.items.cod, 4, 1)
stageall.add_mob(minecraft.items.tropical_fish, 4, 1)
stageall.add_mob(minecraft.items.salmon, 4, 1)
stageall.add_mob(minecraft.entities.drowned, 4, 1)
stageall.add_mob(minecraft.entities.turtle, 4, 1)
stageall.add_mob(minecraft.entities.spider, 4, 1)
stageall.add_mob(minecraft.items.chicken, 4, 1)
stageall.add_block(minecraft.blocks.jack_o_lantern, 3)
stageall.add_block(minecraft.blocks.crying_obsidian, 3)
stageall.add_mob(minecraft.entities.wolf, 3, 1)
stageall.add_mob(minecraft.entities.pig, 3, 1)
stageall.add_mob(minecraft.entities.shulker, 2, 1)
stageall.add_mob(minecraft.entities.strider, 2, 1)
stageall.add_mob(minecraft.entities.wandering_trader, 2, 1)
stageall.add_mob(minecraft.entities.dolphin, 2, 1)
stageall.add_mob(minecraft.entities.elder_guardian, 2, 1)
stageall.add_mob(minecraft.items.pufferfish, 2, 1)
stageall.add_mob(minecraft.entities.squid, 2, 1)
stageall.add_mob(minecraft.entities.mooshroom, 2, 1)
stageall.add_mob(minecraft.entities.sheep, 2, 1)
stageall.add_mob(minecraft.entities.cow, 2, 1)
stageall.add_mob(minecraft.entities.zombie_horse, 2, 1)
stageall.add_block(minecraft.blocks.bee_nest, 1)
stageall.add_block(minecraft.blocks.beehive, 1)
stageall.add_mob(minecraft.entities.panda, 2, 1)
stageall.add_mob(minecraft.entities.polar_bear, 2, 1)
sub_provider.add_phase("all", stageall)

# 04-gift
loot_provider.add_loot(table_id="04-gift", table=LootTableBuilder()
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.items.tadpole_bucket, 1, 1, 1))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.blocks.clay, 1, 2, 4))
                       )

# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(minecraft.blocks.mangrove_propagule, weight=5).add_count_function(2, 3))
loot04.add_entry(SimplePoolEntryBuilder(minecraft.items.tadpole_bucket, weight=3).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(minecraft.items.salmon, weight=4).add_count_function(2, 3))
loot04.add_entry(SimplePoolEntryBuilder(minecraft.items.salmon_bucket, weight=2).add_count_function(0, 1))
loot04.add_entry(SimplePoolEntryBuilder(minecraft.blocks.lily_pad, weight=3).add_count_function(2, 3))
loot04.add_entry(SimplePoolEntryBuilder(minecraft.blocks.seagrass, weight=3).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table=loot04)

# 10-gift
loot_provider.add_loot(table_id="10-gift", table=LootTableBuilder()
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.items.name_tag, 1, 1, 1))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.blocks.cherry_sapling, 1, 1, 1))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.blocks.pink_petals, 1, 1, 1))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.blocks.glow_berries, 1, 2, 3))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.blocks.pointed_dripstone, 1, 2, 3))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.items.axolotl_bucket, 1, 1, 1))
                       )

# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.cherry_sapling, weight=6).add_count_function(2, 4))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.pink_petals, weight=5).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.glow_berries, weight=4).add_count_function(1, 3))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.pointed_dripstone, weight=3).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.dripstone_block, weight=1).add_count_function(1, 2))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.items.brush, weight=3).add_count_function(1, 3))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.decorated_pot, weight=3).add_count_function(1, 3))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.spore_blossom, weight=3).add_count_function(1, 3))
loot10.add_entry(SimplePoolEntryBuilder(minecraft.blocks.hanging_roots, weight=3).add_count_function(1, 3))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table=loot10)

# 12-gift
loot_provider.add_loot(table_id="12-gift", table=LootTableBuilder()
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.items.echo_shard, 1, 4, 5))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.items.experience_bottle, 1, 8, 10))
                       .add_pool(
    LootPoolBuilder(CountBuilder(1, 1), CountBuilder(0, 0)).add_entry_item(minecraft.blocks.sculk_sensor, 1, 1, 1))
                       )

# 12
loot12 = SingleLootTableBuilder()
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.iron_leggings, weight=3).add_count_function(1, 1))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.saddle, weight=3).add_count_function(1, 1))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.bone, weight=6).add_count_function(2, 4))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.book, weight=6).add_count_function(2, 3))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.leather, weight=5).add_count_function(2, 3))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.echo_shard, weight=1).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.gunpowder, weight=3).add_count_function(1, 2))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.items.emerald, weight=4).add_count_function(2, 3))
loot12.add_entry(SimplePoolEntryBuilder(minecraft.blocks.string, weight=1).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_DEPTH.stage_gift], table_id="12", table=loot12)
