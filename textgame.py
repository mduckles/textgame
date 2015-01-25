from os import system
from random import randint

def say(message):
  system('say "%s"' % message)

races = ['Dragonborn', 'Dwarf', 'Eladrin', 'Elf', 'Half Elf', 'Halfling', 'Human', 'Tiefling' ]

def character(listof, mode='race'):
    msg = "Which %s would you like to be" % mode
    print msg
    say(msg)
    for kind in listof:
        say(kind)
        print kind
    selection = raw_input('?')
    say("You have selected %s" % selection)
    return selection

classes = ['Cleric', 'Wizard', 'Fighter', 'Ranger', 'Rogue', 'Warloc', 'Warlord', 'Paladin', '']

def setupchar():
    race = character(races)
    charclass = character(classes,mode='class')
    say('You will be a %s %s' %(race,charclass))
    return {'race': race, 'charclass': charclass}

#print setupchar()
character = {'race': 'Eladrin', 'charclass': 'Wizard'}

locations = ['Dungeon', 'Village', 'Castle', 'Forest', 'Lake', 'Desert', 'Mountain', 'Plains', 'Woodland']
first_monsters = ['Hipogrith', 'Troll', 'Orc', 'Goblins' ]
weapons = ['spear', 'dagger', 'javelin', 'club', 'long bow', 'short bow', 'short sword', 'long sword']

def pickrand(inlist):
    ''' Picks a random item from a list'''
    return inlist[randint(0,len(inlist)-1)]

def pickweapon():
    say("Which weapon would you like to place in your hand?")
    for weapon in weapons:
        print weapon
    weapon = raw_input('?')
    return weapon

def scene():
    ''' Set a random scene '''
    scene = dict()
    scene['loc'] = pickrand(locations)
    say('You are in a %s' % scene['loc'])
    scene['monst'] = pickrand(first_monsters)
    say('There is a %s there' % scene['monst'])
    scene['weap'] = pickweapon()
    say("You can attack first.")
    attack(scene)

def attack(scene):
    say("You are in a %s with a %s, holding a %s" % (
    scene['loc'], scene['monst'], scene['weap']
    ))


scene()
