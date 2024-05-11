from core.provider import *
from core import constant
mod_id = "upgrade_aquatic"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block("upgrade_aquatic:driftwood_log", 8)
stage04.add_mob("upgrade_aquatic:perch", 3, 1)
stage04.add_mob("upgrade_aquatic:pike", 2, 1)
sub_provider.add_phase("04", stage04)


# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block("upgrade_aquatic:driftwood_log", 8)
stage05.add_block("upgrade_aquatic:coralstone", 4)
stage05.add_block("upgrade_aquatic:tube_coralstone", 4)
stage05.add_block("upgrade_aquatic:brain_coralstone", 4)
stage05.add_block("upgrade_aquatic:bubble_coralstone", 4)
stage05.add_block("upgrade_aquatic:fire_coralstone", 4)
stage05.add_block("upgrade_aquatic:horn_coralstone", 4)
stage05.add_block("upgrade_aquatic:acan_coralstone", 4)
stage05.add_block("upgrade_aquatic:finger_coralstone", 4)
stage05.add_block("upgrade_aquatic:star_coralstone", 4)
stage05.add_block("upgrade_aquatic:moss_coralstone", 4)
stage05.add_block("upgrade_aquatic:petal_coralstone", 4)
stage05.add_block("upgrade_aquatic:branch_coralstone", 4)
stage05.add_block("upgrade_aquatic:rock_coralstone", 4)
stage05.add_block("upgrade_aquatic:pillow_coralstone", 4)
stage05.add_block("upgrade_aquatic:silk_coralstone", 4)
stage05.add_block("upgrade_aquatic:chrome_coralstone", 4)
stage05.add_block("upgrade_aquatic:prismarine_coralstone", 2)
stage05.add_block("upgrade_aquatic:elder_prismarine_coralstone", 1)
stage05.add_block("upgrade_aquatic:acan_coral_block", 4)
stage05.add_block("upgrade_aquatic:finger_coral_block", 4)
stage05.add_block("upgrade_aquatic:star_coral_block", 4)
stage05.add_block("upgrade_aquatic:moss_coral_block", 4)
stage05.add_block("upgrade_aquatic:petal_coral_block", 4)
stage05.add_block("upgrade_aquatic:branch_coral_block", 4)
stage05.add_block("upgrade_aquatic:rock_coral_block", 4)
stage05.add_block("upgrade_aquatic:pillow_coral_block", 4)
stage05.add_block("upgrade_aquatic:silk_coral_block", 4)
stage05.add_block("upgrade_aquatic:chrome_coral_block", 4)
stage05.add_block("upgrade_aquatic:prismarine_coral_block", 4)
stage05.add_mob("upgrade_aquatic:lionfish", 2, 1)
stage05.add_mob("upgrade_aquatic:thrasher", 1, 1)
stage05.add_mob("upgrade_aquatic:great_thrasher", 1, 1)
sub_provider.add_phase("05", stage05)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(PoolEntryBuilder("upgrade_aquatic:river_sapling", weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 05
loot05 = SingleLootTableBuilder()
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:silk_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:branch_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:prismarine_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:prismarine_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:branch_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:star_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:moss_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:rock_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:star_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:finger_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:moss_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:petal_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:petal_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:chrome_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:pillow_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:rock_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:chrome_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:acan_coral", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:acan_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:pillow_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:finger_coral_fan", weight=6).add_count_function(2, 4))
loot05.add_entry(PoolEntryBuilder("upgrade_aquatic:silk_coral_fan", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="05", table= loot05)
