from mods import naturalist
from core.provider import *
from core import constant

mod_id = "naturalist"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)
loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 01
stage01 = SubPhaseTableBuilder(target=constant.STAGE_PLAIN.get_phase_id())
stage01.add_mob(naturalist.entities.butterfly, 1)
sub_provider.add_phase("01", stage01)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_mob(naturalist.entities.robin, 1)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_mob(naturalist.entities.firefly, 2)
stage04.add_mob(naturalist.entities.dragonfly, 2)
stage04.add_mob(naturalist.entities.catfish, 2)
stage04.add_mob(naturalist.entities.alligator, 1)
stage04.add_mob(naturalist.entities.bass, 1)
stage04.add_mob(naturalist.entities.duck, 2)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_mob(naturalist.entities.coral_snake, 2)
stage05.add_mob(naturalist.entities.tortoise, 2)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_mob(naturalist.entities.snail, 2)
stage06.add_mob(naturalist.entities.bear, 2)
stage06.add_mob(naturalist.entities.snake, 2)
stage06.add_mob(naturalist.entities.deer, 2)
stage06.add_mob(naturalist.entities.butterfly, 1)
stage06.add_mob(naturalist.entities.caterpillar, 1)
stage06.add_mob(naturalist.entities.canary, 2)
stage06.add_mob(naturalist.entities.bluejay, 2)
sub_provider.add_phase("06", stage06)

# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_mob(naturalist.entities.rattlesnake, 2)
stage07.add_mob(naturalist.entities.rhino, 2)
stage07.add_mob(naturalist.entities.lion, 2)
stage07.add_mob(naturalist.entities.elephant, 2)
stage07.add_mob(naturalist.entities.zebra, 2)
stage07.add_mob(naturalist.entities.giraffe, 2)
stage07.add_mob(naturalist.entities.hippo, 2)
stage07.add_mob(naturalist.entities.boar, 2)
stage07.add_mob(naturalist.entities.lizard, 2)
stage07.add_mob(naturalist.entities.lizard_tail, 2)
sub_provider.add_phase("07", stage07)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage09.add_mob(naturalist.entities.cardinal, 1)
stage09.add_mob(naturalist.entities.sparrow, 3)
sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_mob(naturalist.entities.finch, 2)
sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_mob(naturalist.entities.vulture, 2)
sub_provider.add_phase("11", stage11)

# 04
loot04 = MultiPoolLootTableBuilder()
loot04.create_new_pool(1, 1)
loot04.add_entry(SimplePoolEntryBuilder(naturalist.blocks.duckweed, weight=4).add_count_function(1, 2))
loot04.add_entry(SimplePoolEntryBuilder(naturalist.blocks.cattail, weight=4).add_count_function(1, 2))
loot04.create_new_pool(1, 1)
loot04.add_entry(SimplePoolEntryBuilder(naturalist.items.bass_bucket, weight=4).add_count_function(1, 1))
loot04.add_entry(SimplePoolEntryBuilder(naturalist.items.catfish_bucket, weight=3).add_count_function(1, 1))
loot_provider.add_modified_loot(target=[constant.STAGE_SWAMP.stage_gift],
                                table_id=constant.STAGE_SWAMP.id, table=loot04)
