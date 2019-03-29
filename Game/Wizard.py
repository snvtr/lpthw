from Scene import Scene

class WizardClass(Scene):

    def __init__(self):
        self.items = {'Wizard': 'not happy', 'Door': 'not broken'} # Wizard needs a hat
        self.actions = ['query wizard','go left', 'break door', 'go down','make wizard happy']

    def enter(self, good_items):
        print('You are in a room with a locked door in the wall looking down.', \
              'You are looking at a wizard.')
        if good_items['Hat'] == 'given':
            print('The wizard wears a funny pointy hat.')
        else:
            print('The wizard does not have a hat and his head is bald.')
        print('What would you do?')

        rc = ''
        while rc != 'Hole' and rc != 'EmptyLeftUpper':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go left':
                rc = self.left()
            elif answer == 'go down':
                rc = self.down()
            elif answer == 'break door':
                rc = self.break_door(good_items)
            elif answer == 'query wizard':
                rc = self.ask_wizard()
            elif answer == 'make wizard happy':
                rc = self.make_wizard_happy(good_items)
            else:
                rc = '' # rc = self.enter(good_items) # pass?
        return rc

    def break_door(self, good_items):
        if self.items['Door'] == 'broken':
            print('The door to the room down is already broken.')
            return 'already broken'
        if good_items['Hammer'] == 'not picked':
            print('Are you going to break the door with your fists?')
            return 'no hammer'
        print('You break the door with the hammer. You can pass thought it now.')
        self.items['Door'] = 'broken'
        self.actions.remove('break door')
        return 'broken'
            
    def make_wizard_happy(self, good_items):
        if good_items['Hat'] == 'picked':
            good_items['Hat'] = 'given'
            print('You have given the hat to the wizard.', \
                  'He is really happy to hide his bald head under the hat.', \
                  'He thanks you and lets you pass.')
            self.actions.remove('make wizard happy')
            self.items['Wizard'] = 'happy'
        elif good_items['Hat'] == 'given':
            print('You have already given the hat to the wizard. He is happy enough already.')
        else:
            print('You have nothing to please the wizard. Go and find something useful.')
        
    def ask_wizard(self):
        print('You ask the wizard if he can help you.')
        if self.items['Wizard'] == 'happy':
            print('The wizard angrily replies that he has nothing to add.')
            return 'angry'
        print('The wizard replies that he has lost his hat and is very sad about it.')
        return 'sad'

    def left(self):
        return 'EmptyLeftUpper'

    def down(self):
        if self.items['Wizard'] != 'happy':
            print('The wizard won't let you pass')
            return ''
        else:
            return 'Hole'
