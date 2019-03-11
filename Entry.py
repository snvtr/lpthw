from Scene import Scene

class EntryClass():

    def __init__(self):
        self.items   = {'death counter': 0}
        self.actions = ['go through door', 'do nothing']

    def enter(self, good_items):
        print('You are in a hardly lit cold dungeon.', \
              'You cannot climb up the walls, they are slippery and very high.', \
              'You see a half-opened door in one wall.')
        rc = ''
        while rc != 'Troll':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go through door':
                rc = 'Troll'
            elif answer == 'do nothing':
                self.items['death counter'] += 1
                if self.items['death counter'] > 2:
                    self.death('You die of cold, hunger and thirst. Good job!')
            else:
                rc = ''
        return rc
