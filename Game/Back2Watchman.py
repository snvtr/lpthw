from Scene import Scene

class Back2WatchmanClass():

    def __init__(self):
        self.actions = ['go up', 'go down']

    def up(self):
        return 'Watchman'

    def down(self):
        return 'Gold'

    def enter(self, good_items):
        print('You enter a small room with a ladder to get out of the dungeon.')
        print('What would you do?')

        rc = ''
        while rc != 'Watchman' and rc != 'Gold':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go up':
                rc = self.up()
            elif answer == 'go down':
                rc = sel.down()
            else:
                rc = ''
        return rc
