from core.provider import *
from core import constant
mod_id = "beachparty"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_05.get_phase_id())
stage05.add_block("beachparty:sand_dirty", 4)
stage05.add_block("beachparty:sand_seastars", 4)
stage05.add_block("beachparty:sandwaves", 4)
stage05.add_block("beachparty:palm_log", 6)
sub_provider.add_phase("05", stage05)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 05
loot05 = SingleLootTableBuilder()
loot05.add_entry(PoolEntryBuilder("beachparty:palm_sapling", weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_05.stage_gift], table_id="05", table= loot05)
