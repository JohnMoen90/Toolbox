"""
A collection of functions
- John Moen
"""
import sys


def restart():
    """ This function should be used at the end of a while loop to prompt user to restart
    :return: N/A """
    while True:
        print('')
        yes_or_no = input('Would you like to use ____ again? (y/n)\n')  # Change this text to change prompt
        if yes_or_no == 'n':
            sys.exit()
        elif yes_or_no != 'y':
            continue
        else:
            break



