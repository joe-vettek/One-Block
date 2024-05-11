from core.provider import *
from core import constant
mod_id = "betterend"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 13
stage13 = SubPhaseTableBuilder(target=constant.STAGE_END.get_phase_id())
stage13.add_block("betterend:endstone_dust", 15)
stage13.add_block("betterend:end_mycelium", 15)
stage13.add_block("betterend:end_moss", 15)
stage13.add_block("betterend:chorus_nylium", 15)
stage13.add_block("betterend:cave_moss", 15)
stage13.add_block("betterend:crystal_moss", 15)
stage13.add_block("betterend:shadow_grass", 15)
stage13.add_block("betterend:pink_moss", 15)
stage13.add_block("betterend:amber_moss", 15)
stage13.add_block("betterend:jungle_moss", 15)
stage13.add_block("betterend:sangnum", 15)
stage13.add_block("betterend:rutiscus", 15)
stage13.add_block("betterend:amber_moss", 15)
stage13.add_block("betterend:pallidium_full", 5)
stage13.add_block("betterend:pallidium_heavy", 5)
stage13.add_block("betterend:pallidium_thin", 5)
stage13.add_block("betterend:pallidium_tiny", 5)
stage13.add_block("betterend:mossy_obsidian", 5)
stage13.add_block("betterend:flavolite", 5)
stage13.add_block("betterend:violecite", 5)
stage13.add_block("betterend:sulphuric_rock", 5)
stage13.add_block("betterend:virid_jadestone", 5)
stage13.add_block("betterend:azure_jadestone", 5)
stage13.add_block("betterend:sandy_jadestone", 5)
stage13.add_block("betterend:umbralith", 5)
stage13.add_block("betterend:brimstone", 2)
stage13.add_block("betterend:flavolite_runed", 2)
stage13.add_block("betterend:flavolite_runed_eternal", 1)
stage13.add_block("betterend:dense_snow", 2)
stage13.add_block("betterend:emerald_ice", 2)
stage13.add_block("betterend:mossy_glowshroom_log", 7)
stage13.add_block("betterend:end_lotus_log", 7)
stage13.add_block("betterend:pythadendron_log", 7)
stage13.add_block("betterend:lacugrove_log", 7)
stage13.add_block("betterend:dragon_tree_log", 7)
stage13.add_block("betterend:tenanea_log", 7)
stage13.add_block("betterend:helix_tree_log", 7)
stage13.add_block("betterend:umbrella_tree_log", 7)
stage13.add_block("betterend:umbrella_tree_cluster", 1)
stage13.add_block("betterend:umbrella_tree_cluster_empty", 1)
stage13.add_block("betterend:jellyshroom_cap_purple", 2)
stage13.add_block("betterend:jellyshroom_log", 7)
stage13.add_block("betterend:lucernia_log", 7)
stage13.add_block("betterend:amaranita_stem", 1)
stage13.add_block("betterend:amaranita_hyphae", 1)
stage13.add_block("betterend:amaranita_hymenophore", 12)
stage13.add_block("betterend:amaranita_lantern", 1)
stage13.add_block("betterend:amaranita_cap", 1)
stage13.add_block("betterend:neon_cactus_block", 3)
stage13.add_block("betterend:menger_sponge_wet", 2)
stage13.add_block("betterend:hydralux_petal_block", 1)
stage13.add_block("betterend:hydralux_petal_block_white", 1)
stage13.add_block("betterend:hydralux_petal_block_gray", 1)
stage13.add_block("betterend:hydralux_petal_block_light_gray", 1)
stage13.add_block("betterend:hydralux_petal_block_black", 1)
stage13.add_block("betterend:hydralux_petal_block_blue", 1)
stage13.add_block("betterend:hydralux_petal_block_lime", 1)
stage13.add_block("betterend:hydralux_petal_block_magenta", 1)
stage13.add_block("betterend:hydralux_petal_block_red", 1)
stage13.add_block("betterend:hydralux_petal_block_orange", 1)
stage13.add_block("betterend:hydralux_petal_block_purple", 1)
stage13.add_block("betterend:hydralux_petal_block_cyan", 1)
stage13.add_block("betterend:hydralux_petal_block_brown", 1)
stage13.add_block("betterend:hydralux_petal_block_green", 1)
stage13.add_block("betterend:hydralux_petal_block_yellow", 1)
stage13.add_block("betterend:hydralux_petal_block_pink", 1)
stage13.add_block("betterend:hydralux_petal_block_light_blue", 1)
stage13.add_block("betterend:filalux_lantern", 1)
stage13.add_block("betterend:ender_ore", 2)
stage13.add_block("betterend:amber_ore", 2)
stage13.add_block("betterend:thallasium_ore", 1)
stage13.add_block("betterend:aurora_crystal", 3)
stage13.add_block("betterend:smaragdant_crystal", 1)
stage13.add_block("betterend:budding_smaragdant_crystal", 1)
stage13.add_mob("betterend:dragonfly", 2, 1)
stage13.add_mob("betterend:end_slime", 2, 1)
stage13.add_mob("betterend:end_fish", 2, 1)
stage13.add_mob("betterend:shadow_walker", 2, 1)
stage13.add_mob("betterend:cubozoa", 2, 1)
stage13.add_mob("betterend:silk_moth", 2, 1)
sub_provider.add_phase("13", stage13)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 13
loot13 = SingleLootTableBuilder()
loot13.add_entry(PoolEntryBuilder("betterend:end_lotus_seed", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:lucernia_sapling", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:dragon_tree_sapling", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:pythadendron_sapling", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:mossy_glowshroom_sapling", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:helix_tree_sapling", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:tenanea_sapling", weight=6).add_count_function(2, 4))
loot13.add_entry(PoolEntryBuilder("betterend:umbrella_tree_sapling", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_END.stage_gift], table_id="13", table= loot13)
