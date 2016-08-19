# from evennia.myapp import WeaponMatchups
# import csv

#Rules and general info gathering functions.

from collections import OrderedDict
from random import randint

# Define countering blocks to Katana attacks.
KATANACOUNTERS = {"Jab":
                      {"Hitbox":
                          {"Normal":
                               {"Dodges": ["Sidestep"], "Shields": ["Simple"], "Katanas": ["Downward"], "Bo staves": ["Cross"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           "Low":
                               {"Dodges": ["Leg dodge"], "Shields": ["Low"], "Katanas": ["Low"], "Bo staves": ["Turning"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           "Mid":
                               {"Dodges": [""], "Shields": [""], "Katanas": ["Downward"], "Bo staves": ["Cross"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           "High":
                               {"Dodges": [""], "Shields": [""], "Katanas": ["Upward"], "Bo staves": ["Turning"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           }
                       },
                  "Chop":
                      {"Hitbox":
                          {"Normal":
                               {"Dodges": ["Sidestep"], "Shields": ["Simple"], "Katanas": ["Upward"], "Bo staves": ["Upward"],
                                "Rogatina": "", "Sai": "", "Spear": ""},
                           "Low":
                               {"Dodges": ["Leg dodge"], "Shields": ["Low"], "Katanas": ["Low"], "Bo staves": ["Twisting"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           "Mid":
                               {"Dodges": [""], "Shields": [""], "Katanas": ["Upward"], "Bo staves": ["Upward"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           "High":
                               {"Dodges": [""], "Shields": [""], "Katanas": ["Upward"], "Bo staves": ["Upward"],
                                "Rogatina": [""], "Sai": [""], "Spear": [""]},
                           }
                       }

                }

# Define countering blocks to Bo attacks.
BOCOUNTERS = {"Jab":
                 {"Hitbox":
                      {"Normal":
                           {"Dodges": ["Sidestep"], "Shields": ["Simple"], "Katanas": ["Downward"], "Bo staves": ["Cross"],
                            "Rogatina": [""], "Sai": [""], "Spear": [""]},
                       "Low":
                           {"Dodges": ["Leg dodge"], "Shields": ["Low"], "Katanas": ["Low"], "Bo staves": ["Turning"],
                            "Rogatina": [""], "Sai": [""], "Spear": [""]},
                       "Mid":
                           {"Dodges": [""], "Shields": [""], "Katanas": ["Downward"], "Bo staves": ["Cross"],
                            "Rogatina": [""], "Sai": [""], "Spear": [""]},
                       "High":
                           {"Dodges": [""], "Shields": [""], "Katanas": ["Upward"], "Bo staves": ["Turning"],
                            "Rogatina": [""], "Sai": [""], "Spear": [""]},
                       }
                  }
            }

# Create weapon matchup dictionary.
WEAPONMATCHUPS = {"Katanas": KATANACOUNTERS, "Bo staves": BOCOUNTERS}

#Define attacks and their difficulty

#Define blocks and their difficulty/flavour

NOBLOCK = {"Noblock":
               {"CallerString": "You miss %s.", "CallerFormat": ["target"],
                "TargetString": "%s misses you.", "TargetFormat": ["caller"],
                "RoomString": "%s misses %s.", "RoomFormat": ["caller", "target"]}}

DODGES = {"Simple":
              {"Difficulty": "Easy",
               "CallerString": "%s dodges your attack.", "CallerFormat": ["target"],
               "TargetString": "You dodge %s's attack.", "TargetFormat": ["caller"],
               "RoomString": "%s dodges %s's attack.", "RoomFormat": ["target", "caller"]},
          "Sidestep":
              {"Difficulty": "Easy",
               "CallerString": "%s steps to one side, avoiding your attack.", "CallerFormat": ["target"],
               "TargetString": "You step to one side, avoiding %s's attack.", "TargetFormat": ["caller"],
               "RoomString": "%s steps to one side, avoiding %s's attack.", "RoomFormat": ["target", "caller"]},
          "Jump":
              {"Difficulty": "Easy",
               "CallerString": "%s jumps, drawing their knees up and allowing your attack to pass harmlessly underneath.", "CallerFormat": ["target"],
               "TargetString": "You jump, drawing your knees up and allowing %s's attack to pass harmlessly underneath.", "TargetFormat": ["caller"],
               "RoomString": "%s jumps, drawing their knees up and allowing %s's attack to pass harmlessly underneath.", "RoomFormat": ["target", "caller"]},
          "Leg dodge":
              {"Difficulty": "Average",
               "CallerString": "%s moves their leg out of the way of your attack.", "CallerFormat": ["target"],
               "TargetString": "You move your leg out of the way of %s's attack.", "TargetFormat": ["caller"],
               "RoomString": "%s moves their leg out of the way of %s's attack.", "RoomFormat": ["target", "caller"]},
          "Swaying":
              {"Difficulty": "Average",
               "String": "%s sways to one side, allowing your attack to pass by.", "CallerFormat": ["target"],
               "TargetString": "You sway to one side, allowing %s's attack to pass by.", "TargetFormat": ["caller"],
               "RoomString": "%s sways to one side, allowing %s's attack to pass by.", "RoomFormat": ["target", "caller"]},
          "Turning":
              {"Difficulty": "Average",
               "CallerString": "%s turns sideways, avoiding your attack.", "s1": ["target"],
               "TargetString": "You turn sideways, avoiding %s's attack.", "TargetFormat": ["caller"],
               "RoomString": "%s turns sideways, avoiding %s's attack.", "RoomFormat": ["target", "caller"]},
          "Rolling rise":
              {"Difficulty": "Hard",
               "CallerString": "%s uses their falling momentum to roll, rising back to their feet.", "CallerFormat": ["target"],
               "TargetString": "You use your falling momentum to roll, rising back to your feet.",
               "RoomString": "%s uses their falling momentum to roll, rising back to their feet.", "RoomFormat": ["target"]},
          "Rolling dodge":
              {"Difficulty": "Very hard",
               "CallerString": "%s rolls to the side on the ground, avoiding your attack.", "CallerFormat": ["target"],
               "TargetString": "You roll to the side on the ground, avoiding %s's attack.", "TargetFormat": ["caller"],
               "RoomString": "%s rolls to the side on the ground, avoiding %s's attack.", "RoomFormat": ["target", "caller"]},
          "Back leap":
              {"Difficulty": "Hard",
               "String": "%s leaps back, avoiding your attack.", "CallerFormat": ["target"],
               "TargetString": "You leap back, avoiding %s's attack.", "TargetFormat": ["caller"],
               "RoomString": "%s leaps back, avoiding %s's attack.", "RoomFormat": ["target", "caller"]},
          }

KATANABLOCKS = {"Upward":
                    {"Difficulty": "Average",
                     "CallerString": "%s brings %s up, using the flat of the blade to parry your attack.", "CallerFormat": ["target", "defender_weapon.name"],
                     "TargetString": "You bring %s up, using the flat of the blade to parry %s's attack.", "TargetFormat": ["defender_weapon.name", "caller"],
                     "RoomString": "%s brings %s up, using the flat of the blade to parry %s's attack.", "RoomFormat": ["target", "defender_weapon.name", "caller"]},
                "Downward":
                    {"Difficulty": "Average",
                     "CallerString": "%s brings %s down, chopping your attack out of harm's way.", "CallerFormat": ["target", "defender_weapon.name"],
                     "TargetString": "You bring %s down, chopping %s's attack out of harm's way.", "TargetFormat": ["defender_weapon.name", "caller"],
                     "RoomString": "%s brings %s down, using chopping %s's attack out of harm's way.", "RoomFormat": ["target", "defender_weapon.name", "caller"]
                     },
                "Side":
                    {"Difficulty": "Hard",
                     "CallerString": "%s brings %s to the side, parrying your attack away from their body.",
                     "CallerFormat": ["target", "defender_weapon.name"],
                     "TargetString": "You bring %s to the side, parrying %s's attack away from your body.",
                     "TargetFormat": ["defender_weapon.name", "caller"],
                     "RoomString": "%s brings %s to the side, parrying %s's attack away from their body.",
                     "RoomFormat": ["target", "defender_weapon.name", "caller"]
                     },
                "Low":
                    {"Difficulty": "Hard",
                     "CallerString": "%s swings %s low, using the flat side of the blade to push your attack to the side.",
                     "CallerFormat": ["target", "defender_weapon.name"],
                     "TargetString": "You swing %s low, using the flat side of the blade to push %s's attack to the side.",
                     "TargetFormat": ["defender_weapon.name", "caller"],
                     "RoomString": "%s swings %s low, using the flat side of the blade to push %s's attack to the side.",
                     "RoomFormat": ["target", "defender_weapon.name", "caller"]
                     },
                "Tsuba":
                    {"Difficulty": "Very hard",
                     "String": "Holding %s firmly, %s catches your attack on the tsuba.",
                     "CallerFormat": ["defender_weapon.name", "target"],
                     "TargetString": "Holding %s firmly, you catch %s's attack on the tsuba.",
                     "TargetFormat": ["defender_weapon.name", "caller"],
                     "RoomString": "Holding %s firmly, %s catches %s's attack on the tsuba.",
                     "RoomFormat": ["defender_weapon.name", "target", "caller"]
                     },
                "Drawing":
                    {"Difficulty": "Very hard",
                     "String": "%s draws %s from their scabbard swiftly, catching your attack on the blade.",
                     "CallerFormat": ["target", "defender_weapon.name"],
                     "TargetString": "You draw %s from your scabbard swiftly, catching %s's attack on the blade.",
                     "TargetFormat": ["defender_weapon.name", "caller"],
                     "RoomString": "%s draws %s from their scabbard swiftly, catching %s's attack on the blade.",
                     "RoomFormat": ["target", "defender_weapon.name", "caller"]
                     },
                }

BOBLOCKS = {"Simple":
                {"Difficulty": "Easy",
                 "CallerString": "%s blocks your attack with %s.", "CallerFormat": ["target", "defender_weapon.name"],
                 "TargetString": "You block %s's attack with %s.", "TargetFormat": ["caller", "defender_weapon.name"],
                 "RoomString": "%s blocks %s's attack with %s.", "RoomFormat": ["target", "caller", "defender_weapon.name"]},
            "Cross":
                {"Difficulty": "Easy",
                 "CallerString": "With %s held vertically, %s diverts your attack away from the center of their body.",
                 "CallerFormat": ["defender_weapon.name", "target"],
                 "TargetString": "With %s held vertically, you divert %s's attack away from the center of your body.", "TargetFormat": ["defender_weapon.name", "caller"],
                 "RoomString": "With %s held vertically, %s diverts %s's attack away from the center of their body.", "RoomFormat": ["defender_weapon.name", "target", "caller"]},
            "Upward":
                {"Difficulty": "Average",
                 "CallerString": "%s swings %s upwards, catching your attack.",
                 "CallerFormat": ["target", "defender_weapon.name"],
                 "TargetString": "You swing %s upwards, catching %s's attack.", "TargetFormat": ["defender_weapon.name", "caller"],
                 "RoomString": "%s swings %s upwards, catching %s's attack.", "RoomFormat": ["target", "defender_weapon.name", "caller"]},
            "Overhead":
                {"Difficulty": "Easy",
                 "CallerString": "Bracing themselves, %s brings %s above their head, stopping your attack above their head.",
                 "CallerFormat": ["target", "defender_weapon.name"],
                 "TargetString": "Bracing yourself, you brings %s above your head, stopping %s's attack above your head.", "TargetFormat": ["defender_weapon.name", "caller"],
                 "RoomString": "Bracing themselves, %s brings %s above their head, stopping %s's attack above their head.", "RoomFormat": ["target", "defender_weapon.name", "caller"]},
            "Twisting":
                {"Difficulty": "Hard",
                 "CallerString": "%s uses the length of %s to subtly twist your attack away from their body.",
                 "CallerFormat": ["target", "defender_weapon.name"],
                 "TargetString": "You use the length of %s to subtly twist %s's attack away from your body.", "TargetFormat": ["caller", "defender_weapon.name"],
                 "RoomString": "%s uses the length of %s  to subtly twist %s's attack away from their body.", "RoomFormat": ["target", "defender_weapon.name", "caller"]},
            "Turning":
                {"Difficulty": "Average",
                 "CallerString": "%s turns %s swiftly, using one end to divert your attack away from their centre line.",
                 "CallerFormat": ["target", "defender_weapon.name"],
                 "TargetString": "You turn %s swiftly, using one end to divert %s's attack away from your centre line.", "TargetFormat": ["caller", "defender_weapon.name"],
                 "RoomString": "%s turns %s swiftly, using one end to divert %s's attack away from their centre line.", "RoomFormat": ["target", "defender_weapon.name", "caller"]},
            }

WEAPONBLOCKS = {"Noblock": NOBLOCK, "Dodges": DODGES, "Katanas": KATANABLOCKS, "Bo staves": BOBLOCKS}

def getCombatSuccess(args):
    """This will determine the success of the attack"""

    attack = args.key.title()
    weapon = args.obj
    weapon_type = args.obj.db.weapon_type
    caller = args.caller
    difficulty = args.difficulty

    target = args.target
    hitbox = args.hitbox

    if difficulty == "Easy":
        basic_attack_bonus = 0.75
    elif difficulty == "Average":
        basic_attack_bonus = 0.5
    elif difficulty == "Hard":
        basic_attack_bonus = 0.25
    else:
        basic_attack_bonus = 0.1

    defences = WEAPONMATCHUPS[weapon_type][attack]["Hitbox"][hitbox]

    # Modify success based on stats.
    raw_success = 95 - caller.db.stats['dex']*2 - caller.db.stats['spd'] + target.db.stats['agi']*2 + target.db.stats['spd']

    # Define how much offensive skills benefit attacks.
    attack_success_bonus = weapon.get_success_mod() * (
    caller.db.skills[weapon_type]['Basics']*basic_attack_bonus + caller.db.skills[weapon_type][attack.title()])

    raw_success -= attack_success_bonus
    caller.msg(raw_success)

    thresholds = {"Noblock Noblock": raw_success}

    # Define how much defensive skills benefit attacks.
    if not target.db.right_hand['Wielding']:
        if 'Dodges' not in target.db.skills:
            pass
        else:
            # Determine dodging bonus
            for defence in defences['Dodges']:
                caller.msg(defence)
                if defence in target.db.skills['Dodges']:
                    #Define difficulty bonus from Basics for the dodge.
                    dodging_difficulty = WEAPONBLOCKS["Dodges"][defence]["Difficulty"]
                    if dodging_difficulty == "Easy":
                        basic_dodging_bonus = 0.75
                    elif dodging_difficulty == "Average":
                        basic_dodging_bonus = 0.5
                    elif dodging_difficulty == "Hard":
                        basic_dodging_bonus = 0.25
                    else:
                        basic_dodging_bonus = 0.1

                    #Define effect of dodging on success, and add to raw success.
                    defence_success_bonus = (target.db.skills['Dodges'][defence] +
                                             target.db.skills['Dodges']['Basics']*basic_dodging_bonus)

                    raw_success += defence_success_bonus

                    #Define threshold number for this particular defence to be called if attack misses.
                    thresholds["Dodges" + " " + defence] = raw_success

                else:
                    pass
    else:
        defender_weapon = target.db.right_hand['Wielding']
        defence_success_bonus = {}

        if 'Dodges' not in target.db.skills:
            pass
        else:
            # Determine dodging bonus
            for defence in defences['Dodges']:
                if defence in target.db.skills['Dodges']:

                    # Define difficulty bonus from Basics for the dodge.
                    dodging_difficulty = WEAPONBLOCKS["Dodges"][defence]["Difficulty"]
                    if dodging_difficulty == "Easy":
                        basic_dodging_bonus = 0.75
                    elif dodging_difficulty == "Average":
                        basic_dodging_bonus = 0.5
                    elif dodging_difficulty == "Hard":
                        basic_dodging_bonus = 0.25
                    else:
                        basic_dodging_bonus = 0.1

                    defence_success_bonus["Dodges" + " " + defence] = (target.db.skills['Dodges'][defence] +
                                                     target.db.skills['Dodges']['Basics']*basic_dodging_bonus)

                else:
                    pass

            # Determine weapon defence bonus
        for defence in defences[defender_weapon.db.weapon_type]:
            if defence in target.db.skills[defender_weapon.db.weapon_type]:

                # Define difficulty bonus from Basics for the dodge.
                dodging_difficulty = WEAPONBLOCKS[defender_weapon.db.weapon_type][defence]["Difficulty"]
                if dodging_difficulty == "Easy":
                    basic_block_bonus = 0.75
                elif dodging_difficulty == "Average":
                    basic_block_bonus = 0.5
                elif dodging_difficulty == "Hard":
                    basic_block_bonus = 0.25
                else:
                    basic_block_bonus = 0.1

                defence_success_bonus[defender_weapon.db.weapon_type + " " + defence] = (target.db.skills[defender_weapon.db.weapon_type][defence] +
                                                                target.db.skills[defender_weapon.db.weapon_type]['Basics'] * basic_block_bonus)
            else:
                pass

        ordered_defence_bonuses = OrderedDict(sorted(defence_success_bonus.items(), key = lambda t: t[1], reverse = True))

        weighting = 1

        for defence in ordered_defence_bonuses:
            raw_success += ordered_defence_bonuses[defence]/weighting

            thresholds[defence] = raw_success
            caller.msg(thresholds[defence])

            weighting += 1

        # defence_success_bonus1 = target.db.skills[defender_weapon.weapon_type]['Basics']
        # for defence in defences[defender_weapon]:
        #     defence_success_bonus1 += target.db.skills[defender_weapon][defence]
        #     thresholds[defence] = defence_success_bonus1
        # if 'Dodges' not in target.db.skills:
        #     defence_success_bonus2 = None
        # else:
        #     defence_success_bonus2 = target.db.skills['Dodges']['Basics']
        #     for defence in defences['Dodges']:
        #         defence_success_bonus2 += target.db.skills['Dodges'][defence]
        #
        # # Weight bonuses based on which is most beneficial.
        # if not defence_success_bonus2:
        #     defence_success_bonus = defence_success_bonus1
        # elif defence_success_bonus1 > defence_success_bonus2:
        #     defence_success_bonus = defence_success_bonus1 + 0.5 * defence_success_bonus2
        # else:
        #     defence_success_bonus = defence_success_bonus2 + 0.5 * defence_success_bonus1

    # Determine raw success and refined success (between 5 and 95)
    refined_success = int(round(min(max(raw_success, 5), 95)))

    thresholds = OrderedDict(sorted(thresholds.items(), key = lambda t: t[1]))

    return raw_success, refined_success, thresholds

def getHit():
    return randint(1,100)

def getDamage(args, raw_success, hit):

    damage_mod = args.obj.get_damage_mod()

    strength_mod = args.caller.get_strength_mod()

    damage = round(damage_mod*strength_mod*(hit - raw_success)/10)

    return damage

def inflictDamage(obj, damage):
    #Applies damage to the target.
    target = obj.target

    target.db.vitals['current_hp'] -= damage
