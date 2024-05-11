from core.provider import *
from core import constant
mod_id = "bloomingnature"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_04.get_phase_id())
stage04.add_mob("bloomingnature:pelican", 1, 1)
stage04.add_mob("bloomingnature:muddy_pig", 2, 1)
sub_provider.add_phase("04", stage04)


# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_06.get_phase_id())
stage06.add_mob("bloomingnature:red_wolf", 2, 1)
stage06.add_mob("bloomingnature:raccoon", 2, 1)
stage06.add_mob("bloomingnature:turkey", 2, 1)
stage06.add_mob("bloomingnature:owl", 2, 1)
stage06.add_mob("bloomingnature:termite", 2, 1)
sub_provider.add_phase("06", stage06)


# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_07.get_phase_id())
stage07.add_mob("bloomingnature:wandering_gardener", 2, 1)
stage07.add_mob("bloomingnature:deer", 2, 1)
stage07.add_mob("bloomingnature:boar", 2, 1)
stage07.add_mob("bloomingnature:bison", 2, 1)
sub_provider.add_phase("07", stage07)


# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_08.get_phase_id())
stage09.add_mob("bloomingnature:squirrel", 2, 1)
sub_provider.add_phase("09", stage09)


# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_11.get_phase_id())
stage11.add_mob("bloomingnature:mossy_sheep", 2, 1)
sub_provider.add_phase("11", stage11)
