import sys


class StageInfo:

    def __init__(self, ids, name="", end_gift=None, stage_gift=None, variety_gift=None):
        self.id = ids
        self.name = name
        self.end_gift = end_gift
        self.stage_gift = stage_gift
        self.variety_gift = variety_gift

    def get_phase_id(self):
        return f"oneblock:phases/{self.id}"


STAGE_00 = StageInfo('00', "start", 'ija-one-block:00-gift', 'ija-one-block:00')
STAGE_PLAIN = StageInfo('01', "plain", 'ija-one-block:01-gift', 'ija-one-block:01', 'ija-one-block:01-variety')
STAGE_UNDERGROUND = StageInfo('02', "under", 'ija-one-block:02-gift', 'ija-one-block:02', 'ija-one-block:02-variety')
STAGE_COLD = StageInfo('03', "cold", 'ija-one-block:03-gift', 'ija-one-block:03', 'ija-one-block:03-variety')
STAGE_SWAMP = StageInfo('04', "swamp", 'oneblock:04-gift', 'oneblock:04')
STAGE_OCEAN = StageInfo('05', "ocean", 'ija-one-block:04-gift', 'ija-one-block:04', 'ija-one-block:04-variety')
STAGE_FOREST = StageInfo('06', "forest", 'ija-one-block:05-gift', 'ija-one-block:05', 'ija-one-block:05-variety')
STAGE_HOT = StageInfo('07', "red desert", 'ija-one-block:06-gift', 'ija-one-block:06', 'ija-one-block:06-variety')
STAGE_NETHER = StageInfo('08', "nether", 'ija-one-block:07-gift', 'ija-one-block:07', 'ija-one-block:07-variety')
STAGE_VILLAGE = StageInfo('09', "village", 'ija-one-block:08-gift', 'ija-one-block:08', 'ija-one-block:08-variety')
STAGE_TRAVEL = StageInfo('10', "over hills", 'oneblock:10-gift', 'oneblock:10')
STAGE_ISOLATED = StageInfo('11', "isolated land", 'ija-one-block:09-gift', 'ija-one-block:09',
                           'ija-one-block:09-variety')
STAGE_DEPTH = StageInfo('12', "under depth", 'oneblock:12-gift', 'oneblock:12')
STAGE_END = StageInfo('13', "the end", 'ija-one-block:10-gift', 'ija-one-block:10', 'ija-one-block:10-variety')
STAGE_ALL = StageInfo('all', "after phases")

TYPE_BLOCK = "block"
TYPE_GIFT = "gift"
TYPE_MOB = "mob"
TYPE_ARCHAEOLOGY = "archaeology"
TYPE_STRUCTURE = "structure"
TYPE_TEMPLATE = "template"
TYPE_CONFIGURED_FEATURE = "configured_feature"
TYPE_COMMAND = "command"
TYPE_SOUND = "sound"


def get_stage(res):
    mod = sys.modules[__name__]
    local_cache = dir(mod)
    for v in local_cache:
        if v.startswith("STAGE_"):
            old_v = getattr(mod, v)
            if old_v.get_phase_id() == res:
                return v
    print(f"error get {res}")
