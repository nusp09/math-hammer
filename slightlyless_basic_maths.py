hit_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
wound_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
save_dic = {1: 1,h 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
invul_save_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
fnp_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
save_bonus = 0 
hit_bonus = 0
wound_bonus = 0


invul = input("Do you have an invul save? (y/n): ").strip().lower()
fellnp = input("Do you have a feel no pain? (y/n): ").strip().lower()
mods = input("Do you have any hit, wound, or save modifiers? (y/n): ").strip().lower()

attacks = int(input("Enter the number of attacks: "))
to_hit = int(input("enter what you are hitting on. e.g. 2,3,4 ect: "))
to_wound = int(input("enter what you are wounding on. e.g. 2,3,4 ect: "))
ap = int(input("enter the AP of the weapon. e.g. 0,1,2 ect: "))
save = int(input("enter the save of the target. e.g. 2,3,4 ect: "))
if mods == 'y':
    hit_bonus = input("Do you have a hit bonus? (y/n): ").strip().lower()
    if hit_bonus == 'y':
        hit_bonus = int(input("enter the hit bonus. e.g. 0,1,2 ect: "))
    wound_bonus = input("Do you have a wound bonus? (y/n): ").strip().lower()
    if wound_bonus == 'y':
        wound_bonus = int(input("enter the wound bonus. e.g. 0,1,2 ect: "))
    save_bonus = input("Do you have a save bonus? (y/n): ").strip().lower()
    if save_bonus == 'y':
        save_bonus = int(input("enter the save bonus. e.g. 0,1,2 ect: "))


if invul == 'y':
    invul_save = int(input("enter the invul save of the target. e.g. 5,4,3 ect: "))
    invul_save = invul_save_dic[invul_save]
else:
    invul_save = save
if fellnp == 'y':
    fnp = int(input("enter the feel no pain of the target. e.g. 5,4,3 ect : "))
    fnp = fnp_dic[fnp]
else:
    fnp = 1
damage = int(input("enter the damage of the weapon. e.g. 1,2,3 ect: "))
target_wounds = int(input("enter the number of wounds per target: "))
hit = hit_dic[to_hit]
wound = wound_dic[to_wound]
save = save_dic[save]
def calculations(attacks, hit, wound, save, invul_save, fnp, damage, target_wounds):
    total_hit = attacks * hit
    total_wound = total_hit * wound
    save = save + ap
    save = save - save_bonus
    if save > invul_save:
        save = invul_save
    total_save = total_wound * save
    wounds = total_save * damage
    wounds = wounds * fnp
    kills = wounds / target_wounds
    return kills
print("you will kill",calculations(attacks, hit, wound, save, invul_save, fnp, damage, target_wounds),"models on average \nand you will do", calculations(attacks, hit, wound, save, invul_save, fnp, damage, target_wounds)*target_wounds, "wounds on average")