from command import Command
from time import time
import math
from evennia import utils

class CmdChop(Command):
    """
    Chop attack with Katana

    Usage: chop (target) (body part)


    """

    key = "chop"
    help_category = "mush"
    locks = "call:holds();cmd:cmdis_twowielding()"
    arg_regex = r"\s|$"


    def parse(self):

        args = self.args

        if len(args.rsplit()) == 1:
            target = args
            hitbox = None
        elif len(args.rsplit()) == 2:
            target = args.rsplit()[0]
            hitbox = args.rsplit()[1]
        else:
            target = None
            hitbox = None

        if not target:
            self.target = target
        else:
            self.target = target.strip()

        self.hitbox = hitbox

    def func(self):

        caller = self.caller

        if not self.target:
            caller.msg("No target specified. (Usage: chop <target> <location>).")
            return

        target = caller.search(self.target, location=caller.location)
        hitbox = self.hitbox

        if not target:
            # caller.msg("Your target is not here.")
            return

        if caller.ndb.is_busy:
            # You are still busy.
            timeleft = self.caller.ndb.busy_timer.getTime() - time()
            caller.msg("You are still busy for " + str(int(math.ceil(timeleft))) + " seconds.")
            return

        caller.ndb.is_busy = True
        caller.msg("You chop down with %s viciously, striking at %s." % (self.obj, target.name))

        self.caller.ndb.busy_timer = utils.delay(5 / self.obj.db.attack_speed_mod, callback=self.noLongerBusy)

    def noLongerBusy(self):
        "This will remove busy status."
        del self.caller.ndb.is_busy
        self.caller.msg("You are no longer busy.")


class CmdJab(Command):
    """
    Jab attack with Katana

    Usage: jab (target) (body part)


    """

    key = "jab"
    help_category = "mush"
    locks = "call:holds();cmd:cmdis_twowielding()"


    def parse(self):

        args = self.args

        if len(args.rsplit()) == 1:
            target = args
            hitbox = None
        elif len(args.rsplit()) == 2:
            target = args.rsplit()[0]
            hitbox = args.rsplit()[1]
        else:
            target = None
            hitbox = None

        if not target:
            self.target = target
        else:
            self.target = target.strip()

        self.hitbox = hitbox

    def func(self):

        caller = self.caller

        if not self.target:
            caller.msg("No target specified. (Usage: jab <target> <location>).")
            return

        target = caller.search(self.target,location=caller.location)
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

    def noLongerBusy(self):
        "This will remove busy status."
        del self.caller.ndb.is_busy
        self.caller.msg("You are no longer busy.")
