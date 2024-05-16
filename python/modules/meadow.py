from mods import meadow
from core.provider import *
from core import constant

mod_id = "meadow"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(meadow.blocks.limestone, 4)
stage10.add_block(meadow.blocks.mossy_cobbled_limestone, 4)
stage10.add_block(meadow.blocks.pine_log, 4)
stage10.add_mob(meadow.entities.wooly_cow, 2, 1)
stage10.add_mob(meadow.entities.water_buffalo, 2, 1)
sub_provider.add_phase(constant.STAGE_TRAVEL.id, stage10)

# 10
loot10 = MultiPoolLootTableBuilder()
loot10.create_new_pool(0, 1)
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.pine_sapling, 6, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.small_fir, 4, 1, 1))
loot10.create_new_pool(1, 2)
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.alpine_poppy, 4, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.delphinium, 4, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.saxifrage, 4, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.enzian, 4, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.fire_lily, 4, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.eriophorum, 4, 1, 2))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.eriophorum_tall, 3, 1, 2))
loot10.create_new_pool(0, 1)
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.cheesecake, 4, 1, 1))
loot10.add_entry(CountPoolEntryBuilder(meadow.blocks.roasted_ham, 1, 1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift],
                                table_id=constant.STAGE_TRAVEL.id, table=loot10)
