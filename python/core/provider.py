import json
import os.path

from os.path import join
from typing import List

from core import util, constant


class AbstractProvider:

    def __init__(self, mod_id: str):
        self.mod_id = mod_id
        self.table = {}

    @util.test_time
    def run(self):
        print(f"Now run in {self.get_location()}")
        for p in self.table:
            util.save_json(p, self.table[p], make_dirs=True)

    def add(self, path, d: dict):
        self.table[path] = d

    def get_location(self) -> str:
        raise NotImplementedError


class DataPackProvider(AbstractProvider):

    def __init__(self, mod_id: str):
        super().__init__(mod_id)

    def get_root(self):
        return "datapacks"

    def get_datapack_name(self):
        return f"oneblock-extra-{self.mod_id}"

    def get_mcmeta_path(self):
        return os.path.join(self.get_root(), self.get_datapack_name(), "pack.mcmeta")

    def get_data_path(self, filename):
        return os.path.join(self.get_root(), self.get_datapack_name(), "data", self.get_datapack_name(), filename)

    def get_data_base_path(self, filename):
        return os.path.join(self.get_root(), self.get_datapack_name(), "data", filename)

    def run(self):
        if type(self) == DataPackProvider:
            self.add_meta()
        super().run()

    def get_location(self):
        return f"DataPacksProvider {self.mod_id}"

    def add_meta(self):
        meta = {
            "pack": {
                "_comment": "Auto build by joe-vettek python tool",
                "description": f"oneblock compat resources for {self.mod_id}",
                "pack_format": 9
            }
        }
        self.add(self.get_mcmeta_path(), meta)


class CountBuilder(dict):
    def __init__(self, min_c: int = 0, max_c: int = 1):
        super().__init__()
        self["min"] = min_c
        self["max"] = max_c


class CountFunctionBuilder(dict):
    def __init__(self, min_c: int = 0, max_c: int = 1):
        super().__init__()
        self["count"] = CountBuilder(min_c, max_c)
        self["function"] = "minecraft:set_count"


class PoolEntryBuilder(dict):
    def __init__(self, name: str, weight: int = 6, use_default_functions=True):
        super().__init__()
        self["type"] = "minecraft:item"
        self["name"] = name
        self["weight"] = weight
        self["functions"] = [] if not use_default_functions else [CountFunctionBuilder(1, 2)]

    def add_function(self, function):
        self["functions"].append(function)
        return self

    def add_count_function(self, min_c, max_c):
        self.add_function(CountFunctionBuilder(min_c, max_c))
        return self


class LootPoolBuilder(dict):
    def __init__(self, rolls: CountBuilder = None, bonus_rolls: CountBuilder = None):
        super().__init__()
        if rolls is None:
            rolls = CountBuilder(2, 3)
        if bonus_rolls is None:
            bonus_rolls = CountBuilder(0, 1)
        self["rolls"] = rolls
        self["bonus_rolls"] = bonus_rolls
        self["entries"] = []

    def add_entry(self, entry: PoolEntryBuilder):
        self["entries"].append(entry)
        return self


class LootTableBuilder(dict):
    def __init__(self):
        super().__init__()
        self["type"] = "minecraft:chest"
        self["pools"] = []

    def add_pool(self, pool: LootPoolBuilder):
        self["pools"].append(pool)
        return self


class SingleLootTableBuilder(LootTableBuilder):
    def __init__(self, rolls_min=2, rolls_max=3, bonus_rolls_min=0, bonus_rolls_max=1):
        super().__init__()
        self.add_pool(
            LootPoolBuilder(CountBuilder(rolls_min, rolls_max), CountBuilder(bonus_rolls_min, bonus_rolls_max)))

    def add_entry(self, entry: PoolEntryBuilder):
        self["pools"][0]["entries"].append(entry)
        return self


class LootTableProvider(DataPackProvider):
    def get_location(self):
        return f"LootTableProvider {self.mod_id}"

    def get_loot_table_path(self, table_id):
        return self.get_data_path(join("loot_tables", f"{table_id}.json"))

    def get_loot_table_res(self, table_id):
        return f"oneblock-extra-{self.mod_id}:{table_id}"

    def add_loot(self, table_id:str, table: dict):
        self.add(self.get_loot_table_path(table_id), table)


class ModifiedLootTableProvider(LootTableProvider):

    def __init__(self, mod_id):
        super().__init__(mod_id)
        self.glm_entries = []

    def get_location(self):
        return f"ModifiedLootTableProvider {self.mod_id}"

    def get_glm_path(self):
        return self.get_data_base_path(join("forge", "loot_modifiers", "global_loot_modifiers.json"))

    def get_loot_modifiers_path(self, table_id:str):
        return self.get_data_path(join("loot_modifiers", f"add_loot_from_{table_id}.json"))

    def get_loot_modifiers_res(self, table_id:str):
        return f"oneblock-extra-{self.mod_id}:add_loot_from_{table_id}"

    def add_modified_loot(self, target: List[str], table_id: str, table: dict):
        self.add_loot(table_id, table)
        modified = {
            "type": "oneblock:add_loot_table",
            "conditions": [{"condition": "forge:loot_table_id", "loot_table_id": t} for t in target],
            "lootTable": self.get_loot_table_res(table_id)
        }
        self.add(self.get_loot_modifiers_path(table_id), modified)
        self.glm_entries.append(self.get_loot_modifiers_res(table_id))

    def run(self):
        self.add(self.get_glm_path(), {"entries": self.glm_entries, "replace": False})
        super().run()


class PhaseEntryBuilder(dict):
    def __init__(self, type_c: str, id_c: str, weight=0, count=0):
        super().__init__()
        self["type"] = type_c
        self["id"] = id_c
        if count > 0:
            self["count"] = count
        if weight > 0:
            self["weight"] = weight

    # preprocessing is self type
    def add_preprocessing(self, preprocessing):
        if self.get("preprocessing") is None:
            self["preprocessing"] = []
        self["preprocessing"].append(preprocessing)
        return self

    def set_offset(self, x=0, y=0, z=0):
        if x > 0:
            self["x"] = x
        if y > 0:
            self["y"] = y
        if z > 0:
            self["z"] = z
        return self

    def set_precedence(self, precedence_start=0, precedence_end=0):
        if not precedence_start == precedence_end:
            if precedence_start != 0:
                self["precedence_start"] = precedence_start
            if precedence_end != 0:
                self["precedence_end"] = precedence_end
        else:
            self["precedence"] = precedence_start
        return self

    def set_times(self, min_times=0, max_times=0):
        if not min_times == max_times:
            if min_times > max_times:
                raise ValueError(f"min_times {min_times} can't  bigger than max_times {max_times}")
            if min_times > 0:
                self["min_times"] = min_times
            if max_times > 0:
                self["max_times"] = max_times
        else:
            self["times"] = min_times
        return self

    def set_chance(self, chance=0.0):
        if 1 > chance > 0:
            self["chance"] = chance
        return self

    # for archaeology
    def set_loot_table(self, loot_table: str):
        self["loot_table"] = loot_table
        return self


class PhaseTableBuilder(dict):
    def __init__(self, count=0, end_gift=None, lict_v: List[PhaseEntryBuilder] = None):
        super().__init__()
        self["name"] = ""
        if count > 0:
            self["count"] = count
        if end_gift:
            self["end_gift"] = end_gift
        if lict_v:
            self["list"] = lict_v
        else:
            self["list"] = []

    def add_entry(self, pool: PhaseEntryBuilder):
        self["list"].append(pool)
        return self

    def add_block(self, block_id: str, weight: int):
        self.add_entry(PhaseEntryBuilder(type_c=constant.TYPE_BLOCK, id_c=block_id, weight=weight))
        return self

    def add_mob(self, mob_id: str, weight: int, count: int):
        self.add_entry(PhaseEntryBuilder(type_c=constant.TYPE_MOB, id_c=mob_id, weight=weight, count=count))
        return self


class SubPhaseTableBuilder(PhaseTableBuilder):
    def __init__(self, target: str, lict_v=None):
        super().__init__(lict_v=None)
        self["target"] = target
        del self["list"]
        if lict_v:
            self["list"] = lict_v
        else:
            self["list"] = []


class PhaseProvider(DataPackProvider):
    def get_location(self):
        return f"PhaseProvider {self.mod_id}"

    def get_phase_path(self, table_id):
        return self.get_data_path(join("oneblock", "phases", f"{table_id}.json"))

    def get_phase_res(self, table_id):
        return f"oneblock-extra-{self.mod_id}:phases/{table_id}"

    def add_phase(self, table_id, table: dict):
        self.add(self.get_phase_path(table_id), table)
