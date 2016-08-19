#from objects import Object

from evennia import DefaultObject as Object
from commands import default_cmdsets

class Weapon(Object):
    """
    Defines generic methods and attributes for all weapon types/
    """

    def get_damage_mod(self):

        #Define the effect of material and quality of the weapon
        material_damage_mods = {"Wood": 0.5, "Iron": 0.75, "Steel": 1, "SuperSteel": 1.1, "Oronum": 1.2}
        quality_damage_mods = {"Horrible": 0.8, "Below Average": 0.9, "Average": 1, "Above Average": 1.1, "Good": 1.2, "Excellent": 1.3, "Masterful": 1.4, "Legendary": 1.5}

        attack_damage_mod = material_damage_mods[self.db.material] * quality_damage_mods[self.db.quality]

        return attack_damage_mod

    def get_success_mod(self):

        quality_success_mods = {"Horrible": 0.9, "Below Average": 0.95, "Average": 1, "Above Average": 1.05, "Good": 1.1, "Excellent": 1.15, "Masterful": 1.2, "Legendary": 1.25}

        return quality_success_mods[self.db.quality]



class Katana(Weapon):
    """
    Defines the typical Katana weapon.
    """

    def at_object_creation(self):

        #Weapon properties.
        self.db.weapon_type = "Katanas"
        self.db.material = "Steel"
        self.db.quality = "Average"

        if __name__ == '__main__':
            self.db.weight = 1.2 #in kg. We use metric yo

        self.db.wieldable = "Two"
        self.db.attack_speed_mod = 1

        #Builder-customisable bonuses/mods for custom weapons.
        #Bonus for additional damage, mod for multiplier to damage.
        self.db.builder_damage_bonus = None
        self.db.builder_damage_mod = None


        #Base weapon description
        self.db.desc = "You see a typical steel katana."

        #Define commands available for this weapon type.
        self.cmdset.add(default_cmdsets.KatanaCmdSet)

class Bo(Weapon):
    """
    Defines the typical Bo weapon.
    """

    def at_object_creation(self):

        #Weapon properties.
        self.db.weapon_type = "Bo staves"
        self.db.material = "Oak"
        self.db.quality = "Average"

        if __name__ == '__main__':
            self.db.weight = 1 #in kg. We use metric yo

        self.db.wieldable = "Two"
        self.db.attack_speed_mod = 1

        #Builder-customisable bonuses/mods for custom weapons.
        #Bonus for additional damage, mod for multiplier to damage.
        self.db.builder_damage_bonus = None
        self.db.builder_damage_mod = None


        #Base weapon description
        self.db.desc = "You see a typical Oak Bo Staff."

        #Define attacks available for weapon type

    def get_damage_mod(self):

        #Define the effect of material and quality of the weapon
        material_damage_mods = {"Rattan": 0.5, "Bamboo": 0.75, "Oak": 1, "Iron-banded Oak": 1.1, "Steel-banded Oak": 1.2}
        quality_damage_mods = {"Horrible": 0.8, "Below Average": 0.9, "Average": 1, "Above Average": 1.1, "Good": 1.2, "Excellent": 1.3, "Masterful": 1.4, "Legendary": 1.5}

        attack_damage_mod = material_damage_mods[self.db.material] * quality_damage_mods[self.db.quality]

        return attack_damage_mod

class Rogatina(Weapon):
    """
    Defines the typical Two-Handed Boar Spear (Rogatina) weapon.
    """

    def at_object_creation(self):

        #Weapon properties.
        self.db.weapon_type = "Rogatina"
        self.db.material = "Steel"
        self.db.quality = "Average"

        if __name__ == '__main__':
            self.db.weight = 2 #in kg. We use metric yo

        self.db.wieldable = "Two"
        self.db.attack_speed_mod = 1

        #Builder-customisable bonuses/mods for custom weapons.
        #Bonus for additional damage, mod for multiplier to damage.
        self.db.builder_damage_bonus = None
        self.db.builder_damage_mod = None


        #Base weapon description
        self.db.desc = "You see a typical steel Rogatina."