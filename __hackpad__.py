class _ICharacterDataDestructurer:

    @staticmethod
    def get_assignable_fields(character_data: _CharacterData) -> tuple:
        raise NotImplementedError

    @staticmethod
    def calc_fields(character_data: _CharacterData) -> tuple:
        raise NotImplementedError

    @staticmethod
    def del_data(character_data: _CharacterData) -> _CharacterData:
        raise NotImplementedError


class _IBlock:
    pass


class _StatBlock(_IBlock):

    @staticmethod
    def calc_modifier(stat_value: int) -> int:
        return floor((stat_value - 10) / 2)

    def __init__(self, character_data: _CharacterData):
        self._str = character_data.str
        self.str_mod = self.calc_modifier(self._str)

        self.dex = character_data.dex
        self.dex_mod = self.calc_modifier(self.dex)

        self.con = character_data.con
        self.con_mod = self.calc_modifier(self.con)

        self._int = character_data.int
        self.int_mod = self.calc_modifier(self._int)

        self.wis = character_data.wis
        self.int_mod = self.calc_modifier(self.wis)

        self.cha = character_data.cha
        self.int_mod = self.calc_modifier(self.cha)


class _BasicInfo(_ICharacterDataDestructurer, _StatBlock):
    @staticmethod
    def del_data(character_data: _CharacterData) -> _CharacterData:
        del character_data.name
        del character_data.character_class
        del character_data.experience_points
        return character_data

    @staticmethod
    def calc_level(experience_points: int) -> int:
        # TODO
        return 1

    @staticmethod
    def get_assignable_fields(character_data: _CharacterData) -> tuple:
        return character_data.name, \
            character_data.character_class, \
            character_data.experience_points

    @staticmethod
    def calc_fields(character_data: _CharacterData) -> tuple:
        level = _BasicInfo.calc_level(
            character_data.experience_points
        )

        hitpoints = _CharacterData.character_class.hp_per_level * level

        return level, hitpoints

    def __init__(self, character_data: _CharacterData):
        self.name, self.character_class, self.experience_points = \
            self.get_assignable_fields(character_data)

        self.level, self.hitpoints = self.calc_fields(character_data)
        new_character_data = self.del_data(character_data)

        super().__init__(new_character_data)