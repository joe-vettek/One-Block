from mods import upgrade_aquatic
from core.provider import *
from core import constant
mod_id = "upgrade_aquatic"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(upgrade_aquatic.blocks.driftwood_log, 8)
stage04.add_mob(upgrade_aquatic.items.perch, 3, 1)
stage04.add_mob(upgrade_aquatic.items.pike, 2, 1)
sub_provider.add_phase("04", stage04)


# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(upgrade_aquatic.blocks.driftwood_log, 8)
stage05.add_block(upgrade_aquatic.blocks.coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.tube_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.brain_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.bubble_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.fire_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.horn_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.acan_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.finger_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.star_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.moss_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.petal_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.branch_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.rock_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.pillow_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.silk_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.chrome_coralstone, 4)
stage05.add_block(upgrade_aquatic.blocks.prismarine_coralstone, 2)
stage05.add_block(upgrade_aquatic.blocks.elder_prismarine_coralstone, 1)
stage05.add_block(upgrade_aquatic.blocks.acan_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.finger_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.star_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.moss_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.petal_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.branch_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.rock_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.pillow_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.silk_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.chrome_coral_block, 4)
stage05.add_block(upgrade_aquatic.blocks.prismarine_coral_block, 4)
stage05.add_mob(upgrade_aquatic.items.lionfish, 2, 1)
stage05.add_mob(upgrade_aquatic.entities.thrasher, 1, 1)
stage05.add_mob(upgrade_aquatic.entities.great_thrasher, 1, 1)
sub_provider.add_phase("05", stage05)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.river_sapling, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 05
loot05 = SingleLootTableBuilder()
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.silk_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.branch_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.prismarine_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.prismarine_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.branch_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.star_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.moss_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.rock_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.star_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.finger_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.moss_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.petal_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.petal_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.chrome_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.pillow_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.rock_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.chrome_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.acan_coral, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.acan_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.pillow_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.finger_coral_fan, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.silk_coral_fan, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="05", table= loot05)
