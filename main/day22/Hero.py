from dataclasses import dataclass


@dataclass
class Hero:
    hp: int
    mana: int
    armor: int
    _total_mana_spent: int = 0

    def get_mana_spent(self) -> int:
        return self._total_mana_spent

    def spend_mana(self, mana_spent):
        self.mana -= mana_spent
        self._total_mana_spent += mana_spent
