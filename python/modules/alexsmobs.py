from mods import alexsmobs
from core.provider import *
from core import constant

mod_id = "alexsmobs"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

# 01
stage01 = SubPhaseTableBuilder(target=constant.STAGE_PLAIN.get_phase_id())
stage01.add_mob(alexsmobs.entities.raccoon, 1)
sub_provider.add_phase("01", stage01)

# 02
stage02 = SubPhaseTableBuilder(target=constant.STAGE_UNDERGROUND.get_phase_id())
stage02.add_mob(alexsmobs.entities.cockroach, 2)
sub_provider.add_phase("02", stage02)
# 03
stage03 = SubPhaseTableBuilder(target=constant.STAGE_COLD.get_phase_id())
stage03.add_mob(alexsmobs.entities.tusklin, 1)
stage03.add_mob(alexsmobs.entities.froststalker, 1)
# imaginary end
stage03.add_mob(alexsmobs.entities.moose, 1)
stage03.add_mob(alexsmobs.entities.snow_leopard, 1)

sub_provider.add_phase("03", stage03)

# 04
stage04 = SubPhaseTableBuilder(target=constant.STAGE_SWAMP.get_phase_id())
stage04.add_mob(alexsmobs.entities.catfish, 1)
stage04.add_mob(alexsmobs.entities.mudskipper, 1)
stage04.add_mob(alexsmobs.entities.rain_frog, 1)
stage04.add_mob(alexsmobs.entities.crocodile, 1)
stage04.add_mob(alexsmobs.entities.alligator_snapping_turtle, 1)
stage04.add_mob(alexsmobs.entities.anaconda, 1)
stage04.add_mob(alexsmobs.entities.terrapin, 1)
stage04.add_mob(alexsmobs.entities.caiman, 1)
stage04.add_mob(alexsmobs.entities.shoebill, 1)
stage04.add_mob(alexsmobs.entities.platypus, 1)
sub_provider.add_phase("04", stage04)

# 05
stage05 = SubPhaseTableBuilder(target=constant.STAGE_OCEAN.get_phase_id())
stage05.add_mob(alexsmobs.entities.orca, 1)
stage05.add_mob(alexsmobs.entities.seal, 1)
stage05.add_mob(alexsmobs.entities.cachalot_whale, 1)
stage05.add_mob(alexsmobs.entities.hammerhead_shark, 1)
stage05.add_mob(alexsmobs.entities.blobfish, 1)
stage05.add_mob(alexsmobs.entities.frilled_shark, 1)
stage05.add_mob(alexsmobs.entities.comb_jelly, 1)
stage05.add_mob(alexsmobs.entities.flying_fish, 1)
stage05.add_mob(alexsmobs.entities.mimic_octopus, 1)
stage05.add_mob(alexsmobs.entities.giant_squid, 1)
stage05.add_mob(alexsmobs.entities.lobster, 1)
stage05.add_mob(alexsmobs.entities.mantis_shrimp, 1)
stage05.add_mob(alexsmobs.entities.skelewag, 1)
stage05.add_mob(alexsmobs.entities.seagull, 1)

sub_provider.add_phase("05", stage05)

# 06
stage06 = SubPhaseTableBuilder(target=constant.STAGE_FOREST.get_phase_id())
stage06.add_mob(alexsmobs.entities.banana_slug, 1)
stage06.add_entry(PhaseEntryBuilder(constant.TYPE_MOB, alexsmobs.entities.leafcutter_ant, 2, 1)
                  .add_preprocessing(PhaseEntryBuilder(constant.TYPE_BLOCK, alexsmobs.blocks.leafcutter_anthill)))
stage06.add_mob(alexsmobs.entities.toucan, 1)
stage06.add_mob(alexsmobs.entities.blue_jay, 1)
stage06.add_mob(alexsmobs.entities.potoo, 1)
stage06.add_mob(alexsmobs.entities.hummingbird, 1)
stage06.add_mob(alexsmobs.entities.grizzly_bear, 1)
stage06.add_mob(alexsmobs.entities.gorilla, 1)
stage06.add_mob(alexsmobs.entities.capuchin_monkey, 1)
stage06.add_mob(alexsmobs.entities.tasmanian_devil, 1)
stage06.add_mob(alexsmobs.entities.tiger, 1)
stage06.add_mob(alexsmobs.entities.anteater, 1)
stage06.add_mob(alexsmobs.entities.bison, 1)
stage06.add_mob(alexsmobs.entities.sugar_glider, 1)
stage06.add_mob(alexsmobs.entities.skunk, 1)

sub_provider.add_phase("06", stage06)

# 07
stage07 = SubPhaseTableBuilder(target=constant.STAGE_HOT.get_phase_id())
stage07.add_mob(alexsmobs.entities.guster, 1)
# imaginary end
stage07.add_mob(alexsmobs.entities.tarantula_hawk, 1)
stage07.add_mob(alexsmobs.entities.triops, 1)
stage07.add_mob(alexsmobs.entities.rattlesnake, 1)
stage07.add_mob(alexsmobs.entities.roadrunner, 1)
stage07.add_mob(alexsmobs.entities.emu, 1)
stage07.add_mob(alexsmobs.entities.gazelle, 1)
stage07.add_mob(alexsmobs.entities.elephant, 1)
stage07.add_mob(alexsmobs.entities.kangaroo, 1)
stage07.add_mob(alexsmobs.entities.maned_wolf, 1)
stage07.add_mob(alexsmobs.entities.gelada_monkey, 1)
stage07.add_mob(alexsmobs.entities.jerboa, 1)
stage07.add_mob(alexsmobs.entities.rhinoceros, 1)

sub_provider.add_phase("07", stage07)

# 08
stage08 = SubPhaseTableBuilder(target=constant.STAGE_NETHER.get_phase_id())
stage08.add_mob(alexsmobs.entities.bone_serpent, 1)
stage08.add_mob(alexsmobs.entities.crimson_mosquito, 2)
stage08.add_mob(alexsmobs.entities.warped_toad, 1)
stage08.add_mob(alexsmobs.entities.soul_vulture, 1)
stage08.add_mob(alexsmobs.entities.dropbear, 1)
stage08.add_mob(alexsmobs.entities.straddler, 1)
stage08.add_mob(alexsmobs.entities.stradpole, 1)
stage08.add_mob(alexsmobs.entities.warped_mosco, 1)
stage08.add_mob(alexsmobs.entities.laviathan, 1)
# imaginary end
sub_provider.add_phase("08", stage08)

# 09
stage09 = SubPhaseTableBuilder(target=constant.STAGE_VILLAGE.get_phase_id())
stage09.add_mob(alexsmobs.entities.crow, 1)
sub_provider.add_phase("09", stage09)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_TRAVEL.get_phase_id())
stage10.add_mob(alexsmobs.entities.sunbird, 1)
# imaginary end
stage10.add_mob(alexsmobs.entities.bald_eagle, 1)

sub_provider.add_phase("10", stage10)

# 11
stage11 = SubPhaseTableBuilder(target=constant.STAGE_ISOLATED.get_phase_id())
stage11.add_mob(alexsmobs.entities.bunfungus, 1)
stage11.add_mob(alexsmobs.entities.mungus, 1)
# imaginary end
stage11.add_mob(alexsmobs.entities.komodo_dragon, 1)
sub_provider.add_phase("11", stage11)

# 12
stage12 = SubPhaseTableBuilder(target=constant.STAGE_DEPTH.get_phase_id())
stage12.add_mob(alexsmobs.entities.murmur, 1)
stage12.add_mob(alexsmobs.entities.underminer, 1)
stage12.add_mob(alexsmobs.entities.skreecher, 1)
stage12.add_mob(alexsmobs.entities.farseer, 1)
stage12.add_mob(alexsmobs.entities.flutter, 1)
stage12.add_mob(alexsmobs.entities.rocky_roller, 1)
stage12.add_mob(alexsmobs.entities.centipede_head, 1)
# imaginary end
stage12.add_mob(alexsmobs.entities.devils_hole_pupfish, 1)
sub_provider.add_phase("12", stage12)

# 13
stage13 = SubPhaseTableBuilder(target=constant.STAGE_END.get_phase_id())
stage13.add_mob(alexsmobs.entities.endergrade, 1)
stage13.add_mob(alexsmobs.entities.mimicube, 1)
stage13.add_mob(alexsmobs.entities.spectre, 1)
stage13.add_mob(alexsmobs.entities.enderiophage, 1)
stage13.add_mob(alexsmobs.entities.cosmaw, 1)
stage13.add_mob(alexsmobs.entities.cosmic_cod, 1)
# imaginary end
sub_provider.add_phase("13", stage13)
