from mods import mekanism
from core.provider import *
from core import constant

mod_id = "mekanism"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_UNDERGROUND.get_phase_id())
stage02.add_block(mekanism.blocks.tin_ore, 8)
stage02.add_block(mekanism.blocks.tin_ore, 5)
sub_provider.add_phase("02", stage02)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(mekanism.blocks.tin_ore, 8)
stage03.add_block(mekanism.blocks.tin_ore, 5)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(mekanism.blocks.block_salt, 5)
stage04.add_block(mekanism.blocks.tin_ore, 5)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(mekanism.blocks.block_salt, 5)
stage05.add_block(mekanism.blocks.tin_ore, 5)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(mekanism.blocks.tin_ore, 5)
stage06.add_block(mekanism.blocks.fluorite_ore, 5)
stage06.add_block(mekanism.blocks.lead_ore, 5)
stage06.add_block(mekanism.blocks.osmium_ore, 5)
sub_provider.add_phase("06", stage06)

# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_block(mekanism.blocks.tin_ore, 5)
stage07.add_block(mekanism.blocks.fluorite_ore, 5)
stage07.add_block(mekanism.blocks.lead_ore, 5)
stage07.add_block(mekanism.blocks.osmium_ore, 5)
sub_provider.add_phase("07", stage07)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage09.add_block(mekanism.blocks.tin_ore, 5)
stage09.add_block(mekanism.blocks.fluorite_ore, 5)
stage09.add_block(mekanism.blocks.lead_ore, 5)
stage09.add_block(mekanism.blocks.osmium_ore, 5)
sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(mekanism.blocks.tin_ore, 5)
stage10.add_block(mekanism.blocks.fluorite_ore, 5)
stage10.add_block(mekanism.blocks.lead_ore, 5)
stage10.add_block(mekanism.blocks.osmium_ore, 5)
sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_block(mekanism.blocks.tin_ore, 5)
stage11.add_block(mekanism.blocks.fluorite_ore, 5)
stage11.add_block(mekanism.blocks.lead_ore, 5)
stage11.add_block(mekanism.blocks.osmium_ore, 5)
stage11.add_block(mekanism.blocks.uranium_ore, 5)
sub_provider.add_phase("11", stage11)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(mekanism.blocks.deepslate_fluorite_ore, 20)
stage12.add_block(mekanism.blocks.deepslate_lead_ore, 20)
stage12.add_block(mekanism.blocks.deepslate_tin_ore, 30)
stage12.add_block(mekanism.blocks.deepslate_osmium_ore, 20)
stage12.add_block(mekanism.blocks.deepslate_uranium_ore, 10)
sub_provider.add_phase("12", stage12)

# all
stageall = SubPhaseTableBuilder(target=constant.STAGE_ALL.get_phase_id())
stageall.add_block(mekanism.blocks.deepslate_fluorite_ore, 10)
stageall.add_block(mekanism.blocks.deepslate_lead_ore, 10)
stageall.add_block(mekanism.blocks.deepslate_tin_ore, 15)
stageall.add_block(mekanism.blocks.deepslate_osmium_ore, 10)
stageall.add_block(mekanism.blocks.deepslate_uranium_ore, 5)
stageall.add_block(mekanism.blocks.block_salt, 10)
sub_provider.add_phase("all", stageall)