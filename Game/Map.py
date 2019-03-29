from EmptyLeftUpper import EmptyLeftUpperClass
from Entrance import EntranceClass
from Bow import BowClass
from Wizard import WizardClass
from Hole import HoleClass
from Watchman import WatchmanClass
from Chit import ChitClass
from Ogre import OgreClass
from Hat import HatClass
from Exit import ExitClass
from Bomb import BombClass
from Sword import SwordClass
from Entry import EntryClass
from Troll import TrollClass
from Gold import GoldClass
from Back2Watchman import Back2WatchmanClass

class Map():

    def __init__(self, name):
        self.name = name
        print('%s is starting up' % self.name)

        EmptyLeftUpper = EmptyLeftUpperClass()
        Entrance = EntranceClass()
        Bow = BowClass()
        Wizard = WizardClass()
        Hole = HoleClass()
        Watchman = WatchmanClass()
        Chit = ChitClass()
        Ogre = OgreClass()
        Hat = HatClass()
        Exit = ExitClass()
        Bomb = BombClass()
        Sword = SwordClass()
        Entry = EntryClass()
        Troll = TrollClass()
        Gold = GoldClass()
        Back2Watchman = Back2WatchmanClass()
        
        self.rooms = {'EmptyLeftUpper': EmptyLeftUpper,
                      'Entrance': Entrance,
                      'Bow': Bow,
                      'Wizard': Wizard,
                      'Hole': Hole,
                      'Watchman': Watchman,
                      'Chit': Chit,
                      'Ogre': Ogre,
                      'Hat': Hat,
                      'Exit': Exit,
                      'Bomb': Bomb,
                      'Sword': Sword,
                      'Entry': Entry,                # dungeons
                      'Troll': Troll,                # dungeons
                      'Gold': Gold,                  # dungeons
                      'Back2Watchman': Back2Watchman # dungeons
                     }

    def get_room(self, room_name):
        return self.rooms[room_name]

    def enter(self, room_name, good_items):
        room = self.get_room(room_name)
        return room.enter(good_items)
