from mods import autumnity
from core.provider import *
from core import constant

mod_id = "autumnity"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# forest
stage_forest = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage_forest.set_add_count(25)
stage_forest.add_block(autumnity.blocks.maple_log, 7)
stage_forest.add_block(autumnity.blocks.sappy_maple_log, 1)
stage_forest.add_block(autumnity.blocks.large_pumpkin_slice, 3)
stage_forest.add_mob(autumnity.entities.snail, 2, 1)
stage_forest.add_mob(autumnity.entities.turkey, 2, 1)
sub_provider.add_phase(constant.STAGE_FOREST.id, stage_forest)

# forest
loot_forest = LootTableBuilder()
loot_forest_pool_sapling = LootPoolBuilder(CountBuilder(1, 2))
loot_forest_pool_sapling.add_entry(SimplePoolEntryBuilder(autumnity.blocks.maple_sapling, weight=4).add_count_function(1, 2))
loot_forest_pool_sapling.add_entry(SimplePoolEntryBuilder(autumnity.blocks.maple_sapling, weight=4).add_count_function(1, 2))
loot_forest_pool_sapling.add_entry(SimplePoolEntryBuilder(autumnity.blocks.maple_sapling, weight=4).add_count_function(1, 2))
loot_forest.add_pool(loot_forest_pool_sapling)
loot_forest_pool_flower = LootPoolBuilder(CountBuilder(0, 1))
loot_forest_pool_flower.add_entry(SimplePoolEntryBuilder(autumnity.blocks.autumn_crocus, weight=4).add_count_function(1, 2))
loot_forest_pool_flower.add_entry(SimplePoolEntryBuilder(autumnity.blocks.foul_berries, weight=4).add_count_function(1, 2))
loot_forest.add_pool(loot_forest_pool_flower)
loot_provider.add_modified_loot(target=[constant.STAGE_FOREST.stage_gift],
                                table_id=constant.STAGE_FOREST.id, table=loot_forest)
