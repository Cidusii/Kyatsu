from __future__ import unicode_literals

from django.db import models

# Create your models here.
class WeaponMatchups(models.Model):
    "A simple model for storing weapon matchups table"
    db_weapon_type = models.CharField(max_length=80, db_index = True)
    db_attack = models.CharField(max_length=80, db_index = True)
    db_difficulty = models.CharField(max_length=80, db_index = True)
    db_hitbox = models.CharField(max_length=80, db_index = True)
    db_blocks_dodges = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_shields = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_katana = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_bo = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_rogatina = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_sai = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_spear = models.CharField(max_length=80, null=True, blank=True)
    db_blocks_axe = models.CharField(max_length=80, null=True, blank=True)
