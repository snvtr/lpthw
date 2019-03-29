from Scene import Scene

class EmptyLeftUpperClass(Scene):

    def __init__(self):
        self.actions = ['look around', 'go right', 'go down']

    def enter(self, good_items):
        print('You are in an empty room. What would you do?')
        rc = ''
        while rc != 'Wizard' and rc != 'Entrance':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go down':
                rc = self.down()
            elif answer == 'go right':
                rc = self.right()
            elif answer == 'look around':
                print('You look around and see nothing')
                rc = ''
            else:
                rc = '' #rc = self.enter(good_items) # pass?
        return rc

    def right(self):
        return 'Wizard'

    def down(self):
        return 'Entrance'
