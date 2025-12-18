from functions import drop_off_child, pick_up_child

def main(): 
    while True:
        print("\nWelcome to the WizC Daycare!")
        
        # Try-except block to handle possible user inputs
        try:
            choice = int(input("\nWhat would you like to do today? \n1) Drop off a child\n2) Pick up a child\n3) Quit\n"))
            
            if choice == 1:
                parent_name = input("\nEnter your name: \n")
                children_name = input("\nEnter child's or children's name(s): \n")
                child_list = [item.strip() for item in children_name.split(",")]
                drop_off_child(daycare, parent_name, child_list)
                print(f"\nYour child/children {", ".join(child_list)} has/have been dropped off successfully, thank you {parent_name} for your service!")

            elif choice == 2:
                
                parent_name = input("\nEnter your name: \n")
                try:
                    children_name = daycare[parent_name]
                    print(f"Your child/children {", ".join(children_name)} has/have been picked up successfully, thank you {parent_name} for your service!")
                    pick_up_child(daycare, parent_name)
                except KeyError:
                    print(f"\nSorry {parent_name}, we don't have a record of a child dropped off under your name.")

            elif choice == 3:
                print("Have a nice day!") # (Cuz we're nice guys -Wiz)
                break
        
            else:
                print("\nInvalid choice. Please try again.\n")
                continue
        
        except ValueError:
            print("\nInvalid choice. Please try again.\n")
            continue

if __name__ == "__main__":
    daycare = {}
    main()
    
    


            

            