from core.provider import *
from core import constant

mod_id = "test"
run_list = []

run_list.append(DataPackProvider(mod_id))
sub_config_provider = SubConfigProvider(mod_id)
run_list.append(sub_config_provider)

sub_provider = PhaseProvider(mod_id)
run_list.append(sub_provider)

sub_config_provider.add_config(SubConfigTableBuilder().add_sub(
    sub_provider.get_phase_res("test"), 0, constant.STAGE_HOT.get_phase_id()
))

# 02
stage02 = PhaseTableBuilder(count=1).set_disable_message(True).set_bedrock_time(1)
stage02.add_block("minecraft:lapis_ore", 1)
sub_provider.add_phase("test", stage02)
