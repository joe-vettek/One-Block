from mods import ecologics
from core.provider import *
from core import constant

mod_id = "ecologics"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(ecologics.blocks.thin_ice, 5)
stage03.add_mob(ecologics.entities.penguin, 2)
sub_provider.add_phase("03", stage03)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(ecologics.blocks.coconut_log, 10)
stage05.add_mob(ecologics.entities.coconut_crab, 2)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_mob(ecologics.entities.squirrel, 2)
sub_provider.add_phase(constant.STAGE_FOREST.id, stage06)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage09.add_block(ecologics.blocks.walnut_log, 5)
sub_provider.add_phase("09", stage09)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(ecologics.blocks.azalea_log, 4)
# stage12.add_block(biomesoplenty.blocks.origin_sapling, 8)
sub_provider.add_phase("12", stage12)

# 05
loot05 = MultiPoolLootTableBuilder()
loot05.create_new_pool(1, 1)
loot05.add_entry(SimplePoolEntryBuilder(ecologics.blocks.seashell, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift],
                                table_id=constant.STAGE_OCEAN.id, table=loot05)

# 09
loot09 = MultiPoolLootTableBuilder()
loot09.create_new_pool(0, 1)
loot09.add_entry(SimplePoolEntryBuilder(ecologics.blocks.walnut_sapling, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift],
                                table_id=constant.STAGE_VILLAGE.id, table=loot09)

# 12
loot12 = MultiPoolLootTableBuilder()
loot12.create_new_pool(0, 1)
loot12.add_entry(SimplePoolEntryBuilder(ecologics.blocks.azalea_flower, weight=4).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_DEPTH.stage_gift],
                                table_id=constant.STAGE_DEPTH.id, table=loot12)
