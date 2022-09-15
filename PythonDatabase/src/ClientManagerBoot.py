#The following statement is interrupted by a preprocessor statement.

#The original statement from the file ClientManagerBoot.cpp starts with:
#    snprintf(query, sizeof(query), "SELECT vnum, name, %s, type, rank, battle_type, level, " + "size+0, ai_flag+0, setRaceFlag+0, setImmuneFlag+0, " + "on_click, empire, drop_item, resurrection_vnum, folder, " + "st, dx, ht, iq, damage_min, damage_max, max_hp, regen_cycle, regen_percent, exp, " + "gold_min, gold_max, def, attack_speed, move_speed, " + "aggressive_hp_pct, aggressive_sight, attack_range, polymorph_item, " + "enchant_curse, enchant_slow, enchant_poison, enchant_stun, enchant_critical, enchant_penetrate, " + "resist_sword, resist_twohand, resist_dagger, resist_bell, resist_fan, resist_bow, "

#These cannot be handled by this converter.
#Modify this statement so that it is not interrupted by preprocessor statements and try the conversion again.