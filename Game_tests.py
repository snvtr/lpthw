from nose.tools import *

#from EmptyLeftUpper import EmptyLeftUpperClass
#from Entrance import EntranceClass
#from Bow import BowClass
#from Wizard import WizardClass
#from Hole import HoleClass
#from Watchman import WatchmanClass
#from Chit import ChitClass
#from Ogre import OgreClass
#from Hat import HatClass
#from Exit import ExitClass
#from Bomb import BombClass
#from Sword import SwordClass
#from Entry import EntryClass
#from Troll import TrollClass
#from Gold import GoldClass
#from Back2Watchman import Back2WatchmanClass
from Map import Map
from GoodItems import good_items

def setup():
    print('Setup')

def teardown():
    print('Tear down')

def test_Map():
    game_map = Map("My Game")
    print(good_items)