from command import Command, WeaponAttacks
from time import time
import math
from evennia import utils

from typeclasses.characters import Character

from world import rules
from random import choice

class CmdChop(WeaponAttacks):
    """
    Chop attack with Katana

    Usage: chop (target) (body part)


    """

    key = "Chop"
    help_category = "Katanas"
    locks = "call:holds();cmd:cmdis_twowielding()"

    # def parse(self):
    #
    #     args = self.args
    #
    #     if len(args.rsplit()) == 1:
    #         target = args
    #         hitbox = None
    #     elif len(args.rsplit()) == 2:
    #         target = args.rsplit()[0]
    #         hitbox = args.rsplit()[1]
    #     else:
    #         target = None
    #         hitbox = None
    #
    #     if not target:
    #         self.target = target
    #     else:
    #         self.target = target.strip()
    #
    #     self.hitbox = hitbox

    def func(self):

        caller = self.caller
        self.difficulty = "Easy"

        if not self.target:
            caller.msg("No target specified. (Usage: chop <target> <location>).")
            return

        target = caller.search(self.target, location=caller.location, nofound_string="Your intended target, %s, cannot be found here." % self.target)
        hitbox = self.hitbox

        if not target:
            return

        if not utils.inherits_from(target, Character):
            caller.msg("You cannot attack that!")
            return

        if caller.ndb.is_busy:
            # You are still busy.
            timeleft = self.caller.ndb.busy_timer.getTime() - time()
            caller.msg("You are still busy for " + str(int(math.ceil(timeleft))) + " seconds.")
            return

        self.target = target

        defender_weapon = self.target.db.right_hand['Wielding']

        caller_attempt_string = "You chop down with %s viciously, striking at %s." % (self.obj, target)
        target_attempt_string = "%s chops down with %s viciously, striking at you." % (caller, self.obj)
        room_attempt_string = "%s chops down with %s viciously, striking at %s." % (caller, self.obj, target)

        raw_success, refined_success, thresholds = rules.getCombatSuccess(self)
        hit = rules.getHit()

        roll_string = "[Success: %s, Roll: %s] \n" % (refined_success, hit)

        if hit > refined_success:
            damage = rules.getDamage(self,raw_success,hit)
            rules.inflictDamage(self, damage)

            if hitbox == "Normal" or hitbox == "High":
                hit_locations = ["Face", "Head", "Neck", "Left shoulder", "Right shoulder"]
                hitlocation = choice(hit_locations)
            elif hitbox == "Mid":
                hit_locations = ["Chest", "Waist", "Left arm", "Right arm", "Left hand", "Right hand"]
                hitlocation = choice(hit_locations)
            else:
                hit_locations = ["Left thigh", "Right thigh", "Left calf", "Right calf", "Left foot", "Right foot"]
                hitlocation = choice(hit_locations)

            if damage < 5:
                injury = "Shallow cut"
            elif damage < 10:
                injury = "Cut"
            elif damage < 15:
                injury = "Deep cut"
            elif damage < 20:
                injury = "Severe cut"
            else:
                injury = "Devastating cut"

            caller_damage_string = " Hit! %s suffers a %s to their %s." % (target, injury.lower(), hitlocation.lower())
            target_damage_string = " Hit! You suffer a %s to your %s." % (injury.lower(), hitlocation.lower())

            caller.msg(roll_string + caller_attempt_string + caller_damage_string)
            target.msg(roll_string + target_attempt_string + target_damage_string)
            caller.location.msg_contents(room_attempt_string + caller_damage_string, exclude=(caller, target))
        else:
            for defence in thresholds:
                if hit <= thresholds[defence]:

                    #Call relevant message strings and their formats to fill %s.
                    caller_block_string = rules.WEAPONBLOCKS[defence.rsplit()[0]][defence.rsplit()[1]]["CallerString"]
                    target_block_string = rules.WEAPONBLOCKS[defence.rsplit()[0]][defence.rsplit()[1]]["TargetString"]
                    room_block_string = rules.WEAPONBLOCKS[defence.rsplit()[0]][defence.rsplit()[1]]["RoomString"]
                    caller_format = rules.WEAPONBLOCKS[defence.rsplit()[0]][defence.rsplit()[1]]["CallerFormat"]
                    target_format = rules.WEAPONBLOCKS[defence.rsplit()[0]][defence.rsplit()[1]]["TargetFormat"]
                    room_format = rules.WEAPONBLOCKS[defence.rsplit()[0]][defence.rsplit()[1]]["RoomFormat"]

                    #initialise lists for formats
                    caller_format_list = []
                    target_format_list = []
                    room_format_list = []

                    #Call what the format strings represent and append the resulting variables to the lists.
                    for formats in caller_format:
                        caller_format_list.append(eval(formats))
                    for formats in target_format:
                        target_format_list.append(eval(formats))
                    for formats in room_format:
                        room_format_list.append(eval(formats))

                    caller_string = (caller_block_string % tuple(caller_format_list))
                    target_string = (target_block_string % tuple(target_format_list))
                    room_string = (room_block_string % tuple(room_format_list))

                    caller.msg(roll_string + caller_attempt_string + " " + caller_string)
                    target.msg(roll_string + target_attempt_string + " " + target_string)
                    caller.location.msg_contents(room_attempt_string + " " + room_string, exclude=(caller, target))
                    break
                else:
                    pass

        caller.ndb.is_busy = True

        self.caller.ndb.busy_timer = utils.delay(1 / self.obj.db.attack_speed_mod, callback=self.noLongerBusy)

    # def noLongerBusy(self):
    #     "This will remove busy status."
    #     del self.caller.ndb.is_busy
    #     self.caller.msg("You are no longer busy.")


class CmdJab(WeaponAttacks):
    """
    Jab attack with Katana

    Usage: jab (target) (body part)


    """

    key = "jab"
    help_category = "Katanas"
    locks = "call:holds();cmd:cmdis_twowielding()"


    # def parse(self):
    #
    #     args = self.args
    #
    #     if len(args.rsplit()) == 1:
    #         target = args
    #         hitbox = None
    #     elif len(args.rsplit()) == 2:
    #         target = args.rsplit()[0]
    #         hitbox = args.rsplit()[1]
    #     else:
    #         target = None
    #         hitbox = None
    #
    #     if not target:
    #         self.target = target
    #     else:
    #         self.target = target.strip()
    #
    #     self.hitbox = hitbox

    def func(self):

        caller = self.caller
        self.difficulty = "Easy"

        if not self.target:
            caller.msg("No target specified. (Usage: jab <target> <location>).")
            return

        target = caller.search(self.target,location=caller.location, nofound_string="Your intended target, %s, cannot be found here." % self.target)
        hitbox = self.hitbox

        if not target:
            #caller.msg("Your target is not here.")
            return

        if caller.ndb.is_busy:
            #You are still busy.
            timeleft = self.caller.ndb.busy_timer.getTime() - time()
            caller.msg("You are still busy for " + str(int(math.ceil(timeleft))) + " seconds.")
            return

        caller.ndb.is_busy = True
        caller.msg("You jab %s forward at %s." % (self.obj, target.name))

        self.caller.ndb.busy_timer = utils.delay(4/self.obj.db.attack_speed_mod, callback = self.noLongerBusy)

    # def noLongerBusy(self):
    #     "This will remove busy status."
    #     del self.caller.ndb.is_busy
    #     self.caller.msg("You are no longer busy.")
