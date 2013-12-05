#!/usr/bin/env python
__author__ = 'Paul Son'
__email__ = 'pcson@ischool.berkeley.edu'
__python_version = '2.7.3'
__can_anonymously_use_as_example = False
import re

yelp_fin = open('yelp_listings.html').read()

def get_input():
    print('''
============================================================
MENU
============================================================
0 - Exit
1 - Question 1:  Restaurant Names
2 - Question 2:  Restaurant Neighborhoods
3 - Question 3:  Restaurant Ratings
4 - Question 4:  Restaurant Telephone Numbers
5 - Question 5:  Neighborhood with the Highest Rating
6 - Question 6:  Did Not Do Extra Credit
7 - Show Regular Expressions
    ''')
    command = raw_input('What would you like to do? ')
    return command

# Finds all restaurant names using RegEx
def q1():
    # Counter used to keep track of number of names
    count =0
    # Creates empty list
    my_list = []
    names = re.findall(r"""\"[a-z]{3}[A-Z][a-z]{4}[A-Z][a-z]{3}\d{1,2}\"\> # Captures part of the attribute info in the tag preceding restaurant name
                            \d{1,2} # Captures single/double digit number before the name
                            .*""",# Captures restaurant name before /r</a> in html
                             yelp_fin, flags=re.VERBOSE)
    length = range(0,len(names))
    # Loops through all the names and cleans up the str
    for i in length:
        # Find where the tab is
        name_index = names[i].find('\t')
        # Find the restaurant name right of tab
        rest_name = names[i][name_index+1:]
        # Adds it to list
        my_list.append(rest_name)
    # Loops through list and prints out the name
    for i in my_list:
        count +=1
        print str(count) + '.', i

# Takes list of neighborhood names and prints out in order of appearance in the orig file
def q2():
    # Calls hood function and takes output list
    names_hood = hood()
    length = range(0,len(names_hood))
    # Counter used to keep track of the number of neighborhoods
    count = 0
    for h in names_hood:
        count +=1
        print str(count) + '.', h

# Find neighborhood names using RegEx, cleans str, and return list
def hood():
    # Creates empy list
    hood_list = []
    # Finds hood names using regexes
    hood = re.findall(r"""\"[a-z]{4}\_[a-z]{6}\_\d{1,2}\_\d\" # Captures info in tage before neighborhood name
                            .* # Captures the neighborhood name
                            \< # Capture angle bracket of end tag
                            """, yelp_fin, flags=re.VERBOSE)
    length = range(0,len(hood))
    # Loops through to clean up str
    for i in length:
        # Finds index for angle bracket
        hood_index = hood[i].find('>')
        # Uses that above index to strip out hood name
        hood_name = hood[i][hood_index+1:-1]
        # Add it to the empty list
        hood_list.append(hood_name)
    # Return list of neighborhood names
    return hood_list

# Prints out ratings for each restaurant
def q3():
    # Counter to keep track of number of ratings
    count = 0
    # Calls function and gets ratings_list
    ratings = rating()
    length = range(0, len(ratings))
    # Loops through and prints out ratings for each restaurant
    for r in ratings:
        count +=1
        print str(count) + '.', r

# Captures ratings found in HTML tag
def rating():
    # Creates empty list for ratings
    ratings_list = []
    # Captures ratings using regexes
    ratings = re.findall(r"""\s\w{3}\=\" # finding/capturing tag attr info for ratings
                            \d\.?\d? # find/capture rating as either single digit or decimal number
                            """, yelp_fin, flags=re.VERBOSE)
    length = range(0, len(ratings))
    # Goes through list of ratings and cleans up strings
    for i in length:
        # Finds the index for double quotes
        ratings_index1 = ratings[i].find('"')
        # Strips everything after it
        ratings_number = ratings[i][ratings_index1+1:]
        # Adds it to list
        ratings_list.append(ratings_number)
    # Output list of ratings. Called by q3()
    return ratings_list

def q4():
    # Counter to keep track of number of phone numbers
    count = 0
    # Creates empty list
    phone_list = []
    # Uses regexes to find phone numbers
    phone_numb = re.findall(r"""\(\d{3}\) # find the area code
                                \s\d{3}\- # finds the first 3 numb of phone number
                                \d{4} # Finds last 4 numb of phone number
                                """, yelp_fin, flags=re.VERBOSE)
    length = range(0, len(phone_numb))
    # Loops through list of phone numbers and prints them
    for each in phone_numb:
        count +=1
        print str(count)+'.',each

def q5():
    # Gets list from other functions
    list_of_ratings = rating()
    list_of_neighborhoods = hood()
    # Creates empty dictionaries
    best_dict = {} # Total rating amount for each neighborhood
    number_dict = {} # Total number of restaurants in each neighborhood
    ave_rate_dict = {} # Total rating amount/total number of restaurants

    # Creates variable for loop range
    length = range(0,len(list_of_neighborhoods))

    # Loops through each neighborhood and each new one is added to a dictionary
    # The order of restaurant names, ratings, and neighborhoods all correlate.
    for index in length:
        # Variable for the neighborhood name
        r_name = list_of_neighborhoods[index]
        # If the name exists in the dict...
        if r_name in best_dict:
            # The restaurant rating in the neighborhood is added to neighborhoods current total
            best_dict[r_name] += float(list_of_ratings[index])
            number_dict[r_name] += 1 # number of ratings in each neighborhood accounted for
        # If it doesn't already exist...
        else:
            # The neighborhood name is added to the dict along with it's rating
            best_dict[r_name] = float(list_of_ratings[index])   
            number_dict[r_name] = 1 # The total number of ratings in said hood thus far
        # NOTE: each neighborhood should only hit the ELSE above only ONCE

    # Iterates through dict and finds average rating for each neighborhood
    for key in best_dict:
        ave_rate_dict[key] = best_dict[key]/number_dict[key]
    # Prints out results
    print 'The Neighborhood with the Highest Rating is:'
    # Finds the highest number for the best rated neighborhood
    the_best_hood = max(ave_rate_dict, key=ave_rate_dict.get)
    # Prints out results       # Minimizes ave rate to two decimal places
    print the_best_hood, ": ",("%.2f" % ave_rate_dict[the_best_hood])

# Did not do extra credit
def q6():
    print 'n/a'

def q7():
    print 'Regular Expressions:'
    print 'name: ', "\"[a-z]{3}[A-Z][a-z]{4}[A-Z][a-z]{3}\d{1,2}\"\>\d{1,2}.*"
    print 'neighborhood: ', "\"[a-z]{4}\_[a-z]{6}\_\d{1,2}\_\d\".*\<"
    print 'rating: ', "\s\w{3}\=\"\d\.?\d?"
    print 'phone: ', "\(\d{3}\)\s\d{3}\-\d{4}"
    print 'extra credit: ', "n/a"



if __name__ == '__main__':

    command = None
    while command != '0':
        #gets input from the user:
        command = get_input()

        #depending on the item selected, call the corresponding function:
        if command == '0':
            exit()
        elif command == '1': q1()
        elif command == '2': q2()
        elif command == '3': q3()
        elif command == '4': q4()
        elif command == '5': q5()
        elif command == '6': q6()
        elif command == '7': q7()
        else: print('"{}" is an invalid command.'.format(command))

        raw_input('\nPress enter to continue...')

