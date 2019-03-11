from Scene import Scene

class SwordClass(Scene):

    def __init__(self):
        self.actions = ['go left', 'go up', 'pick sword']

    def left(self):
        return 'Hat'

    def up(self):
        return 'Bomb'

    def pick_sword(self, good_items):
        print('You have picked up the sword.')
        good_items['Sword'] = 'picked'
        self.actions.remove('pick sword')
        return 'picked'

    def enter(self, good_items):
        print('You entered a new room.')
        if good_items['Sword'] == 'not picked':
            print('There you can see a sword on the wall.')
        else:
            print('Not much is in it.')
        print('What would you do?')
        rc = ''

        while rc != 'Hat' and rc != 'Bomb':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go left':
                rc = self.left()
            elif answer == 'go up':
                rc = self.up()
            elif answer == 'pick sword':
                rc = self.pick_sword(good_items)
            else:
                rc = ''
        return rc
