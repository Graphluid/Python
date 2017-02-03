import time
import random


Atk=random.randrange(10,100)
Def=random.randrange(10,100)
Speed=random.randrange(1,10)
Dps=int(Atk/Speed)

xp=1
plevel=1

def xpgraphic():
    if xp<=plevel*5:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp<=plevel*10:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*15:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*20:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*25:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*30:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*35:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*40:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ████████▒▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*45:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 █████████▒▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*50:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ██████████▒▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*55:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ███████████▒▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*60:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ████████████▒▒▒▒▒▒▒▒▒")
    elif xp>=plevel*65:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 █████████████▒▒▒▒▒▒▒▒")
    elif xp>=plevel*70:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ██████████████▒▒▒▒▒▒▒")
    elif xp>=plevel*75:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ███████████████▒▒▒▒▒▒")
    elif xp>=plevel*80:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ████████████████▒▒▒▒▒")
    elif xp>=plevel*85:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 █████████████████▒▒▒▒")
    elif xp>=plevel*90:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ██████████████████▒▒▒")
    elif xp>=plevel*95:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ███████████████████▒")
    elif xp>=plevel*100:
        progress=print("                 .·´¯¯`·.¸",plevel,"¸.·´¯¯`·.","\n                 ████████████████████")
    return ""

input("""
||==================================================||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||      RESIZE THE WINDOW TO TOUCH THE BORDERS      ||
||                 THEN PRESS ENTER                 ||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||==================================================||""")
print("""













Greetings outlander...""")        #start#
time.sleep(1)

name=input("What is your name? ")

weapon=input("What is your weapon of choice? ")
time.sleep(1)

print("Oh wow! a",weapon,"isn't really my style but...")
time.sleep(1)

print("I'm sure I'll have one lying around here somwhere.")
print("*Searches around*")
time.sleep(2)
print("...")
time.sleep(2)
print("...Oh here it is!")
time.sleep(1)

def wepstats():                                  #print weapon Stats function
    print("A",weapon)
    print("Stats:\nAtk:",Atk)
    print("Def:",Def)
    print("Speed:",Speed)
    print("=======     Dps:",Dps,"     =======")
    return ""
    
print("\n\n\n\n=======You have been handed:=======")
print(wepstats())

wepname=input("\n\nDo you want to name your weapon?\nIf not just press enter: ")

if wepname=="":
    print("Your weapon will remain named:",weapon)
else:
    print("You have named your",weapon,":",wepname)
    weapon=wepname

etypelist=("Troll","Slime")
elevel=random.randrange(plevel-1,plevel+1)+1
etype=random.choice(etypelist)
ehp=elevel*100
ehpmax=elevel*100
php=plevel*100
phpmax=plevel*100

def playerhp():
    if php==phpmax/100*100:
        print(name,"lvl:",plevel,"\n██████████HP:",php,"██████████")
    elif php>=phpmax/100*90:
        print("\n██████████",php,"██████▒▒▒▒")
    elif php>=phpmax/100*80:
        print("\n██████████",php,"██████▒▒▒▒")
    elif php>=phpmax/100*70:
        print("\n██████████",php,"████▒▒▒▒▒▒")
    elif php>=phpmax/100*60:
        print("\n██████████",php,"██▒▒▒▒▒▒▒▒")
    elif php>=phpmax/100*50:
        print("\n████████▒▒",php,"▒▒▒▒▒▒▒▒▒▒")
    elif php>=phpmax/100*40:
        print("\n██████▒▒▒▒",php,"▒▒▒▒▒▒▒▒▒▒")
    elif php>=phpmax/100*30:
        print("\n████▒▒▒▒▒▒",php,"▒▒▒▒▒▒▒▒▒▒")
    elif php>=phpmax/100*20 or php<=phpmax/100*20:
        print("\n██▒▒▒▒▒▒▒▒",php,"▒▒▒▒▒▒▒▒▒▒")
    elif php>=phpmax/100*10:
        print("\n▒▒▒▒▒▒▒▒▒▒",php,"▒▒▒▒▒▒▒▒▒▒\nYou are dead!")
    return ""

def enemyhp():
    if ehp==ehpmax/100*100:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██████████",ehp,"██████████")
    elif ehp>=ehpmax/100*90:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██████████",ehp,"████████▒▒")
    elif ehp>=ehpmax/100*80:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██████████",ehp,"██████▒▒▒▒")
    elif ehp>=ehpmax/100*70:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██████████",ehp,"████▒▒▒▒▒▒")
    elif ehp>=ehpmax/100*60:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██████████",ehp,"██▒▒▒▒▒▒▒▒")
    elif ehp>=ehpmax/100*50:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n████████▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒")
    elif ehp>=ehpmax/100*40:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██████▒▒▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒")
    elif ehp>=ehpmax/100*30:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n████▒▒▒▒▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒")
    elif ehp>=ehpmax/100*20:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n██▒▒▒▒▒▒▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒")
    elif ehp>=ehpmax/100*10:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n█▒▒▒▒▒▒▒▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒")
    elif ehp<=ehpmax/100*10:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n█▒▒▒▒▒▒▒▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒")
    elif ehp<=0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n",etype,"Lvl:",elevel,"\n▒▒▒▒▒▒▒▒▒▒",ehp,"▒▒▒▒▒▒▒▒▒▒/nEnemy Defeated!")
        chance=1
    return ""


def pmoveN():
    print("""\n\n
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░▄░░░░░░░░░
    /░░░░░░░░╬░░░░░░░░\\
    \░░░░░░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    
    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░▄░░░░░░░░░
    ░░░░░░░░░╬░░░░░░░░░
    /░░░░░░░░░░░░░░░░░\\
    \░░░░░░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")

    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░▄░░░░░░░░░
    ░░░░░░░░░╬░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░░░░░░\\
    \░░░░░░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    return ""

#==============================#

def pmoveE():
    print("""\n\n
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░▄░░░░░░\\
    \░░░░░░░░░░╬░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")

    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░▄░░░░\\
    \░░░░░░░░░░░░╬░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")

    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░░░▄░░\\
    \░░░░░░░░░░░░░░╬░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    
    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░░░░░▄\\
    \░░░░░░░░░░░░░░░░╬/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    return ""

#==============================#

def pmoveS():
    print("""\n\n
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░░░░░░\\
    \░░░░░░░░▄░░░░░░░░/
    ░░░░░░░░░╬░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    
    time.sleep(.5)
    
    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░░░░░░\\
    \░░░░░░░░░░░░░░░░░/
    ░░░░░░░░░▄░░░░░░░░░
    ░░░░░░░░░╬░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    
    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░░░░░░░░░░\\
    \░░░░░░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░▄░░░░░░░░░
    ░░░░░░░░░╬░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    return ""

#==============================#

def pmoveW():
    print("""\n\n
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░▄░░░░░░░░░░\\
    \░░░░░░╬░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")

    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░▄░░░░░░░░░░░░\\
    \░░░░╬░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")

    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░▄░░░░░░░░░░░░░░\\
    \░░╬░░░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    return ""
    
    time.sleep(.5)

    print("""
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /▄░░░░░░░░░░░░░░░░\\
    \╬░░░░░░░░░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░\n""")
    return ""

darkroom="""\n\n
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n"""


emptyroom="""\n\n
    You are in an empty room with four exits
    ░░░░░░░░░^░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    /░░░░░░░░▄░░░░░░░░\\
    \░░░░░░░░╬░░░░░░░░/
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░V░░░░░░░░░"""

chance=1
inemptyroom=1

while inemptyroom==1:
    ehp=ehpmax
    elevel=random.randrange(plevel-1,plevel+1)+1
    etype=random.choice(etypelist)
    print(chance)
    print(emptyroom)
    pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")

    while chance<=30:     #Chance for empty room#
        if pmove=="N" or pmove=="n":
            print(pmoveN())
            print(darkroom)
            time.sleep(.2)
            print(emptyroom)
            chance=random.randrange(100)
            pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")

        elif pmove=="E" or pmove=="e":
            print(pmoveE())
            print(darkroom)
            time.sleep(.2)
            print(emptyroom)
            chance=random.randrange(100)
            pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")

        elif pmove=="S" or pmove=="s":
            print(pmoveS())
            print(darkroom)
            time.sleep(.2)
            print(emptyroom)
            chance=random.randrange(100)
            pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")

        elif pmove=="W" or pmove=="w":
            print(pmoveW())
            print(darkroom)
            time.sleep(.2)
            print(emptyroom)
            chance=random.randrange(100)
            pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")

        else:
            print("\nPlease choose a valid direction to move in.\n")
            pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")
            
        if 30<chance<=95:     #chance for encounter
            if pmove=="N" or pmove=="n":
                print(pmoveN())
                print(darkroom)
                time.sleep(.2)
            elif pmove=="E" or pmove=="e":
                print(pmoveE())
                print(darkroom)
                time.sleep(.2)
            elif pmove=="S" or pmove=="s":
                print(pmoveS())
                print(darkroom)
                time.sleep(.2)
            elif pmove=="W" or pmove=="w":
                print(pmoveW())
                print(darkroom)
                time.sleep(.2)
            input("""
@xxxxxx[{::::::::::::::>Combat<::::::::::::::}]xxxxxx@
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
||          You have encountered an enemy!          ||
||             Press enter to continue:             ||
||                                                  ||
||                                                  ||
||                                                  ||
||                                                  ||
@xxxxxx[{::::::::::::::>Combat<::::::::::::::}]xxxxxx@
    """)
            
            print("@xxxxxx[{::::::::::::::>COMBAT<::::::::::::::}]xxxxxx@")
            estatus=print("               ",etype,"Lvl:",elevel,"\n               ██████████",ehpmax,"██████████")
            print("""
                        _    __    
                       | |  / /____
                       | | / / ___/
                       | |/ (__  ) 
                       |___/____(_)
            """)
            pstatus=print("               ",name,"Lvl:",plevel,"\n               ██████████",php,"██████████")
            input("               Press Enter to continue:\n@xxxxxx[{::::::::::::::>COMBAT<::::::::::::::}]xxxxxx@\n")
            
            print("\n\n\n\n\n\n","======= Your wep stats are: =======\n")
            print(wepstats())
            ehp=ehpmax

            while ehp>0:
                print(ehp)
                print(enemyhp())
                AtkMove=input("Rapidly press enter to attack: ")
                ehp=ehp-Dps
            if ehp<=0:
                xpgain=random.randrange(1,ehpmax, 10)
                xp=xp+xpgain
                plevel=int(xp/100)
                php=plevel*100
                print("\n\n\n\n@xxxxxx[{::::::::::::::>COMBAT<::::::::::::::}]xxxxxx@\n\n")
                print("           You have defeated",etype,"Level:",elevel,"\n           and gained",xpgain,"XP towards level",plevel+1)
                print("                       ",name,"\n                ██████████",php,"██████████")
                print(xpgraphic())
                input("                  Enter to continue:\n\n\n\n@xxxxxx[{::::::::::::::>COMBAT<::::::::::::::}]xxxxxx@")
                chance=1
                inemptyroom=1
                print(emptyroom)
                time.sleep(.2)
                pmove=input("Which direction would you like to travel in? \n N,E,S or W: ")
            else:
                input("Whaddafuck to i do now?")


        elif 95<chance<=100:  #chance for shop#
            chance=1
            print("You have found a shop.")
            shop=input("""
            You have found a shop!
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░▄░░░░░░░░░
            ░░░░░░░░░╬░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░
            1: To buy stats
            2: To buy HP
            3: To Leave
            """)
            if shop==1:
                print("You are now buying stats.")
            elif shop==2:
                print("You are now buying HP.")
            elif shop==3:
                print("You have left the shop")
                inemptyroom=1
            else:
                print("Choose an option.")

