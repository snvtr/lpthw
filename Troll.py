from Scene import Scene

class TrollClass(Scene):

    def __init__(self):
        self.actions = ['go up', 'go left']

    def up(self, good_items):
        if good_items['Troll'] == 'alive':
            death('Troll catches you and rips your legs off.')
        return 'Entry'

    def left(self, good_items):
        if good_items['Troll'] == 'alive':
            death('Troll grabs you and tears you apart.')
        return 'Gold'

    def attack(self, good_items, weapon):
        if   weapon == 'attack with sword':
            print('The troll grabs the sword and breaks it. You are able to beat him to death with the hammer.')
            good_items['Troll'] = 'dead';
            good_items['Sword'] = 'broken';
            self.actions.remove('attack with sword')
            self.actions.remove('attack with hammer')
#            self.actions.remove('attack with bow')
#            self.actions.remove('attack with bomb')
            return 'win'
        elif weapon == 'attack with hammer':
            print('The troll rips the hammer from your arms and breaks it. You are able to chop his head off with the sword.')
            good_items['Troll'] = 'dead';
            good_items['Hammer'] = 'broken';
            self.actions.remove('attack with sword')
            self.actions.remove('attack with hammer')
#            self.actions.remove('attack with bow')
#            self.actions.remove('attack with bomb')
            return 'win'
#        elif weapon == 'attack with bow':
#            self.death('Do you think you can win with little peace of wood?')
#        else:
#            self.death('The bomb goes off and you both die.')
        else:
            self.death('You have nothing to fight against the troll.')

    def enter(self, good_items):
        if good_items['Sword'] == 'picked':
            self.actions.append('attack with sword')
        if good_items['Hammer'] == 'picked':
            self.actions.append('attack with hammer')
#        if good_items['Bow'] == 'picked':
#            self.actions.append('attack with bow')
#        if good_items['Bomb'] == 'picked':
#            self.actions.append('attack with bomb')

        if good_items['Troll'] == 'alive':
            print('You are facing a mountain troll. He is hungry and attacks you.')
        else:
            print('There is a dead troll. It stinks.')
        print('What would you do?')

        rc = ''
        while rc != 'Entry' and rc != 'Gold':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go up':
                rc = self.up(good_items)
            elif answer == 'go left':
                rc = self.left(good_items)
            elif answer == 'attack with sword' or answer == 'attack with hammer' or answer == 'attack with bow' or answer == 'attack with bomb':
                rc = self.attack(good_items, answer)
            else:
                rc = ''
        return rc
