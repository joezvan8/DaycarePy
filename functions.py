import sys

def drop_off_child(daycare: dict, parent, children: list):
    '''
    Accepts a dictonary, key and value and adds the pair to the dictionary
    '''
    daycare.update({parent: children})

def pick_up_child(daycare: dict, parent):
    ''' 
    Accepts a dictonary and a key, using said key to access and remove a key-value pair from the dictionary 
    '''
    daycare.pop(parent)

if __name__ == "__main__":
    print("This file isn't meant to be run.")
    sys.exit()


