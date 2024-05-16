from mods import candlelight
from core.provider import *
from core import constant
mod_id = "candlelight"
run_list = []

run_list.append(DataPackProvider(mod_id))

loot_provider = ModifiedLootTableProvider(mod_id)
run_list.append(loot_provider)

# 09
loot09 = SingleLootTableBuilder()
loot09.add_entry(SimplePoolEntryBuilder(candlelight.blocks.tomato_seeds, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_VILLAGE.stage_gift], table_id="09", table= loot09)


# 10
loot10 = SingleLootTableBuilder()
loot10.add_entry(SimplePoolEntryBuilder(candlelight.blocks.lettuce_seeds, weight=6).add_count_function(1, 2))
loot_provider.add_modified_loot(target=[constant.STAGE_TRAVEL.stage_gift], table_id="10", table= loot10)
