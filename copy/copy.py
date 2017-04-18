# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys

def inputs():
    if len(sys.argv) == 1:
        print('copy [source] [destination]')
    elif len(sys.argv) == 2:
        print('No destination provided')
    else:
        pass
        
        
def copy_paste():
    original_file = open(sys.argv[2])

inputs()
            

