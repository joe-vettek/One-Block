from mods import supplementaries
from core.provider import *
from core import constant

mod_id = "supplementaries"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_mob(supplementaries.entities.red_merchant, 2, 1)
sub_provider.add_phase(constant.STAGE_ISOLATED.id, stage11)

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 06
loot06 = SingleLootTableBuilder(1, 1)
loot06.add_entry(
    SimplePoolEntryBuilder(supplementaries.blocks.flax_seeds, weight=6)
    .add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift,constant.STAGE_ISOLATED.stage_gift],
                                table_id=constant.STAGE_FOREST.id, table=loot06)
