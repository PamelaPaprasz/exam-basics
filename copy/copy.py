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
                
        def copy_paste():
            from_file = open(sys.argv[2], 'r')
            from_data = from_file.read()
            
            to_file = open(sys.argv[3], 'r')
            to_data = to_file.read()
            
            from_file.close()
            to_file.close()
    
    except FileNotFoundError:
        print('File not found.')
    
    

inputs()
            

