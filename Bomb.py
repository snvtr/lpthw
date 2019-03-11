from Scene import Scene

class BombClass(Scene):

    def __init__(self):
        self.items   = {'Door' : 'not broken'}
        self.actions = ['go left', 'go down', 'pick bomb', 'throw bomb at door', 'break door']

    def left(self):
        if self.items['Door'] == 'broken':
            return 'Ogre'
        else:
            print('You cannot go, there is a door in front of you, do you see it?')
            return 'fail'

    def down(self):
        return 'Sword'

    def pick_bomb(self, good_items):
        print('You have picked up the bomb. You can know use it against something or someone.')
        good_items['Bomb'] = 'picked'
        self.actions.remove('pick bomb')
        return 'picked'

    def throw_bomb(self):
        self.death('You are throwing the bomb against the door. The bomb goes off and kills you.')

    def break_door(self, good_items):
        if good_items['Hammer'] == 'picked':
            print('You have broken down the door and can go into the next room.')
            self.actions.remove('break door')
            self.actions.remove('throw bomb at door')
            self.items['Door'] = 'broken'
            return 'broken'
        else:
            print('How can you break down the door if do not have tools?')
            return 'fail'

    def enter(self, good_items):
        print('You enter a room and there a box on the floor.')
        if good_items['Bomb'] == 'not picked':
            print('You came to the box and see a bomb in it.')
        else:
            print('The box is empty.')
        print('What would you do?')
        rc = ''
        while rc != 'Ogre' and rc != 'Sword':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go left':
                rc = self.left()
            elif answer == 'go down':
                rc = self.down()
            elif answer == 'pick bomb':
                rc = self.pick_bomb(good_items)
            elif answer == 'throw bomb at door':
                rc = self.throw_bomb()
            elif answer == 'break door':
                rc = self.break_door(good_items)
            else:
                rc = ''
        return rc
               
