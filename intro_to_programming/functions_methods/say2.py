def say(text='hello'):
    print('==> ' + text + '!')

say()
say('hi')
say('how do you do')
say('Quite all right')

def say2(msg1, msg2, msg3='dummy message', msg4='omitted message'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)
   # return 'Function executed successfully'

say2('s', 'o', 'u', 'p')
