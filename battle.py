from os import system
import enemies


enemy1 = enemies.Skeleton()
hero1 = enemies.Hero()

def checkout_victory(enemy: object):
    if (enemy.life <= 0):
        print("{}THE PLAYER WINS{}".format("\033[1;44m", "\033[0m"))
        return True
    
    return False

def choice_option(hero):
    if (hero.defending == True):
        hero.defending = False

    choice = int(input("Enter 1 - to attack\nEnter 2 - to defend\nEnter 3 - to critical attack\nEnter 4 - to skip round\nEnter 5 - to exit battle >:(\n-> "))

    if (choice == 1):
        print("\nSkeleton life before attack: {}".format(enemy1.life))
        hero1.attack_enemy(enemy1)
        print("Skeleton life after attack: {}\n".format(enemy1.life))

    elif (choice == 2):
        hero1.active_defense()
    
    elif (choice == 3):
        hero1.critical_attack(enemy1)

    elif (choice == 4):
        print("\n{}The player skiped this round{}\n".format("\033[1;33m", "\033[0m"))
        return "skiped"
    
    elif (choice == 5):
        print("You choice forgot... ok, I understand.")
        return "coward"
    else:
        print("\n{}Please enter a valid option!{}\n".format("\033[1;31m", "\033[0m"))
        return "invalid"

def simulate_battle():
    round_counter = 1
    running = True
    while (running):

        if (checkout_victory(enemy1)):
            running = False
            break

        print("{}Round {}{}\n".format("\033[1;36m", round_counter, "\033[0m"))
        print("Enemy life: {}\n".format(enemy1.life))

        opt = choice_option()
        round_counter += 1

        if (opt == "skiped") or (opt == "invalid"):
            continue
        
        elif (opt == "coward"):
            running = False
            break
        
        system("pause")
        system("cls")
