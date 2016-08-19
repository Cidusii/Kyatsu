"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
# from evennia import default_cmds

from evennia import default_cmds

class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_command(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_command(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

#------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
#------------------------------------------------------------

#from evennia.utils import utils
#class MuxCommand(Command):
#    """
#    This sets up the basis for a MUX command. The idea
#    is that most other Mux-related commands should just
#    inherit from this and don't have to implement much
#    parsing of their own unless they do something particularly
#    advanced.
#
#    Note that the class's __doc__ string (this text) is
#    used by Evennia to create the automatic help entry for
#    the command, so make sure to document consistently here.
#    """
#    def has_perm(self, srcobj):
#        """
#        This is called by the cmdhandler to determine
#        if srcobj is allowed to execute this command.
#        We just show it here for completeness - we
#        are satisfied using the default check in Command.
#        """
#        return super(MuxCommand, self).has_perm(srcobj)
#
#    def at_pre_cmd(self):
#        """
#        This hook is called before self.parse() on all commands
#        """
#        pass
#
#    def at_post_cmd(self):
#        """
#        This hook is called after the command has finished executing
#        (after self.func()).
#        """
#        pass
#
#    def parse(self):
#        """
#        This method is called by the cmdhandler once the command name
#        has been identified. It creates a new set of member variables
#        that can be later accessed from self.func() (see below)
#
#        The following variables are available for our use when entering this
#        method (from the command definition, and assigned on the fly by the
#        cmdhandler):
#           self.key - the name of this command ('look')
#           self.aliases - the aliases of this cmd ('l')
#           self.permissions - permission string for this command
#           self.help_category - overall category of command
#
#           self.caller - the object calling this command
#           self.cmdstring - the actual command name used to call this
#                            (this allows you to know which alias was used,
#                             for example)
#           self.args - the raw input; everything following self.cmdstring.
#           self.cmdset - the cmdset from which this command was picked. Not
#                         often used (useful for commands like 'help' or to
#                         list all available commands etc)
#           self.obj - the object on which this command was defined. It is often
#                         the same as self.caller.
#
#        A MUX command has the following possible syntax:
#
#          name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#        The 'name[ with several words]' part is already dealt with by the
#        cmdhandler at this point, and stored in self.cmdname (we don't use
#        it here). The rest of the command is stored in self.args, which can
#        start with the switch indicator /.
#
#        This parser breaks self.args into its constituents and stores them in the
#        following variables:
#          self.switches = [list of /switches (without the /)]
#          self.raw = This is the raw argument input, including switches
#          self.args = This is re-defined to be everything *except* the switches
#          self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                     no = is found, this is identical to self.args.
#          self.rhs: Everything to the right of = (rhs:'right-hand side').
#                    If no '=' is found, this is None.
#          self.lhslist - [self.lhs split into a list by comma]
#          self.rhslist - [list of self.rhs split into a list by comma]
#          self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#          All args and list members are stripped of excess whitespace around the
#          strings, but case is preserved.
#        """
#        raw = self.args
#        args = raw.strip()
#
#        # split out switches
#        switches = []
#        if args and len(args) > 1 and args[0] == "/":
#            # we have a switch, or a set of switches. These end with a space.
#            switches = args[1:].split(None, 1)
#            if len(switches) > 1:
#                switches, args = switches
#                switches = switches.split('/')
#            else:
#                args = ""
#                switches = switches[0].split('/')
#        arglist = [arg.strip() for arg in args.split()]
#
#        # check for arg1, arg2, ... = argA, argB, ... constructs
#        lhs, rhs = args, None
#        lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#        if args and '=' in args:
#            lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#            lhslist = [arg.strip() for arg in lhs.split(',')]
#            rhslist = [arg.strip() for arg in rhs.split(',')]
#
#        # save to object properties:
#        self.raw = raw
#        self.switches = switches
#        self.args = args.strip()
#        self.arglist = arglist
#        self.lhs = lhs
#        self.lhslist = lhslist
#        self.rhs = rhs
#        self.rhslist = rhslist
#
#        # if the class has the player_caller property set on itself, we make
#        # sure that self.caller is always the player if possible. We also create
#        # a special property "character" for the puppeted object, if any. This
#        # is convenient for commands defined on the Player only.
#        if hasattr(self, "player_caller") and self.player_caller:
#            if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                # caller is an Object/Character
#                self.character = self.caller
#                self.caller = self.caller.player
#            elif utils.inherits_from(self.caller, "evennia.players.players.DefaultPlayer"):
#                # caller was already a Player
#                self.character = self.caller.get_puppet(self.session)
#            else:
#                self.character = None
#

class CmdSetStat(Command):
    """
    set a stat of a character

    Usage:
     +setstat (stat) (1-200)

    This sets the power of the current character. This can only be
    used during character generation.
    """

    key = "+setstat"
    help_category = "mush"

    def parse(self):
        "This parses the arguments"
        args = self.args

        if len(args.rsplit()) != 2:
            self.statname = None
            self.statvalue = None
            return

        statname = args.rsplit()[0]
        statvalue = args.rsplit()[1]
        self.statname = statname
        self.statvalue = statvalue

    def func(self):
        "This performs the actual command"

        allowed_statnames = self.caller.db.stats.keys()

        errmsg1 = "You must supply a stat ( %s ). Syntax: +setstat (stat) (1-200)" % self.caller.db.stats.keys()
        errmsg2 = "You must supply an integer between 1 and 200. Syntax: +setstat (stat) (1-200)"

        if not self.args or not self.statname:
            self.caller.msg(errmsg1)
            return
        if self.statname not in allowed_statnames:
            self.caller.msg(errmsg1)
            return
        try:
            statvalue = int(self.statvalue)
        except ValueError:
            self.caller.msg(errmsg2)
            return
        if not (1 <= statvalue <= 200):
            self.caller.msg(errmsg2)
            return
        else:
            self.caller.db.stats[self.statname] = statvalue
            self.caller.msg("Your %s was set to %i" % (self.statname,statvalue))
            if self.statname == 'edr':
                self.caller.db.vitals['max_edr'] = statvalue
            if self.statname == 'will':
                self.caller.db.vitals['max_hp'] = statvalue

class CmdSetSkill(Command):
    """
    set a stat of a character

    Usage:
     +setskill (skillset) (skillname) (skillvalue)

    This sets the power of the current character. This can only be
    used during character generation.
    """

    key = "+setskill"
    help_category = "mush"

    def parse(self):
        "This parses the arguments"
        args = self.args

        #Check if right number of arguments are present.
        if len(args.rsplit()) != 3:
            self.skillset = None
            self.skillname = None
            self.skillvalue = None
            return

        #Split argument line into different components
        skillset = args.rsplit()[0]
        skillname = args.rsplit()[1]
        skillvalue = args.rsplit()[2]
        self.skillset = skillset
        self.skillname = skillname
        self.skillvalue = skillvalue

    def func(self):
        "This performs the actual command"

        #Define allowed skill sets and associated skill names
        allowed_skillsets = ['Katanas','Dodges']
        allowed_skillnames = {'Katanas': ['Basics','Chop','Jab','Upward','Downward'], 'Dodges': ['Basics','Jump','Sidestep','Duck']}

        errmsg = "Please use the correct syntax: +setskill (skillset) (skillvalue)"
        errmsg1 = "You must supply a skillset ( %s ). Syntax: +setskill (skillset) (skillvalue)" % allowed_skillsets

        if not self.args or not self.skillset:
            self.caller.msg(errmsg)
            return
        if self.skillset not in allowed_skillsets:
            self.caller.msg(errmsg1)
            return

        errmsg2 = "You must supply a skill name ( %s ). Syntax: +setskill (skillset) (skillvalue)" % allowed_skillnames[self.skillset]

        if not self.skillname:
            self.caller.msg(errmsg)
            return
        if self.skillname not in allowed_skillnames[self.skillset]:
            self.caller.msg(errmsg2)
            return

        errmsg3 = "You must supply a skill value. Syntax: +setskill (skillset) (skillvalue)"

        #Make sure skill value is a number, and set as an integer.
        try:
            skillvalue = int(self.skillvalue)
        except ValueError:
            self.caller.msg(errmsg3)
            return

        #Modify the skill. Not allowed to be better than the Basics skill level.
        else:
            if self.skillname != 'Basics' and skillvalue > self.caller.db.skills[self.skillset]['Basics']:
                self.caller.msg("You must supply a skill value no greater than your Basics level, (Current Basics: %s)" % self.caller.db.skills[self.skillset]['Basics'])
            else:
                self.caller.db.skills[self.skillset][self.skillname] = skillvalue
                self.caller.msg("Your move %s in the skill set %s was set to %i" % (self.skillset, self.skillname, skillvalue))

class CmdStats(Command):
    """
    List stats

    Usage:
        stats

    Displays a list of your current stats
    """

    key = "stats"
    aliases = ["ss","stat"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"

        stats, vitals = self.caller.get_stats()
        string = "STRENGTH: %s, AGILITY: %s, SPEED: %s, DEXTERITY: %s" % (stats['str'], stats['agi'], stats['spd'], stats['dex'])
        self.caller.msg(string)
        string = "HP: %s / %s, Endurance: %s %%" % (int(vitals['current_hp']),int(vitals['max_hp']), int(vitals['current_edr']/vitals['max_edr']*100))
        self.caller.msg(string)

class CmdSkills(Command):
    """
    List stats

    Usage:
        stats

    Displays a list of your current stats
    """

    key = "skills"
    aliases = ["sk","skill"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        "implements the actual functionality"

        skills = self.caller.get_skills()
        for x in range(len(skills)):
            string = "%s:" % skills.keys()[x-1]
            self.caller.msg(string)
            for y in range (len(skills[skills.keys()[x-1]])):
                string = "%s: %s" % (skills[skills.keys()[x-1]].keys()[y-1], skills[skills.keys()[x-1]][skills[skills.keys()[x-1]].keys()[y-1]])
                self.caller.msg(string)

            string = ""
            self.caller.msg(string)

class CmdWield(default_cmds.MuxCommand):
    #Command to wield an object.

    key = "wield"
    help_category = "General"

    def func(self):
        caller = self.caller
        args = self.args

        if not args:
            caller.msg("Wield what?")
            return

        obj = caller.search(args, location=caller, nofound_string="You are not carrying %s." % args)
        if not obj:
            return

        if not obj.db.wieldable:
            caller.msg("You cannot wield that you numpty!")
            return
        if obj.db.wieldable == "Two":
            if not caller.db.right_hand['Wielding'] and not caller.db.left_hand['Wielding']:
                caller.db.right_hand['Wielding'] = obj
                caller.db.left_hand['Wielding'] = obj
                caller.msg("You wield %s." % obj.name)
            else:
                caller.msg("You are already wielding something.")
        elif obj.db.wieldable == "One":
            if not caller.db.right_hand['Wielding']:
                caller.db.right_hand['Wielding'] = obj
                caller.msg("You wield %s." % obj.name)
            else:
                caller.msg("You are already wielding %s in your right hand." % caller.db.right_hand['Wielding'])


class CmdUnWield(default_cmds.MuxCommand):

    key = "unwield"
    aliases = "unw"
    help_category = "General"

    def func(self):
        caller = self.caller
        args = self.args

        if not args:
            caller.msg("Unwield what?")
            return

        obj = caller.search(args, location=caller, nofound_string="You are not carrying %s." % args)
        if not obj:
            return

        if caller.db.right_hand['Wielding'] != obj and caller.db.left_hand['Wielding'] != obj:
            self.caller.msg("You aren't wielding anything.")
        else:
            if self.caller.db.right_hand['Wielding'] == obj:
                self.caller.db.right_hand['Wielding'] = None
            if self.caller.db.left_hand['Wielding'] == obj:
                self.caller.db.left_hand['Wielding'] = None
            self.caller.msg("You unwield %s." % obj.name)


class CmdSmile(Command):
    """
    A smile command

    Usage:
      smile [at] [<someone>]
      grin [at] [<someone>]

    Smiles to someone in your vicinity or to the room
    in general.

    (This initial string (the __doc__ string)
    is also used to auto-generate the help
    for this command)
    """

    key = "smile"
    aliases = ["smile at"]
    locks = "cmd:all()"
    help_category = "Emoting"

    def parse(self):
        "Very trivial parser"
        self.target = self.args.strip()

    def func(self):
        "This actually does things"
        caller = self.caller
        if not self.target or self.target == "here":
            string = "%s smiles." % caller.name
            caller.location.msg_contents(string, exclude=caller)
            caller.msg("You smile.")
        else:
            target = caller.search(self.target)
            if not target:
                # caller.search handles error messages
                return
            string = "%s smiles to you." % caller.name
            target.msg(string)
            string = "You smile to %s." % target.name
            caller.msg(string)
            string = "%s smiles to %s." % (caller.name, target.name)
            caller.location.msg_contents(string, exclude=[caller, target])

class WeaponAttacks(Command):

    def parse(self):

        args = self.args

        if len(args.rsplit()) == 1:
            target = args
            hitbox = "Normal"
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

    def noLongerBusy(self):
        "This will remove busy status."
        del self.caller.ndb.is_busy
        self.caller.msg("You are no longer busy.")


class CmdDrop(default_cmds.MuxCommand):
    """
    drop something

    Usage:
      drop <obj>

    Lets you drop an object from your inventory into the
    location you are currently in.
    """

    key = "drop"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        "Implement command"

        caller = self.caller
        if not self.args:
            caller.msg("Drop what?")
            return

        # Because the DROP command by definition looks for items
        # in inventory, call the search function using location = caller
        obj = caller.search(self.args, location=caller,
                            nofound_string="You aren't carrying %s." % self.args,
                            multimatch_string="You carry more than one %s:" % self.args)
        if not obj:
            return

        if caller.db.left_hand['Wielding'] == obj or caller.db.right_hand['Wielding'] == obj:
            caller.execute_cmd("unwield " + obj.name)

        obj.move_to(caller.location, quiet=True)
        caller.msg("You drop %s." % (obj.name,))
        caller.location.msg_contents("%s drops %s." %
                                         (caller.name, obj.name),
                                     exclude=caller)
        # Call the object script's at_drop() method.
        obj.at_drop(caller)