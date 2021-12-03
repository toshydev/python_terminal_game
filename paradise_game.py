# imported Modules:
import time, random, sys

# global Variables:
def next_page():
    for i in range(10):
        print("\n")
        time.sleep(0.1)

def typeText(text, sec=0.05):
    for char in text: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(sec)

def endText():
    print("\n")
    print(".".center(100))
    time.sleep(0.5)
    print(".".center(100))
    time.sleep(0.5)
    print(".".center(100))
    time.sleep(0.5)
    print(".".center(100))
    time.sleep(0.5)
    print(".".center(100))
    time.sleep(0.5)
    print(".".center(100))        
    print("\n")
    time.sleep(1)
    print("The End".center(100))
    time.sleep(1)
    print("Thank you for playing!".center(100))
    time.sleep(1)
    print("Goodbye".center(100))
    time.sleep(2)
    sys.exit()

def playerInput():
    print("Press any key + ENTER to continue. Press 'Q' + ENTER to exit.".center(100))
    start_bn = input()
    while True:
        if start_bn.lower() == "q":
            endText()
        else:
            break

# Game start:
print("".center(100, "="))
print(" A Day In Paradise ".center(100, "="))
print("                      ".center(100, "="))
print(" a digital novel by A.Roshkov ".center(100, "="))
print("".center(100, "="))
print("\n")
print("\n")
time.sleep(2)
playerInput()

# starting game:
print("\n")
print("loading".center(100))
print("\n")
time.sleep(1)
print("3".center(100))
time.sleep(1)
print("2".center(100))
time.sleep(1)
print("1".center(100))
time.sleep(1)

next_page()

# Intro:
intro_text = """
Dec 15th, 2023

Some people believe that our lives are a constant path that unavoidably leads to death.
All we can do is fill the little time we have into actions that make us believe we matter.

That we matter more than others.

I refuse to live by such beliefs!
We all have our traumas, rock-bottoms, crises but how can you overcome the struggle when 
you lay your power to change something into the hands of an eternal being that just sounds like
the father of all excuses?

I won't live by such beliefs!

I'd rather risk my life!

Fuck you, Sesh!

PAM

"""
print("".center(100, "*"))
time.sleep(0.5)
typeText(intro_text, 0.01)
time.sleep(1)
print("".center(100, "*"))
playerInput()

# Main game:
wake_up_text= """
I snooze the alarm.

My diary has to put up with my worst self.
I am using it and abusing it with my thoughts. Not to mention the horrific 
handwriting I present it with but if it wasn't for this little book of horrors
I might not even be able to write my name in cursive anymore.
What will it be like, 30 years from now, when all the free pens that were handed out as
promotionals gifts fill up long forgotten desks without anyone knowing how to use them.
Nobody thinks about that.
The alarm again. Snooz.
Is this what Sesh meant? Is this the fate of pens? The constant in life one can only accept?
What a load of bullshit! If she's so keen on accepting her struggle as destiny and stop working
on a better life for herself, be my guest.
Why do people always get all philosophical and political or religious after a couple of beers?
I'm glad she left in the end. I couldn't have spent the whole night wasting my time on this crap.
Wait, the alarm!
Fuck, it's almost nine!
I jump up from my bed, diary left open. I'm already wearing sweatpants and a hoodie - the winter
got cold early this year, It's not even christmas.
Half an hour until I'm meeting my boss, I have to hurry. It's at "Le Chou", a cute cafe two blocks
away from the company. They have soft and crispy french croissants which they serve with apricot jam. 
Disgusting, but my boss loves it. She studied in europe I guess.
It will take 20 minutes to get there and I still need my coffee. 
Come on, Pam, think!
"""
typeText(wake_up_text, 0.01)
typeText("...", 0.5)
time.sleep(0.5)
print("\n")
typeText("... 9:00 ... (30 minutes remaining)", 0.1)
time.sleep(0.5)
print("\n")
pam_inv = {}
backpack = {}
home_inv = {1: "Keys", 2: "Phone", 3: "Wallet", 4: "Headphones", 
            5: "Charger", 6: "Laptop", 7: "Water", 8: "Food", 9: "Backpack"}

print("I need to pack my things quickly! What do I need?")
print("\n")
print(" Items nearby ".center(25, "#"))
for key, value in home_inv.items():
    print(str(key).ljust(20, "."), value.rjust(5, " "))
print("Press a number + ENTER to collect an item. To quit press Q + ENTER")
while True:
    choice = input()
    if choice.lower() == "q":
        break
    if choice.isdecimal() == False or (int(choice) < 1 or int(choice) > 9):
        print("Pick a number from 1 to 9 and press ENTER. To quit press Q + ENTER")
        continue
    if 9 not in pam_inv.keys() and (int(choice) >= 5 and int(choice) <= 8):
        print("You can't put this in your pockets. You need a backpack.")
        continue
    pam_inv.setdefault(int(choice), home_inv.get(int(choice)))
print(" Inventory: ".center(20, "#"))
for item in pam_inv.values():
    print(item.ljust(20, "."))
typeText("...", 0.5)
time.sleep(0.5)
print("\n")
typeText("... 9:05 ... (25 minutes remaining)", 0.1)
time.sleep(0.5)
print("\n")
print("I close the door behind me.")
playerInput()
lets_go_text= """
And run down the stairs while trying to figure out which way will be the fastest to get to "Le Chou".
I could take my bike but lose five minutes, trying to unlock the rusty chain I use, to secure it against
the certain loss I'd suffer if I didn't.
9:06.
The most obvious solution would be to take a cab. I'd waste ten bucks for a ride that won't even assure to
get me to the meeting on time. One accident or a wave of red lights is all it takes to lose ten valuable minutes.
9.07.
Damn, I forgot to switch on my phone. I started switching it off recently when I go to bed and began trusting
the old alarm clock I found someone left on their front-porch. It helps me fall asleep and lets me forget the
ever pacing digital world I work in and have become a valuable part of.
It's a Samsung. Not the newest but it get's the job done and has a relatively fast boot time.
Checking the trains now, which is the easiest and most reliable way of getting to "Le Chou".
The L-Train leaves from Bushwick Station at 9:10. I'll need 18 minutes to get to James Ave and another minute
of running to "Le Chou". Close call!
Come on, Pam. Think!
"""
typeText(lets_go_text, 0.01)
typeText("...", 0.5)
time.sleep(0.5)
print("\n")
typeText("... 9:08 ... (22 minutes remaining)", 0.1)
time.sleep(0.5)
print("\n")
path = {"Bike": "20 min, 66% chance of succes", "Taxi": "15 min, 50% chance of succes", 
        "Train": "18 min, 80% chance of succes"}
bike_chance = random.randint(1, 3)
taxi_chance = random.randint(0, 1)
train_chance = random.randint(1, 5)
# storylines: 1 = Bike success, 2 = Bike failure, 3 = Taxi success, 4 = Taxi failure, 
# 5 = Train success, 6 = Train failure, 7 = Walk success, 8 = Walk failure
storyline = 0
choices = ["bike", "taxi", "train"]
print("Pick a transport, e.g. [Bike] + ENTER, press Q + ENTER to walk")
print(" Transport ".center(50, "#"))
for key, value in path.items():
    print(key.ljust(20, "."), value.rjust(30, " "))
while True:
    choice = input()
    if choice.isalpha() == False or choice.lower() not in choices:
        print("Type [Bike], [Taxi] or [Train] + ENTER")
    if choice.lower == "q":
        print("""
No way I can make it in time. Even if I ran it would take almost an hour to get to 'Le Chou'.
What was I thinking?
        """)
    if choice.lower() == "bike":
        typeText("Looking for the key ...", 0.1)
        time.sleep(0.5)
        if "Keys" in pam_inv.values():
            print(" Found it!")
            typeText("Unlocking ...", 0.1)
            time.sleep(0.5)
            if bike_chance >= 2:
                print(" Unlock successfull!")
                storyline = 1
                break
            else:
                print(" The key broke!")
                pam_inv.pop(1)
                print("\n")
                print("I won't make it. Better call my boss.")
                storyline = 2
                break
        else:
            print("I forgot my keys!")
            print("\n")
            print("I won't make it. Better call my boss.")
            storyline = 2
            break
    if choice.lower() == "taxi":
        typeText("I holler at a cab that drives past me ...", 0.1)
        time.sleep(0.5)
        typeText(" No luck yet ...", 0.1)
        time.sleep(0.5)
        print(" There! Finally!")
        time.sleep(0.5)
        print("""
I rush inside the yellow cab. That's odd. Most of the cars are black nowadays.
"James and Richardson Ave, hurry!" I tell the driver. The car smells of old nicotine
and cheap black coffee. This guy, who probably had a hard time getting into this
vehicle, even though it's quite spacey, doesn't stand a chance at getting a healthier
way of life. He's stuck in this car, stuck in this job, stuck in this life. 
I feel sorry for him.

I just hope there's not too much traffic on the way to "Le Chou".
        """)
        if taxi_chance == 1:
            storyline = 3
            break
        else:
            print("""
I can't believe this shit!
When did this fucking city decide to rebuild itself on every corner at the same time?
The car is standing inside a shining ocean of metal. Just without waves.
It's been 15 minutes of car horns, Fat Joe on Hot97 and suicidal bike drivers, which could
be me.
9:25.
Better call my boss.
            """)
            storyline = 4
            break
    if choice.lower() == "train":
        print("""
The downtown L-Train is my best chance. I start running. If I don't stop I can
make it to the station just in time to hop on.
Dodging pedestrians on the sidewalk, I jaywalk over a red light. If I get hit by a car,
at least I have a good enough reason to be late, I tell myself, wondering how such a
stupid thought could find its way into my - as I like to think - rational brain.
I see the stairs leading into the underground station. Two steps at a time I jump down.
One more flight of stairs, I can already hear the train arriving. It stops and the doors open.
One second, two seconds, three. The closing-door alarm goes off and I slide into the train
just before the opening becomes too small.
I did it!   
9:11.
The train is one minute late.
Had it been on time, I wouldn't have made it.
But I lost one minute and my punctuality for the meeting now depends on the speed of
the train.       
        """)
        if train_chance < 5: # train ride goes smooth, arrives on time
            typeText("Calm down, Pam. Now get your head clear.", 0.1)
            time.sleep(0.5)
            typeText(" I hope I didn't forget anything.", 0.1)
            time.sleep(0.5)
            print("""
I sit down on one of the blue plastic seats with one free seat on each side.
The car is only half full. It's too late for rush hour.
That was too close.
My eyes get heavy with relief about the good luck of the past five minutes.
9:13            
            """)
            storyline = 3
            break
        else:
            print("""
The doors are closed. But why are we waiting?
"Dear passengers, the departure of this train is currently delayed for the reason of
an ongoing police investigation. The new departure time is 09:20. We apologize for the inconvenience." 
The speaker system of the car just nullified all my efforts to be on time.
In such moments, I think there are only few people who don't ask themselves the typical
question:
"Why now? Why me?"
Stupid question.
I better call my boss. There's no chance I'll make it.
            """)
            storyline = 4
            break
if storyline == 2 or storyline == 4 or storyline == 6 or storyline == 8:
    endText()
if storyline == 1 or storyline == 3 or storyline == 5 or storyline == 7:
    print("I made it!")
    print("Running this early makes me sick to the stomach. Beth will think I overslept.")
    print("There's 'Le Chou'! How I hate that apricot jam!")

# Outro:

