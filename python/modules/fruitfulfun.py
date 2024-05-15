from mods import fruitfulfun
from core.provider import *
from core import constant
mod_id = "fruitfulfun"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(fruitfulfun.blocks.citrus_log, 8)
sub_provider.add_phase("10", stage10)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(PoolEntryBuilder(fruitfulfun.blocks.tangerine_sapling, weight=6).add_count_function(2, 4))
loot10.add_entry(PoolEntryBuilder(fruitfulfun.blocks.lime_sapling, weight=6).add_count_function(2, 4))
loot10.add_entry(PoolEntryBuilder(fruitfulfun.blocks.citron_sapling, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)
