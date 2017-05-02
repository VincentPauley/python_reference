#!/usr/bin/python

# basically arrays, all items can be of different types

list = [ 'Rick', "Morty", 342.3, 4, "Summer", 7990.4 ]

short_list = [ 'Wubaluba', 'dub dub' ]


print( list )      # prints the complete list
print( list[0] )   # prints first element in the array
print( list[1:3] ) # prints second, untill 3rd (stops before 3rd)
print( list[2:] )  # print 2nd element on
print( list * 2 )  # print the list twice
print( list + short_list ) # print the concateated lists
