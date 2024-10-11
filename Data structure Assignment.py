from collections import deque
undo_stack = []
delivery_queue = deque()

stored_parcels = [
    {"Parcel ID": "P001", "Recipient": "Adolphe"},
    {"Parcel ID": "P002", "Recipient": "Evode"},
    {"Parcel ID": "P003", "Recipient": "Bernard"},
    {"Parcel ID": "P004", "Recipient": "Annett"},
]

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
    else:
        print("Invalid choice. Please try again.\n")

def undo_last_parcel():
    """Undo the last added parcel from the delivery queue."""
    if undo_stack:
        last_parcel = undo_stack.pop()
        delivery_queue.remove(last_parcel)
        parcel_list.remove(last_parcel)
        print(f"Last parcel with ID {last_parcel['Parcel ID']} has been undone.\n")
    else:
        print("No parcels to undo.\n")

def process_delivery():
    """Process the next parcel in the delivery queue."""
    if delivery_queue:
        next_parcel = delivery_queue.popleft()
        print(f"Processing delivery for parcel {next_parcel['Parcel ID']} to {next_parcel['Recipient']}.\n")
    else:
        print("No parcels in the delivery queue.\n")

def show_parcels():
    """Show all parcels currently tracked."""
    if parcel_list:
        print("Tracking the following parcels:")
        for parcel in parcel_list:
            print(f"Parcel ID: {parcel['Parcel ID']}, Recipient: {parcel['Recipient']}")
        print()
    else:
        print("No parcels being tracked.\n")

def menu():
    """Display menu options to the user."""
    while True:
        print("Parcel Delivery Service")
        print("1. Add a Parcel")
        print("2. Undo Last Parcel")
        print("3. Process Delivery")
        print("4. Show Tracked Parcels")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_parcel()
        elif choice == '2':
            undo_last_parcel()
        elif choice == '3':
            process_delivery()
        elif choice == '4':
            show_parcels()
        elif choice == '5':
            print("Exiting the Parcel Delivery Service.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the menu
menu()