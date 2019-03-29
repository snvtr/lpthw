from Scene import Scene

class ChitClass(Scene):

    def __init__(self):
        self.actions = ['go right', 'go down', 'read paper']

    def right(self):
        return 'Exit'

    def down(self):
        return 'Ogre'

    def read_paper(self):
        print('You pick and read the chit which says: 'There is a sack of gold in the dungeon'')
        return 'sack of gold'

    def enter(self, good_items):
        print('You enter a small room. There is a table in the corner with a piece of paper on it.')
        print('What would you do?')

        rc = ''
        while rc != 'Exit' and rc != 'Ogre':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go right':
                rc = self.right()
            elif answer == 'go down':
                rc = self.down()
            elif answer == 'read paper':
                rc = self.read_paper()
            else:
                rc = ''
        return rc
