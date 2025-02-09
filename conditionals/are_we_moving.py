speed = 0
acceleration = 24
braking_force = 19

is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
          #     19       True    24           ( 0 False  or       24    True)
          #               True            and               True    
          #  This is truthy
print(is_moving)   # True
# Yes the parentheses are needed here because the 'and' has higher operator precedence than 'or'.