"""
A collection of functions
- John Moen
"""
import sys
import datetime


# Offers option to restart program
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


# Returns morning/afternoon/evening depending on time of day
def time_day():
    """
    This function simply returns the correct time of day word when the function is run
    :return: morning, evening, or afternoon depending on time of day
    """

    # Get the time
    time = str(datetime.datetime.now().time())

    # Slice the hour out
    time = int(time[:2])

    # Get appropriate time of day word
    if time < 12:
        day_time = "morning"
    elif time >= 17:
        day_time = "evening"
    else:
        day_time = "afternoon"
    return day_time


