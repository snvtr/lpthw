from Scene import Scene

class WatchmanClass(Scene):

    def __init__(self):
        self.actions = ['go left',
                        'go right',
                        'use bow',
                        'use hammer']

    def left(self):
        return 'Bow'

    def right(self):
        return 'Hat'

    def use_bow(self, good_items):
        print('You think you can beat the watchman with this stick?')
        self.death('You are dead.')

    def use_hammer(self, good_items):
        print('You kill the watchman and you are alive!')
        good_items['Watchman'] = 'dead'
        self.actions.remove('use hammer')
        self.actions.remove('use bow')
        return 'dead watchman'

    def enter(self, good_items):
        if good_items['Watchman'] == 'alive':
            print('You enter the room and see an armed watchman on guard.', \
                  'He blocks the door. He sees you and attacks you.')
        else:
            print('You enter the room and see the dead watchman on the floor.')

        print('What would you do?')
        rc = ''
        while rc != 'Bow' and rc != 'Hat':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go left':
                if good_items['Watchman'] != 'alive':
                    rc = self.left()
                else:
                    self.death('The watchman catches you and kills you.')
            elif answer == 'go right':
                if good_items['Watchman'] != 'alive':
                    rc = self.right()
                else:
                    self.death('The watchman catches you and kills you.')
            elif answer == 'use bow':
                rc = self.use_bow(good_items)
            elif answer == 'use hammer':
                rc = self.use_hammer(good_items)
            else:
                rc = ''
        return rc

    
