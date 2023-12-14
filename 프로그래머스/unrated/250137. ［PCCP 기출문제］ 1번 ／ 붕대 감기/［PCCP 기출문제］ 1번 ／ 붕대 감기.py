def solution(bandage, health, attacks):
    
    countinue_t =0
    max_hp = health
    end_time = attacks[-1][0]
    attack_dict = {}
    t = 0
    
    for attack in attacks:
        attack_dict[attack[0]] = attack[1]
    
    ##while t<= end_time:
    for t in range(end_time+1):
        if(t in attack_dict): ##key 있는지 확인
            health -= attack_dict[t]
            countinue_t = 0
             
            if(health <= 0):
                return -1
        else:
            countinue_t += 1
            if(countinue_t != bandage[0]):
                health += bandage[1]                
                if(health > max_hp):
                    health = max_hp
            if(countinue_t == bandage[0]):
                health += bandage[1] + bandage[2]
                if(health > max_hp):
                    health = max_hp
                countinue_t = 0
       ## t += 1
                                     
    return health