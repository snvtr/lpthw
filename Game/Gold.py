from Scene import Scene

class GoldClass(Scene):

    def __init__(self):
        self.actions = ['go left', 'go up', 'pick gold']
        self.gold_counter = 0

    def up(self):
        return 'Back2Watchman'

    def left(self):
        return 'Troll'

    def pick_gold(self, good_items):
        print('You have picked a sack with gold.')
        self.gold_counter += 1
        good_items['Gold'] = 'picked'
        if self.gold_counter > 2:
            print('So many sacks with gold are too heavy for you. You cannot pull them out of the room.')
            self.actions.append('drop a sack')
            return 'too much'
        return 'enough'

    def enter(self, good_items):
        print('You are in a treasure room. There are many sacks with gold.')
        if   self.gold_counter == 1:
            print('You have already picked one sack.')
        elif self.gold_counter >= 2:
            print('You have already picked %s sacks.' % self.gold_counter)

        print('What would you do?')

        rc = ''
        while rc != 'Back2Watchman' and rc != 'Troll':
            answer = input(', '.join(self.actions) + ' > ')
            if   answer == 'go left':
                rc = self.left()
            elif answer == 'go up':
                rc = self.up()
            elif answer == 'drop a sack':
                if self.gold_counter != 0:
                    self.gold_counter -= 1
                    if self.gold_counter == 1:
                        print('You know have only one sack of gold.')
                    else:
                        print('you now have %s sacks of gold.' % self.gold_counter)
                rc = ''
            elif answer == 'pick gold' :
                rc = self.pick_gold(good_items)
            else:
                rc = ''
        return rc
                
