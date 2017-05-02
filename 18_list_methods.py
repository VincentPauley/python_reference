#!usr/bin/python

games = [ 1, 2, 2, 2, 3, 4, 5, 6, 7, 8 ]

# append() -> add item to array

games.append( 9 )

print( games )

# count() -> returns total occurances of parameter in the array
print( games.count( 2 ) ) # 3

# index() -> returns lowest index that obj appears in the list
print( games.index(4) ) # 5

# pop() -> remove and return last object from list

last = games.pop()

print( last ) # 9

print( games )
