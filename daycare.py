

def drop_off_child(daycare, parent, child):
    '''
    Accepts a dictonary, key and value and adds the pair to the dictionary
    '''
    daycare.update({parent: child})

def pick_up_child(daycare, parent):
    ''' 
    Accepts a dictonary and a key, using said key to access and remove a key-value pair from the dictionary 
    '''
    daycare.pop(parent)


if __name__ == "__main__":
    daycare = {}
    
    while True:
        print("Welcome to the WizC Daycare!")
        
        # Try-except block to handle possible user inputs
        try:
            choice = int(input("What would you like to do today? \n1) Drop off a child\n2) Pick up a child\n3) Quit\n"))
            
            if choice == 1:
                parent_name = input("Enter your name: \n")
                child_name = input("Enter child's name: \n")
                drop_off_child(daycare, parent_name, child_name )
                print(f"Your child {daycare.get(parent_name)} has been dropped off successfully, thank you {parent_name} for your service!")

            elif choice == 2:
                parent_name = input("Enter your name: \n")
                print(f"Your child {daycare.get(parent_name)} has been picked up successfully, thank you {parent_name} for your service!")
                pick_up_child(daycare, parent_name)

            elif choice == 3:
                print("Have a nice day!") # (Cuz we're nice guys -Wiz)
                break
        
            else:
                print("\nInvalid choice. Please try again.\n")
                continue
        
        except ValueError:
            print("\nInvalid choice. Please try again.\n")
            continue


            

            