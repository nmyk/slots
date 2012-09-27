import time
from random import randint

# By changing the "pictures" on the reel, you can make the slot machine whatever theme you want. For example, reel = ['CHAT','CHIEN','ARBRE','MAISON','VILLE','MERDE'] has a French theme.

reel = ['LEMON','CHERRY','ORANGE','WATERMELON','PINEAPPLE','GARBAGE']

def spin():
    n = 3
    payout = 0

# The probabilities of getting the six pictures are 30%, 25%, 15%, 10%, 5%, and 15%, respectively.
    def convert(m):
        if        m <=  5: return reel[4]
        elif  5 < m <= 15: return reel[3]
        elif 15 < m <= 30: return reel[2]
        elif 30 < m <= 55: return reel[1]
        elif 55 < m <= 85: return reel[0]
        elif 85 < m      : return reel[5]

    reelPics = [convert(randint(1,100)) for i in xrange(n)]
    # Pause in between pictures for suspense!
    print 20*' ' + reelPics[0]
    time.sleep(.4)
    print 20*' ' + reelPics[1]
    time.sleep(.4)
    print 20*' ' + reelPics[2] + '\n'
    time.sleep(.2)
	
    # Various payout schemes. Edit these to your heart's content.
    if reelPics == [reel[4],reel[4],reel[4]]:
        payout = 500
    elif reelPics == [reel[3],reel[3],reel[3]]:
        payout = 250
    elif reelPics == [reel[2],reel[2],reel[2]]:
        payout = 80
    elif reelPics[0] == reelPics[1] == reel[3] and reelPics[2] != reel[3]:
        payout = 35
    elif reelPics[0] == reel[2] and reelPics[1] == reel[3]:
        payout = 15
    elif reelPics == [reel[1],reel[1],reel[1]]:
        payout = 10
    elif reelPics == [reel[0],reel[0],reel[0]]:
        payout = 8
    elif reelPics[0] == reelPics[1] == reel[1] and reelPics[2] != reel[1]:
        payout = 5
    elif reelPics[0] == reelPics[1] == reel[0] and reelPics[2] != reel[0]:
        payout = 2
    return payout
