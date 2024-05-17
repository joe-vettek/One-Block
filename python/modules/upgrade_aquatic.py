from mods import upgrade_aquatic
from core.provider import *
from core import constant

#  Note not all we need, but we just need to keep the
mod_id = "upgrade_aquatic"
run_list = [DataPackProvider(mod_id)]

sub_provider = PhaseProvider(mod_id)
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
stage05.add_mob(upgrade_aquatic.items.lionfish, 2, 1)
stage05.add_mob(upgrade_aquatic.entities.thrasher, 1, 1)
stage05.add_mob(upgrade_aquatic.entities.great_thrasher, 1, 1)
sub_provider.add_phase("05", stage05)

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 04
loot04 = SingleLootTableBuilder()
loot04.add_entry(SimplePoolEntryBuilder(upgrade_aquatic.blocks.river_sapling, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table=loot04)
