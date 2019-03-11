from Map import Map
from GoodItems import good_items

### __main__() ###

game_map = Map('My Game')
print(good_items)

next_room = 'Entrance'
while True:
    next_room = game_map.enter(next_room, good_items)
