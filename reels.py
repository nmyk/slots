import time
from random import randint
import yaml

with file('reel.yaml', 'r') as reel_file:
    reel = yaml.load(reel_file)
print reel

def spin():
    n = 3
    payout = 0

    def convert(m):
        if        m <=  5: return reel[4]
        elif  5 < m <= 15: return reel[3]
        elif 15 < m <= 30: return reel[2]
        elif 30 < m <= 55: return reel[1]
        elif 55 < m <= 85: return reel[0]
        elif 85 < m      : return reel[5]

    reel_pics = [convert(randint(1,100)) for i in xrange(n)]
    # Pause in between pictures for suspense!
    print 20*' ' + reel_pics[0]
    time.sleep(.4)
    print 20*' ' + reel_pics[1]
    time.sleep(.4)
    print 20*' ' + reel_pics[2] + '\n'
    time.sleep(.2)
    # Various payout schemes. Edit these to your heart's content.
    # TODO: big refactor
    if reel_pics == [reel[4],reel[4],reel[4]]:
        payout = 500
    elif reel_pics == [reel[3],reel[3],reel[3]]:
        payout = 250
    elif reel_pics == [reel[2],reel[2],reel[2]]:
        payout = 80
    elif reel_pics[0] == reel_pics[1] == reel[3] and reel_pics[2] != reel[3]:
        payout = 35
    elif reel_pics[0] == reel[2] and reel_pics[1] == reel[3]:
        payout = 15
    elif reel_pics == [reel[1],reel[1],reel[1]]:
        payout = 10
    elif reel_pics == [reel[0],reel[0],reel[0]]:
        payout = 8
    elif reel_pics[0] == reel_pics[1] == reel[1] and reel_pics[2] != reel[1]:
        payout = 5
    elif reel_pics[0] == reel_pics[1] == reel[0] and reel_pics[2] != reel[0]:
        payout = 2
    return payout
