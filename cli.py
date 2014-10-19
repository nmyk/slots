import sys
import os
import machine

def CLI(slot_machine):
    player_input = raw_input('Command: ')
    parsed_commands = player_input.split()
    if len(parsed_commands) > 0:
        if parsed_commands[0] == 'bet':
            if len(parsed_commands) ==2:
                slot_machine.change_bet(int(parsed_commands[1]))
            else:
                print 'The current bet is $' + str(slot_machine.bet) + '.'
        elif parsed_commands[0] == 'balance':
            slot_machine.print_balance()
        elif parsed_commands[0] == 'add':
            slot_machine.add_money(int(parsed_commands[1]))
        elif parsed_commands[0] == 'quit':
            sys.exit(0)
        elif parsed_commands[0] == 'help':
            os.system('clear')
            print_help()
        else:
            os.system('clear')
            print 'Invalid command. Type "help" for options.'
    else:
        slot_machine.gamble()

def print_help():
    print 'Commands:\n bet (#)\n balance\n help\n quit\n Press enter without issuing a command to pull the crank!'
    print """
    Combination                        Payout multiplier 
    ----------------------------------------------------
    PINEAPPLE PINEAPPLE PINEAPPLE            500
    WATERMELON WATERMELON WATERMELON         250
    ORANGE ORANGE ORANGE                      80
    WATERMELON WATERMELON *any*               35
    ORANGE WATERMELON *any*                   15
    CHERRY CHERRY CHERRY                      10
    LEMON LEMON LEMON                          8 
    CHERRY CHERRY *any*                        5
    LEMON LEMON *any*                          2     

"""

def game_intro():
    print """
        
    
                  SLOTS! v1.0
            developed by Nick Mykins    

"""
