"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move - Launches the "look" command after every move.
    at_post_unpuppet(player) -  when Player disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Player has disconnected" 
                    to the room.
    at_pre_puppet - Just before Player re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "PlayerName has entered the game" to the room.

    """

    def at_object_creation(self):
        """
                Called only at initial creation. This is a rather silly
                example since ability scores should vary from Character to
                Character and is usually set during some character
                generation step instead.
                """
        # set persistent stats and skills
        self.db.stats = {'str':100, 'agi':100, 'spd':100, 'dex':100, 'will':100, 'edr':100}

        self.db.vitals = {'current_hp':self.db.stats['will'],'max_hp':self.db.stats['will'],
                          'current_edr':self.db.stats['edr'],'max_edr':self.db.stats['edr']}

        self.db.skills = {'Katanas': {'Basics':50,'Jab':10,'Chop':10},'Dodges': {'Basics':50,'Duck':10,'Jump':10,'Sidestep':10}}

    def get_stats(self):
        """
        Simple access method to return stats
        """
        return self.db.stats, self.db.vitals

    def get_skills(self):
        """
        Simple access method to return skill scores
        """

        return self.db.skills



    pass
