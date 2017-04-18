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
    try:
        if len(sys.argv) == 1:
            print('copy [source] [destination]')
        elif len(sys.argv) == 3:
            print('No destination provided')
        else:
            copy_paste()
                
    except FileNotFoundError:
        print('File not found.')
            
def copy_paste():
    with open(sys.argv[2]) as f:
        with open(sys.argv[3]) as f1:
            for line in f:
                f1.write(line)
            
inputs()
            

