#!/usr/bin/python

# dictionaries are similar to hashes in perl or objects in javascript.  Robust
# key/value pair types.  denoted with curly braces '{', values are accessible
# with standard brackets:

dict = {}

dict[ 'hometown' ] = 'Chicago'
dict[ 'occupation' ] = 'Coder'

# note: keys can also be numbers if desired.

# access values from dictionary:
print( dict['hometown'] )

# print full dictionary
print( dict )

# print JUST keys:
print( dict.keys() )

# print JUST values:
print( dict.values() )

# Note: there is no guarantee of ordering in dictionaries
