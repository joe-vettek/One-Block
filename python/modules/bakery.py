from core.provider import *
from core import constant
mod_id = "bakery"
run_list = []

run_list.append(DataPackProvider(mod_id))

sub_provider=PhaseProvider(mod_id)
run_list.append(sub_provider)

# 10
stage10 = SubPhaseTableBuilder(target=constant.STAGE_10.get_phase_id())
stage10.add_block("bakery:strawberry_crate", 3)
stage10.add_block("bakery:oat_crate", 4)
sub_provider.add_phase("10", stage10)
