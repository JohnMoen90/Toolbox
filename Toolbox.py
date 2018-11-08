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
    """ This function simply returns the correct time of day word when the function is run
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


# Formats book/movie titles
def title(old_title):
    """
    This program takes a string and capitalizes every word that is not
    a function word (and, or, etc...) and also moves the 'The' at the beginning
    to the end of the title preceded by a comma.
    :param old_title: This is the title you want to change
    :return: Returns modified title
    """
    # Set variables
    new_title = []
    word_one = ''

    # Split up the title
    words = old_title.split(" ")

    # Separate first word from rest if there is more than one word
    if len(words) > 1:
        word_one = str(words.pop(0)).capitalize()

    # List exceptions to the capitalization rule
    exceptions = ['a', 'an', 'the', 'am', 'for', 'and', 'nor', 'but'
                  'or', 'yet', 'so', 'at', 'around', 'by', 'after',
                  'along', 'from', 'of', 'on', 'to', 'with', 'without']

    # Capitalize each word not in exceptions
    for word in words:
        if word not in exceptions:
            new_title.append(word.capitalize())
        else:
            new_title.append(word)

    # Capitalize the 'the' at the end of title, if inputted that way
    if new_title[-1] == 'the':
        new_title[-1] = new_title[-1].capitalize()

    # Join words back together into a string
    new_title = ' '.join(new_title)

    # Put the 'the' at the end if 'the' was the first word
    if word_one == 'The':
        new_title += ', The'

    # Don't add space if title is one word
    elif word_one == '':
        return new_title

    # Put first word back
    else:
        word_one += ' ' + new_title
        new_title = word_one

    return new_title
