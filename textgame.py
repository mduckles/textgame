from os import system
from random import randint
import yaml

config = yaml.load(file('config.yaml'))
races = config['races']
weapons = config['weapons'].keys()
classes = config['classes']
first_monsters = config['first_monsters']
locations = config['locations']


def say(message,output=False):
    ''' Say a message through the Mac `say` command '''
    system('say "%s"' % message)
    if output:
        print message

def pickrand(inlist):
    ''' Picks a random item from a list'''
    return inlist[randint(0,len(inlist)-1)]

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

def setupchar():
    race = character(races)
    charclass = character(classes,mode='class')
    say('You will be a %s %s' %(race,charclass))
    return {'race': race, 'charclass': charclass}

character = {'race': 'Eladrin', 'charclass': 'Wizard'}

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
    say('You are in a %s' % scene['loc'], output=True)
    scene['monst'] = pickrand(first_monsters)
    say('There is a %s there' % scene['monst'], output=True)
    scene['weap'] = pickweapon()
    say("You can attack first.", output=True)
    attack(scene)

def weapon(weap):
    about = config['weapons'][weap]
    print "%s can attack at %s with up to %s dammage" % (weap, about['range'], about['die'])
    res = roll(about['die'])
    print "Your first roll was %s" % res

def roll(d):
    return randint(1,d)

def attack(scene):
    say("You are in a %s with a %s, you are holding a %s" % (
    scene['loc'], scene['monst'], scene['weap']
    ), output = True)
    weapon(scene['weap'])


#print setupchar()
#scene()
weapon('javelin')
