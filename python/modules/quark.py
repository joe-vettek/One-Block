from mods import quark
from core.provider import *
from core import constant

mod_id = "quark"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

sub_provider.add_phase_target( SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
                       .add_mob(quark.entities.foxhound, 2, 1))


sub_provider.add_phase_target( SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
                       .add_mob(quark.entities.shiba, 2, 1))

loot_provider.add_modified_loot(target=[constant.STAGE_COLD.stage_gift], table_id="cold", table=SingleLootTableBuilder()
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.blue_blossom_sapling, weight=4).add_count_function(1, 2))
                                )

loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift], table_id="swamp", table=SingleLootTableBuilder()
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.lavender_blossom_sapling, weight=4).add_count_function(1, 2))
                                )

loot_provider.add_modified_loot(target=[constant.STAGE_HOT.stage_gift], table_id="hot", table=SingleLootTableBuilder()
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.orange_blossom_sapling, weight=4).add_count_function(1, 2))
                                )
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift], table_id="village", table=SingleLootTableBuilder()
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.yellow_blossom_sapling, weight=4).add_count_function(1, 2))
                                )
loot_provider.add_modified_loot(target=[constant.STAGE_ISOLATED.stage_gift], table_id="isolated", table=SingleLootTableBuilder()
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.red_blossom_sapling, weight=4).add_count_function(1, 2))
                                )

loot_provider.add_modified_loot(target=[constant.STAGE_DEPTH.stage_gift], table_id="depth", table=SingleLootTableBuilder()
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.glow_shroom, weight=4).add_count_function(1, 2))
                                .add_entry(SimplePoolEntryBuilder(quark.blocks.ancient_sapling, weight=2).add_count_function(1, 1))
                                )