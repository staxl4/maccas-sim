import random

sys_random = random.SystemRandom()

food_list = ["cheeseburger", "fries", "hamburger", "fries", "salad"]
death_list = [
    "the customer jumps over the table and suffocates you with your own food... harsh",
    "The customer calls down an air raid on the maccas. Slight overreaction",
    "The customer looks you dead in the eyes and tells you a secret that forever changed your life so you decided to run away to become a buddhist monk. To this day I dont know what they said",
    "Your customer takes a bottle of ketchup and summons satan from the underworld. upon the sight of the dissapointment of a meal you made satan shoots you without hesitation. Forver blessing this world.",
    "In the time it took you to whip up the dissapointment of a meal you made. Your customer managed to create a loophole in the fabric of the universe giving giraffes short necks. (giraffes are your favourite animal and you die of fright)",
    "On the sight of their food, your customer takes a bottle of bleach and 'accidentally' pours bleach into your eyes. Now you lowkey look like a tweaker",
    "The food looked so un-appetizing not even the local homeless guy would touch it. could it have really been that ba- OH MY EYES! IT BURNS!!!!",
]
inv = []
# clean oil - more valuable fries
# cool hat -  +5 energy every order
# faster learnin' - every time you make something the score is increased by .1 permanently

energy = 10
energy_up = 10
placeholder = ""
tutorial_active = True
food_made = False
drink_made = False
extras_made = False
score = 0
score_boost = 1
score_needed = 0.5
coins = 0
round_ = 1
count = 0


class upgrade:
    def __init__(self, name, cost, desc):
        self.name = name
        self.cost = cost
        self.desc = desc

    def cost_call(self, count):
        print(f"{count}. {self.name} is ${self.cost} coins. ({self.desc})")


cool_hat = upgrade("cool hat", 50, "+2 energy every order")
fresh_uniform = upgrade("fresh_uniform", 300, "for every $50 you have + 0.1 score")
faster_learnin = upgrade(
    "faster learnin'",
    250,
    "every time you make food your score boost is increased by .1 permanently",
)
better_patties = upgrade("better patties", 100, "increase score of cheeseburgers by 2")
coupon = upgrade("coupon", 1000, "halves all prices for next round")

shop_list = [cool_hat, fresh_uniform, faster_learnin, better_patties, coupon]


class person:
    def __init__(self, order):
        self.order = order

    def ordering(self):
        while True:
            tut = input(f"\nHey can I get a {self.order}? (y/n): ").strip().lower()

            if tut in ["y", "n"]:
                break
            elif tut == "":
                input("hi james stop breaking my game please")
            else:
                print("type like a normal person please")
        choice(tut, self.order, "", "", "")


sadie = person("")


class game_loop:
    def __init__(self):
        global energy_up
        global score_boost
        if "cool hat" in inv:
            energy_up += 5
        order_placed = sys_random.choice(food_list)
        sadie.order = order_placed
        sadie.ordering()


class choice:
    def __init__(self, x, meal, drink, extra1, extra2):
        self.x = x
        self.meal = meal
        self.drink = drink
        self.extra1 = extra1
        self.extra2 = extra2

        while True:
            if x.lower() == "y":
                food(meal)
                break
            elif x.lower() == "n":
                final_choice = input("Are you serious dude? (y/n)")
                if final_choice.lower() == "y":
                    quit()
                    break
                else:
                    print("thank god...")
                    food(meal)


class food:
    def __init__(self, food_choice):
        global tutorial_active
        global score
        self.food_choice = food_choice
        if better_patties in inv:
            if food_choice == "cheeseburger":
                score += 1
        while True:
            print(f"your current energy is {energy}")
            if tutorial_active:
                placeholder = " (Remember you have limited energy! put at least 5 in for this one. Scoring is (energy/10) * score_boost)"
            else:
                placeholder = ""
            print(f"\nYou must get {score_needed} score to impress your customer")
            energy_choice = int(input(f"how much energy would you like to use?{placeholder}: "))
            if energy_choice > energy:
                print("try again...")
            elif energy <= 0:
                print("how does one use less than one energy???")
                input("try again...")
            else:
                print(f"{food_choice} has been made!")
                scoring(energy_choice)
                break

            placeholder = ""


class scoring:
    def __init__(self, energy_used):
        global score
        global coins
        global energy
        global tutorial_active
        global score_boost
        global score_needed
        global round_
        self.energy_used = energy_used
        if "fresh_uniform" in inv:
            money_boost = coins / 100
            score_boost += money_boost
        score += (energy_used / 10) * score_boost
        money_boost = 0
        input(f"Nice! you got a score of {score}/10!")
        if score < score_needed:
            input("This is terrible!")
            input(sys_random.choice(death_list))
            quit()
        energy -= energy_used
        if "faster learnin'" in inv:
            score_boost += 0.1
        round_ += 1
        if tutorial_active:
            input("to finish off your shift and your tutorial, you will regain your energy and be able to buy equipment for yourself!")
            tutorial_active = False
        coin_gain = score * 100
        coins += coin_gain
        score_needed += 0.1 * round_
        input(f"you gained ${coin_gain} coins!")
        score = 0
        energy += energy_up
        shop()


class shop:
    def __init__(self):
        global count
        global coins
        global round_
        if "coupon" in inv:
            for i in range(len(shop_list)):
                item = shop_list[i]
                item.cost = item.cost / 2
                print(item.cost)

        if shop_list == []:
            input("you lowkey bought everything...")
            game_loop()

        choice_1 = sys_random.choice(shop_list)
        choice_2 = sys_random.choice(shop_list)
        print()
        choice_1.cost_call("1")
        choice_2.cost_call("2")
        print()

        if round_ == 10:
            input("You are too good at this...")
            input("Out of the 50 other employees...")
            input("You were the only one left...")
            input("...")
            input("look, I'll sell you the company. You clearly know it better than me.")
            input("but it wont come free!")
            input("pay up 100k and its yours!")
            input("--- Game To Be Continued ---")

            quit()

        while True:
            print(f"you have ${coins} coins!")
            shop_choice = input("what would you like to buy? (1 or 2. Leave blank if you dont want anything)")
            if shop_choice == "1":
                if coins >= choice_1.cost:
                    coins -= choice_1.cost
                    shop_list.remove(choice_1)
                    inv.append(choice_1.name)
                    break
                else:
                    print(f"You dont have enough coins for that! You have ${coins} coins")
                    break
            elif shop_choice == "2":
                if coins >= choice_2.cost:
                    coins -= choice_2.cost
                    shop_list.remove(choice_2)
                    inv.append(choice_2.name)
                    break
                else:
                    print(f"You dont have enough coins for that! You have ${coins} coins...")
            elif shop_choice == "":
                break
        print("You currently have: ")
        for i in range(len(inv)):
            print(inv[i])
        game_loop()


print("Welcome to your first day at Maccas!")
while tutorial_active:
    tut_choice = input("Would you like to complete a tutorial? (y/n) ")
    if tut_choice.lower() == "y":
        # tutorial stuffs
        tutorial_active = True
        print("tutorial")
        bleh = input("Type any key to continue ")
        if bleh == "any key to continue":
            print("you are welcome james now play the fuckin game")
            while True:
                input("...")
        input("This job is about taking orders and making the food required for your customers (1/3) ")
        input("The customer get constantly more and more needy (2/3) ")
        input("This game is also a roguelike so... good luck :) (3/3) ")
        input("Here is your first customer!")
        tut = input("\nHey can I get a cheeseburger? (y/n)")
        choice(tut, "cheeseburger", "", "", "")

    elif tut_choice.lower() == "n":
        tutorial_active = False
        game_loop()
        break

    else:
        print("Seriously? It's y or n...")
