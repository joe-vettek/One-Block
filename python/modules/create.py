from core.provider import *
from core import constant
mod_id = "create"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_02.get_phase_id())
stage02.add_block("create:limestone", 10)
stage02.add_block("create:veridium", 6)
stage02.add_block("create:scoria", 5)
sub_provider.add_phase("02", stage02)


# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_03.get_phase_id())
stage03.add_block("create:zinc_ore", 10)
stage03.add_block("create:veridium", 6)
sub_provider.add_phase("03", stage03)


# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_04.get_phase_id())
stage04.add_block("create:zinc_ore", 10)
stage04.add_block("create:veridium", 6)
sub_provider.add_phase("04", stage04)


# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_05.get_phase_id())
stage05.add_block("create:zinc_ore", 10)
stage05.add_block("create:veridium", 6)
sub_provider.add_phase("05", stage05)


# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_06.get_phase_id())
stage06.add_block("create:zinc_ore", 10)
stage06.add_block("create:veridium", 6)
stage06.add_block("create:scoria", 5)
sub_provider.add_phase("06", stage06)


# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_07.get_phase_id())
stage07.add_block("create:zinc_ore", 16)
stage07.add_block("create:veridium", 6)
stage07.add_block("create:scoria", 5)
sub_provider.add_phase("07", stage07)


# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_07.get_phase_id())
stage08.add_block("create:zinc_ore", 12)
stage08.add_block("create:veridium", 6)
sub_provider.add_phase("08", stage08)


# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_08.get_phase_id())
stage09.add_block("create:zinc_ore", 14)
stage09.add_block("create:veridium", 6)
sub_provider.add_phase("09", stage09)


# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_10.get_phase_id())
stage10.add_block("create:zinc_ore", 16)
stage10.add_block("create:veridium", 6)
sub_provider.add_phase("10", stage10)


# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_11.get_phase_id())
stage11.add_block("create:zinc_ore", 15)
stage11.add_block("create:veridium", 6)
sub_provider.add_phase("11", stage11)


# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_12.get_phase_id())
stage12.add_block("create:deepslate_zinc_ore", 20)
stage12.add_block("create:asurine", 30)
stage12.add_block("create:crimsite", 30)
stage12.add_block("create:ochrum", 8)
sub_provider.add_phase("12", stage12)


# all
stageall = SubPhaseTableBuilder(target=constant.STAGE_ALL.get_phase_id())
stageall.add_block("create:zinc_ore", 10)
stageall.add_block("create:limestone", 16)
stageall.add_block("create:veridium", 6)
stageall.add_block("create:asurine", 30)
stageall.add_block("create:crimsite", 30)
stageall.add_block("create:ochrum", 8)
stageall.add_block("create:scoria", 5)
sub_provider.add_phase("all", stageall)
