from Scene import Scene

class EntranceClass(Scene):

    def __init__(self):
        self.items = {'Door': 'not broken'}
        self.actions = ['go up', 'go down', 'pick hammer', 'break door']

    def up(self):
        return 'EmptyLeftUpper'

    def down(self):
        if self.items['Door'] == 'not broken':
            print('You cannot go through the closed door.')
            return ''
        return 'Bow'

    def pick(self, good_items):
        if  good_items['Hammer'] == 'not picked':
            print('You have picked up the hammer')
            good_items['Hammer']     = 'picked'
            self.actions.remove('pick hammer')
            return 'picked'
        print('You already have it! Do you not remember?')
        return 'not picked'
 
    def break_door(self, good_items):
        if good_items['Hammer'] == 'picked' and self.items['Door'] == 'not broken':
            print('You have broken down the door')
            self.items['Door'] = 'broken'
            self.actions.remove('break door')
            return 'Door broken'
        elif self.items['Door'] == 'broken':
            print('What's the point? The door has already been broken!')
        elif good_items['Hammer'] == 'not picked':
            print('You gonna break the door with your owns fists?')
        return 'Door not broken'
        
    def enter(self, good_items):
        print('You have entered the room. There is way up into another room.')
        if self.items['Door'] == 'broken':
            print('The door to the room down is broken.')
        else:
            print('The door to the room down is locked.')
        if good_items['Hammer'] == 'not picked':
            print('There is also a hammer on the floor.')
        else:
            print('There is nothing on the floor.') 
            
        print('What would you do?')
        rc = ''
        while rc != 'Bow' and rc != 'EmptyLeftUpper':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go down':
                rc = self.down()
            elif answer == 'go up':
                rc = self.up()
            elif answer == 'pick hammer':
                rc = self.pick(good_items)
            elif answer == 'break door':
                rc = self.break_door(good_items)
            else:
                rc = '' # rc = self.enter(good_items) # pass ?
        return rc
 
