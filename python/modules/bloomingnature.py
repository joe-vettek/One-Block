from mods import bloomingnature
from core.provider import *
from core import constant
mod_id = "bloomingnature"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_mob(bloomingnature.entities.pelican, 1, 1)
stage04.add_mob(bloomingnature.entities.muddy_pig, 2, 1)
sub_provider.add_phase("04", stage04)


# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_mob(bloomingnature.entities.red_wolf, 2, 1)
stage06.add_mob(bloomingnature.entities.raccoon, 2, 1)
stage06.add_mob(bloomingnature.entities.turkey, 2, 1)
stage06.add_mob(bloomingnature.entities.owl, 2, 1)
stage06.add_mob(bloomingnature.entities.termite, 2, 1)
sub_provider.add_phase("06", stage06)


# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_mob(bloomingnature.entities.wandering_gardener, 2, 1)
stage07.add_mob(bloomingnature.entities.deer, 2, 1)
stage07.add_mob(bloomingnature.entities.boar, 2, 1)
stage07.add_mob(bloomingnature.entities.bison, 2, 1)
sub_provider.add_phase("07", stage07)


# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage09.add_mob(bloomingnature.entities.squirrel, 2, 1)
sub_provider.add_phase("09", stage09)


# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_mob(bloomingnature.entities.mossy_sheep, 2, 1)
sub_provider.add_phase("11", stage11)
