attacks = int(input("Enter the number of attacks: "))
to_hit = int(input("enter what you are hitting on. e.g. 2,3,4 ect: "))
to_wound = int(input("enter what you are wounding on. e.g. 2,3,4 ect: "))
ap = int(input("enter the AP of the weapon. e.g. 0,1,2 ect: "))
save = int(input("enter the save of the target. e.g. 2,3,4 ect: "))
hit_bonus = int(input("enter the hit bonus. e.g. 0,1,2 ect: "))
wound_bonus = int(input("enter the wound bonus. e.g. 0,1,2 ect: "))
save_bonus = int(input("enter the save bonus. e.g. 0,1,2 ect: "))
invul_save = int(input("enter the invul save of the target. e.g. 5,4,3 ect: "))
fnp = int(input("enter the feel no pain of the target. e.g. 5,4,3 ect : "))
damage = int(input("enter the damage of the weapon. e.g. 1,2,3 ect: "))
target = int(input("enter the number of targets: "))
target_wounds = int(input("enter the number of wounds per target: "))
hit_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
wound_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
save_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
invul_save_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
fnp_dic = {1: 1, 2: 5/6, 3: 4/6, 4: 0.5, 5: 2/6, 6: 1/6}
hit = hit_dic[to_hit]
wound = wound_dic[to_wound]
save = save_dic[save]
fnp = fnp_dic[fnp]
def calculations(attacks, hit, wound, save, invul_save, fnp, damage, target, target_wounds):
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
print(calculations(attacks, hit, wound, save, invul_save, fnp, damage, target, target_wounds))
