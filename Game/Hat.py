from Scene import Scene

class HatClass(Scene):

    def __init__(self):
        self.actions = ['go left', 'go right', 'pick hat']

    def left(self):
        return 'Watchman'

    def right(self):
        return 'Sword'

    def pick_hat(self, good_items):
        print('You have picked the hat.')
        good_items['Hat'] = 'picked'
        self.actions.remove('pick hat')
        return 'picked'
    
    def enter(self, good_items):
        print('You enter a room')
        if good_items['Hat'] == 'not picked':
            print('There is a pointy hat on the floor.')
        else:
            print('There is nothing else in the room.')
        print('What would you do?')

        rc = ''
        while rc != 'Watchman' and rc != 'Sword':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go left':
                rc = self.left()
            elif answer == 'go right':
                rc = self.right()
            elif answer == 'pick hat':
                rc = self.pick_hat(good_items)
            else:
                rc = ''
        return rc
