#!/usr/bin/env python
__author__ = 'Paul Son'
__email__ = 'pcson@ischool.berkeley.edu'
__python_version = '2.7.3'
__can_anonymously_use_as_example = False

import re
import sqlite3 as lite
import sys
#Importing functions that were in Asignment 5
from a5_fcn import restaurantNames
from a5_fcn import nHood
from a5_fcn import rating
from a5_fcn import phoneNumbers

# Connecting to DB made in command line
con = lite.connect('sqlite/yelp.db')
# Setting up cursor
cur = con.cursor()

def withCon():
	# Retrieves lists from Assignment 5 functions
	restaurantList = restaurantNames()
	neighborHood = nHood()
	ratings = rating()
	phoneNumb = phoneNumbers()
	# Inserts data into DB
	with con:
		# Looops through each list and adds the info in order
		for name, hood, rate, number in zip(restaurantList, neighborHood, ratings, phoneNumb):
			cur.execute("insert into yelp (RestaurantNames, Neighborhood, Rating, Phone) values (?,?,?,?)", (name,hood,rate,number))


def main():
	withCon()

if __name__ == '__main__':
	main()