print("Python ran.py")
we_live_on = "Earth"
apocolypse_days = 321
appocolyps = str(apocolypse_days) + " days remaining"
enemy = "Martians"
continent = "Europe"
north_west = "Russia"
surrender = "Join"
vap = "vaporize"
print(we_live_on)
print(appocolyps)
print(enemy)
print("We are the only surviving inhabitants of", we_live_on,".")
print("There is an appocolypse coming which leaves us with ", appocolyps, "until the oxygen has leaked out of the ozone layer.")
print("We are under attack by the", enemy, "they made the hole bigger in the already pollution created hole.")
print(f"The {enemy} then invaded {continent}, then expanded west and slowly east.")

def nuke():
    print("Nuke the sons of B*TCHES!)")
    print("The nuke bounces of an invisible force field and deflects back to you")
    print(f"{vap} into ashes!")

def bunker():
    print("You survive long enough to reach the last stronghold of humanity.")
    print("Will you join the resistance or will you remain in the bunker.")
    print("BUNKER!")
    print("You have 1234 allies")
    print("You withdraw to the bunker, preparing for war and call on your allies")

def martian_fight():
    print(f"The {enemy} take over {we_live_on} they caprtue every last survivor and give the option to {surrender} or be {vap}")
    response = input("Join or vaporize?\n")
    if surrender.lower() == response :
        print(f"Morph into {enemy}")
        print("After you morph you join their army and fight against the resistance")
    elif surrender.upper() == response :
        print("the procedure fails and you remain human they thought you were dead and discard your body suddenly air fills your lungs but you are not the same will you return to the bunker or hide in the shadows")
        bunker()
        war_machine()
    elif vap.lower() == response.lower():
        print("You are disintergrated into ashes")

response = input(f"You are held up in {north_west} with how many days remaining?\n")

def war_machine():
    global attempts
    attempts = 0

    def pin_func(): 
        pin = input("How many requests for allies do you send...\n")
        if pin == "1234":
            print("Allies respond")
            balance_func()
        else:
            print("Allies ignored you!")
            global attempts
            attempts += 1
            if attempts  >= 3:
                print("We have seized your army for security purposes...you will loose the war\nHave a nice day.")
            else:
                pin_func() 

    def balance_func(): 
        global balance, withdrawal, allies
        allies = 5000
        withdrawal = input("How many troops would you like to call forth?\n")
        if int(withdrawal) <= allies:
            print("Accessing account...")
            withdraw_func() 
        else:
            print("Insufficient allies!")
            balance_func() 

    def withdraw_func(): 
        global allies, withdrawal
        new_balance = allies - int(withdrawal)
        print(f"Please take your troops and may you prosper.\n Don't forget your army.\nYou have {new_balance} allies remaining")

    pin_func()
if response == str(apocolypse_days) and north_west == "Russia":
    response = input ("Will you fight?\n")
    if response.lower() == "no":
        bunker()
        war_machine()

    else:
        print("resistance you get captured")
        martian_fight()
else:
    print(f"The {enemy} attacked early and caught the survivors by surprise.")
    nuke()