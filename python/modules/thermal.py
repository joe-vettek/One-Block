from mods import thermal
from core.provider import *
from core import constant

mod_id = "thermal"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_UNDERGROUND.get_phase_id())
stage02.add_block(thermal.blocks.tin_ore, 6)
stage02.add_block(thermal.blocks.apatite_ore, 6)
stage02.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("02", stage02)

# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_block(thermal.blocks.tin_ore, 6)
stage03.add_block(thermal.blocks.apatite_ore, 6)
stage03.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_block(thermal.blocks.nickel_ore, 4)
stage04.add_block(thermal.blocks.tin_ore, 6)
stage04.add_block(thermal.blocks.apatite_ore, 6)
stage04.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_block(thermal.blocks.niter_ore, 4)
stage05.add_block(thermal.blocks.lead_ore, 4)
stage05.add_block(thermal.blocks.nickel_ore, 4)
stage05.add_block(thermal.blocks.oil_sand, 4)
stage05.add_block(thermal.blocks.tin_ore, 6)
stage05.add_block(thermal.blocks.apatite_ore, 6)
stage05.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_block(thermal.blocks.cinnabar_ore, 4)
stage06.add_block(thermal.blocks.sulfur_ore, 4)
stage06.add_block(thermal.blocks.niter_ore, 4)
stage06.add_block(thermal.blocks.lead_ore, 4)
stage06.add_block(thermal.blocks.nickel_ore, 4)
stage06.add_block(thermal.blocks.tin_ore, 6)
stage06.add_block(thermal.blocks.apatite_ore, 6)
stage06.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("06", stage06)

# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_block(thermal.blocks.oil_red_sand, 4)
stage07.add_block(thermal.blocks.cinnabar_ore, 4)
stage07.add_block(thermal.blocks.sulfur_ore, 4)
stage07.add_block(thermal.blocks.niter_ore, 4)
stage07.add_block(thermal.blocks.lead_ore, 4)
stage07.add_block(thermal.blocks.nickel_ore, 4)
stage07.add_block(thermal.blocks.tin_ore, 6)
stage07.add_block(thermal.blocks.apatite_ore, 6)
stage07.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("07", stage07)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage09.add_block(thermal.blocks.cinnabar_ore, 4)
stage09.add_block(thermal.blocks.sulfur_ore, 4)
stage09.add_block(thermal.blocks.niter_ore, 4)
stage09.add_block(thermal.blocks.lead_ore, 4)
stage09.add_block(thermal.blocks.nickel_ore, 4)
stage09.add_block(thermal.blocks.tin_ore, 6)
stage09.add_block(thermal.blocks.apatite_ore, 6)
stage09.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_block(thermal.blocks.cinnabar_ore, 4)
stage10.add_block(thermal.blocks.sulfur_ore, 4)
stage10.add_block(thermal.blocks.niter_ore, 4)
stage10.add_block(thermal.blocks.lead_ore, 4)
stage10.add_block(thermal.blocks.nickel_ore, 4)
stage10.add_block(thermal.blocks.tin_ore, 6)
stage10.add_block(thermal.blocks.apatite_ore, 6)
stage10.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_block(thermal.blocks.cinnabar_ore, 4)
stage11.add_block(thermal.blocks.sulfur_ore, 4)
stage11.add_block(thermal.blocks.niter_ore, 4)
stage11.add_block(thermal.blocks.lead_ore, 4)
stage11.add_block(thermal.blocks.nickel_ore, 4)
stage11.add_block(thermal.blocks.tin_ore, 6)
stage11.add_block(thermal.blocks.apatite_ore, 6)
stage11.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("11", stage11)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_block(thermal.blocks.cinnabar_ore, 4)
stage12.add_block(thermal.blocks.sulfur_ore, 4)
stage12.add_block(thermal.blocks.niter_ore, 4)
stage12.add_block(thermal.blocks.lead_ore, 4)
stage12.add_block(thermal.blocks.nickel_ore, 4)
stage12.add_block(thermal.blocks.tin_ore, 6)
stage12.add_block(thermal.blocks.apatite_ore, 6)
stage12.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("12", stage12)

# all
stageall = SubPhaseTableBuilder(target=constant.STAGE_ALL.get_phase_id())
stageall.add_block(thermal.blocks.cinnabar_ore, 4)
stageall.add_block(thermal.blocks.sulfur_ore, 4)
stageall.add_block(thermal.blocks.niter_ore, 4)
stageall.add_block(thermal.blocks.lead_ore, 4)
stageall.add_block(thermal.blocks.nickel_ore, 4)
stageall.add_block(thermal.blocks.tin_ore, 6)
stageall.add_block(thermal.blocks.apatite_ore, 6)
stageall.add_block(thermal.blocks.tin_ore, 6)
sub_provider.add_phase("all", stageall)
