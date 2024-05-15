import json
from typing import List


class RegisterEntry(str):
    def __init__(self, id: str, tags: List[str] = None, nbt: dict = None):
        self.id = id
        self.tags = tags
        self.nbt = nbt

    def __str__(self):
        return f"{self.id}"

    def __repr__(self):
        return f"'{self.id}'"


class Collections:
    def dir(self):
        return [i for i in dir(self) if not i.startswith("__")]

    def list(self) -> List[str]:
        return [RegisterEntry(getattr(self, i)) for i in self.dir()]

    def get_key_by_value(self, value):
        for i in self.dir():
            v = getattr(self, i)
            if str(v) == value:
                return i
        return None
