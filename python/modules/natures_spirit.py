from core.provider import *
from core import constant
mod_id = "natures_spirit"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_02.get_phase_id())
stage02.add_block("natures_spirit:travertine", 2)
stage02.add_block("natures_spirit:cobbled_travertine", 2)
stage02.add_block("natures_spirit:mossy_cobbled_travertine", 2)
sub_provider.add_phase("02", stage02)


# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_03.get_phase_id())
stage03.add_block("natures_spirit:fir_log", 5)
stage03.add_block("natures_spirit:redwood_log", 5)
stage03.add_block("natures_spirit:cedar_log", 5)
stage03.add_block("natures_spirit:red_moss_block", 4)
sub_provider.add_phase("03", stage03)


# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_04.get_phase_id())
stage04.add_block("natures_spirit:willow_log", 5)
stage04.add_block("natures_spirit:wisteria_log", 5)
sub_provider.add_phase("04", stage04)


# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_05.get_phase_id())
stage05.add_block("natures_spirit:coconut_log", 5)
stage05.add_block("natures_spirit:mahogany_log", 5)
sub_provider.add_phase("05", stage05)


# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_07.get_phase_id())
stage07.add_block("natures_spirit:aspen_log", 5)
stage07.add_block("natures_spirit:maple_log", 5)
stage07.add_block("natures_spirit:palo_verde_log", 5)
stage07.add_block("natures_spirit:joshua_log", 5)
stage07.add_block("natures_spirit:ghaf_log", 5)
stage07.add_block("natures_spirit:saxaul_log", 5)
stage07.add_block("natures_spirit:sandy_soil", 5)
stage07.add_block("natures_spirit:pink_sand", 5)
stage07.add_block("natures_spirit:pink_sandstone", 4)
stage07.add_block("natures_spirit:chert", 4)
sub_provider.add_phase("07", stage07)


# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_10.get_phase_id())
stage10.add_block("natures_spirit:sugi_log", 5)
sub_provider.add_phase("10", stage10)


# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_11.get_phase_id())
stage11.add_block("natures_spirit:cypress_log", 5)
stage11.add_block("natures_spirit:larch_log", 5)
stage11.add_block("natures_spirit:olive_log", 5)
sub_provider.add_phase("11", stage11)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
loot03 = SingleLootTableBuilder()
loot03.add_entry(PoolEntryBuilder("natures_spirit:fir_sapling", weight=4).add_count_function(1, 2))
loot03.add_entry(PoolEntryBuilder("natures_spirit:redwood_sapling", weight=4).add_count_function(1, 2))
loot03.add_entry(PoolEntryBuilder("natures_spirit:frigid_grass", weight=3).add_count_function(1, 1))
loot03.add_entry(PoolEntryBuilder("natures_spirit:cedar_sapling", weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_03.stage_gift], table_id="03", table= loot03)


# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(PoolEntryBuilder("natures_spirit:willow_sapling", weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder("natures_spirit:white_wisteria_sapling", weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder("natures_spirit:blue_wisteria_sapling", weight=3).add_count_function(1, 1))
loot04.add_entry(PoolEntryBuilder("natures_spirit:pink_wisteria_sapling", weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder("natures_spirit:purple_wisteria_sapling", weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder("natures_spirit:helvola_pad", weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder("natures_spirit:lotus_flower", weight=4).add_count_function(1, 2))
loot04.add_entry(PoolEntryBuilder("natures_spirit:lotus_stem", weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_04.stage_gift], table_id="04", table= loot04)


# 05
loot05 = SingleLootTableBuilder()
loot05.add_entry(PoolEntryBuilder("natures_spirit:coconut_sprout", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("natures_spirit:mahogany_sapling", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_05.stage_gift], table_id="05", table= loot05)


# 07
loot07 = SingleLootTableBuilder()
loot07.add_entry(PoolEntryBuilder("natures_spirit:marigold", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:red_maple_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:saxaul_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:aspen_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:ghaf_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:orange_maple_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:yellow_maple_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:palo_verde_sapling", weight=6).add_count_function(2, 4))
loot07.add_entry(PoolEntryBuilder("natures_spirit:joshua_sapling", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_07.stage_gift], table_id="07", table= loot07)


# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(PoolEntryBuilder("natures_spirit:sugi_sapling", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_10.stage_gift], table_id="10", table= loot10)


# 11
loot11 = SingleLootTableBuilder()
loot11.add_entry(PoolEntryBuilder("natures_spirit:olive_sapling", weight=6).add_count_function(2, 4))
loot11.add_entry(PoolEntryBuilder("natures_spirit:cypress_sapling", weight=6).add_count_function(2, 4))
loot11.add_entry(PoolEntryBuilder("natures_spirit:larch_sapling", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_11.stage_gift], table_id="11", table= loot11)
