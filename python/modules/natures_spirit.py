from mods import natures_spirit
from core.provider import *
from core import constant
mod_id = "natures_spirit"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_UNDERGROUND.get_phase_id())
stage02.add_block(natures_spirit.blocks.travertine, 2)
stage02.add_block(natures_spirit.blocks.cobbled_travertine, 2)
stage02.add_block(natures_spirit.blocks.mossy_cobbled_travertine, 2)
sub_provider.add_phase("02", stage02)


# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(natures_spirit.blocks.fir_log, 5)
stage03.add_block(natures_spirit.blocks.redwood_log, 5)
stage03.add_block(natures_spirit.blocks.cedar_log, 5)
stage03.add_block(natures_spirit.blocks.red_moss_block, 4)
sub_provider.add_phase("03", stage03)


# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(natures_spirit.blocks.willow_log, 5)
stage04.add_block(natures_spirit.blocks.wisteria_log, 5)
sub_provider.add_phase("04", stage04)


# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(natures_spirit.blocks.coconut_log, 5)
stage05.add_block(natures_spirit.blocks.mahogany_log, 5)
sub_provider.add_phase("05", stage05)


# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_block(natures_spirit.blocks.aspen_log, 5)
stage07.add_block(natures_spirit.blocks.maple_log, 5)
stage07.add_block(natures_spirit.blocks.palo_verde_log, 5)
stage07.add_block(natures_spirit.blocks.joshua_log, 5)
stage07.add_block(natures_spirit.blocks.ghaf_log, 5)
stage07.add_block(natures_spirit.blocks.saxaul_log, 5)
stage07.add_block(natures_spirit.blocks.sandy_soil, 5)
stage07.add_block(natures_spirit.blocks.pink_sand, 5)
stage07.add_block(natures_spirit.blocks.pink_sandstone, 4)
stage07.add_block(natures_spirit.blocks.chert, 4)
sub_provider.add_phase("07", stage07)


# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(natures_spirit.blocks.sugi_log, 5)
sub_provider.add_phase("10", stage10)


# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_block(natures_spirit.blocks.cypress_log, 5)
stage11.add_block(natures_spirit.blocks.larch_log, 5)
stage11.add_block(natures_spirit.blocks.olive_log, 5)
sub_provider.add_phase("11", stage11)


loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 03
loot03 = MultiPoolLootTableBuilder()
loot03.create_new_pool(1,2)
loot03.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.fir_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.redwood_sapling, weight=4).add_count_function(1, 2))
loot03.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.frigid_grass, weight=3).add_count_function(1, 1))
loot03.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.cedar_sapling, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="03", table= loot03)


# 04
loot04 = MultiPoolLootTableBuilder()
loot04.create_new_pool(1,2)
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.willow_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.white_wisteria_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.blue_wisteria_sapling, weight=3).add_count_function(1, 1))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.pink_wisteria_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.purple_wisteria_sapling, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.helvola_pad, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.lotus_flower, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.lotus_stem, weight=4).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="04", table= loot04)


# 05
loot05 = MultiPoolLootTableBuilder()
loot05.create_new_pool(1,2)
loot05.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.coconut_sprout, weight=6).add_count_function(2, 4))
loot05.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.mahogany_sapling, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_OCEAN.stage_gift], table_id="05", table= loot05)


# 07
loot07 = MultiPoolLootTableBuilder()
loot07.create_new_pool(1,2)
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.marigold, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.red_maple_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.saxaul_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.aspen_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.ghaf_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.orange_maple_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.yellow_maple_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.palo_verde_sapling, weight=6).add_count_function(2, 4))
loot07.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.joshua_sapling, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="07", table= loot07)


# 10
loot10 = MultiPoolLootTableBuilder()
loot10.create_new_pool(1,2)
loot10.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.sugi_sapling, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)


# 11
loot11 = MultiPoolLootTableBuilder()
loot11.create_new_pool(1,2)
loot11.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.olive_sapling, weight=6).add_count_function(2, 4))
loot11.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.cypress_sapling, weight=6).add_count_function(2, 4))
loot11.add_entry(SimplePoolEntryBuilder(natures_spirit.blocks.larch_sapling, weight=6).add_count_function(2, 4))
loot_provider.add_modified_loot(target=[constant.STAGE_ISOLATED.stage_gift], table_id="11", table= loot11)
