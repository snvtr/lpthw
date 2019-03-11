from Scene import Scene

class OgreClass(Scene):

    def __init__(self):
        self.actions = ['go up', 'go right', 'attack', 'use bomb']
   
    def up(self):
        return 'Chit'

    def right(self):
        return 'Bomb'

    def use_hammer(self):
        if good_items['Hammer'] == 'picked':
            self.death('You attack the Ogre with the hammer but the Ogre is too big and powerful. You die.')
        return 'fail'

    def use_bomb(self, good_items):
        if good_items['Bomb'] == 'picked':
            print('You throw the bomb at the ogre and run away.')
            good_items['Ogre'] = 'dead'
            good_items['Bomb'] = 'used'
            self.actions.remove('use bomb')
            self.actions.remove('attack')
            return 'Bomb'
        else:
            self.death('You do not have the bomb! The Ogre catches you and bites your head off!')
            return 'fail'

    def enter(self, good_items):
        if good_items['Ogre'] == 'alive':
            print('You see a huge Ogre in front of you. What would you do?')
        else:
            print('You see a dead Ogre on the floor. The bomb killed him. What would you do next?')

        rc = ''
        while rc != 'Chit' and rc != 'Bomb':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go up':
                rc = self.up()
            elif answer == 'go right':
                rc = self.right()
            elif answer == 'attack':
                rc = self.attack(good_items)
            elif answer == 'use bomb':
                rc = self.use_bomb(good_items)
            else:
                rc = ''
        return rc

      
