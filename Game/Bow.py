from Scene import Scene

class BowClass(Scene):

    def __init__(self):
        self.actions = ['go right', 'go up', 'pick bow']

    def enter(self, good_items):
        print('You are in a room.')
        if good_items['Bow'] == 'not picked':
            print('There is a bow on the floor.')
        print('What would you do?')
 
        rc = ''
        while rc != 'Watchman' and rc != 'Entrance':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go right':
                rc = self.right()
            elif answer == 'go up':
                rc = self.up()
            elif answer == 'pick bow':
                rc = self.pick_bow(good_items)
            else:
                rc = ''
        return rc

    def right(self):
        return 'Watchman'

    def up(self):
        return 'Entrance'
    
    def pick_bow(self, good_items):
        if good_items['Bow'] == 'not picked':
            print('You have picked up the bow')
            self.actions.remove('pick bow')
            good_items['Bow'] = 'picked'
            return 'picked'
        print('You already have it! Do you not remember?')
        return 'not picked'
