from Scene import Scene
from sys import exit

class ExitClass(Scene):

    def __init__(self):
        self.actions = ['go out', 'go left', 'go down']

    def out(self):
        print('You reached the end of the maze! Congratulations!')
        exit(0)

    def left(self):
        return 'Chit'

    def down(self):
        return 'Bomb'

    def enter(self, good_items):
        print('You have reached the exit room.')
        
        rc = ''
        while rc != 'Bomb' and rc != 'Chit':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go out':
                rc = self.out()
            elif answer == 'go left':
                rc = self.left()
            elif answer == 'go down':
                rc = self.down()
            else:
                rc = ''
        return rc
