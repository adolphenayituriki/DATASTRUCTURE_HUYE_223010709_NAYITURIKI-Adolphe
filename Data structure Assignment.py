
                                        #Q6. PARCEL DELIVERY SERVICE


from collections import deque
undo_stack = []
delivery_queue = deque()


stored_parcels = [
    {"Parcel ID": "P001", "Recipient": "Adolphe"},
    {"Parcel ID": "P002", "Recipient": "Evode"},
    {"Parcel ID": "P003", "Recipient": "Bernard"},
    {"Parcel ID": "P004", "Recipient": "Annett"},
]
# Is used to ask the user to add any parcel if he/she want
adding = [
    {"Parcel ID": "P001", "Recipient": "Adolphe"},
    {"Parcel ID": "P002", "Recipient": "Evode"},
    {"Parcel ID": "P003", "Recipient": "Bernard"},
    {"Parcel ID": "P004", "Recipient": "Annett"},
]
# This is the function to add parcel from the user
def adding_another():
    """add another parcels."""
    print("Stored Parcels:")
    for idx, parcel in enumerate(adding, start=1):
        print(f"{idx}. Parcel ID: {parcel['Parcel ID']}, Recipient: {parcel['Recipient']}")
    print()

    
parcel_list = []

def display_stored_parcels():
    """Display stored parcels."""
    print("Stored Parcels:")
    for idx, parcel in enumerate(stored_parcels, start=1):
        print(f"{idx}. Parcel ID: {parcel['Parcel ID']}, Recipient: {parcel['Recipient']}")
    print()

def add_parcel():
    """Add a parcel to the delivery queue by selecting from stored parcels."""
    display_stored_parcels()
    choice = int(input("Select a parcel number to add to the delivery queue (1-4): "))
    if 1 <= choice <= len(stored_parcels):
        
        
        selected_parcel = stored_parcels[choice - 1]
        delivery_queue.append(selected_parcel)
        parcel_list.append(selected_parcel)
        undo_stack.append(selected_parcel)
        print(f"Parcel {selected_parcel['Parcel ID']} added to delivery queue.\n")
        print(f"Current parcel Your Selected : {selected_parcel}")
    else:
        print("Invalid choice. Please try again.\n")
    
def process_delivery():
    """Process the next parcel in the delivery queue."""
    if delivery_queue:
        next_parcel = delivery_queue.append(delivery_queue)
        print(f"Processing delivery for parcel {next_parcel['Parcel ID']} to {next_parcel['Recipient']}.\n")
    else:
        print("No parcels in the delivery queue.\n")

def undo_last_parcel():
    """Undo the last added parcel from the delivery queue."""
    if undo_stack:
        last_parcel = input("Enter any parcel to undo")
        print(stored_parcels)
        last_parcel = undo_stack.pop()
        delivery_queue.remove(last_parcel)
        parcel_list.remove(last_parcel)
        print(f"Last parcel with ID {last_parcel['Parcel ID']} has been undone.\n")
    else:
        print("No parcels to undo.\n")



def show_parcels():
    """Show all parcels currently tracked."""
    if parcel_list:
        print("Tracking the following parcels:")
        for parcel in parcel_list:
            print(f"Parcel ID: {parcel['Parcel ID']}, Recipient: {parcel['Recipient']}")
        print()
    else:
        print("No parcels being tracked.\n")


    """Display menu options to the user."""
    while True:
        print("Parcel Delivery Service")
        print("1. Available parcel")
        print("2. Undo Last Parcel")
        print("3. Process Delivery")
        print("4. Show Tracked Parcels")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_parcel()
            choice = str(input("Do you want to add another? yes/no "))
            if choice=='yes':
                adding_another()
                choice = int(input("Add another parcel: "))
                print(f"Parcel {choice} added to delivery queue.\n")
                if choice==1 or 3 or 3 or 4:
                    stored_parcels.append(choice)
                    print(f"{choice} added to a list to be delivered ")
                    
        elif choice=="no":
            print("thank you")
            for i in stored_parcels:
                print(i)
            if choice=="adolphe" or "evode" or "bernard" or "annett":
        
                print(f"{choice} added to be delivered")
            else: print("Thank you for your choice! ")
        elif choice == '2':
    
            undo_last_parcel()
        elif choice == '3':
            
            delivery_queue.append(delivery_queue)
            print(delivery_queue)
            
        elif choice == '4':
            print("the tracked parcels are: ")
            show_parcels()
        elif choice == '5':
            print("Exiting the Parcel Delivery Service.")
            
        else:
            print("Invalid choice. Please try again.\n")
            break #######
# Run the menu
show_parcels()
undo_last_parcel()
process_delivery()
