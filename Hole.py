from Scene import Scene
from time import sleep

class HoleClass(Scene):

    def __init__(self):
        pass

    def enter(self, good_items):
        print('You entered the dark room where you can see nothing.')
        sleep(3)
        print('Suddenly you slip and fall down the hole.')
        return 'Entry'
              
