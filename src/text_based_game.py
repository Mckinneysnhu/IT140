"""Project Two starter for the student's text-based adventure game."""

# Kaleef Mckinney Wilson


def show_instructions():
    print("Text Adventure Game")
    print("Collect all 6 items before entering the Command Center.")
    print("Move commands: go North,go South, go East, go West")
    print("To collect an item: get item name'")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    print("You are in the", current_room)
    # TODO: Show the current inventory.
    print("Inventory:" , inventory)
    # TODO: Show the current-room item when one is available.
    if "item" in rooms[current_room]:
       print("You see a" , rooms[current_room]["item"])
    


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.
    rooms = {
     "Main Gate":{
        "North": "Barracks",
    },
    "Barracks": { "South": "Main Gate",
                  "East": "Security Office",
                  "item": "Protective Vest",
    },
    "Security Office": {
                  "West": "Barracks",
                  "North": "Medical Bay",
                  "item": "Keycard",
    },
    "Medical Bay": {
                  "South": "Security Office",
                  "East": "Supply Depot",
                  "item": "First Aid Kit",
   },
   "Supply Depot": {
                  "West": "Medical Bay",
                  "South": "Communications Room",
                  "item": "Flashlight",
   },
   "Communications Room": {
                        "North": "Supply Depot",
                        "West": "Armory",
                        "item": "Radio",
   },
   "Amory": {
           "East": "Communications Room",
           "South": "Command Center",
           "item": "Weapon",
  },
  "Command Center": {
                   "item": "Zombie Commander"
                 }
  }

    # TODO: Set the player's starting room.
    current_room = "Main Gate"

    # TODO: Create the player's inventory.
    inventory = []

    # TODO: Call the instruction function at the appropriate time.
    show_instructions ()

    # TODO: Create the gameplay loop.
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move:")
        if command.startswith("go"):
             direction = command[3:]
             if direction in rooms[current_room]:
              current_room = rooms[current_room][direction]
             else: 
                 print("You cant go that way.")
        elif command.startswith("get"):
            item = command[4:]
            if "item" in rooms[current_room] and rooms[current_room]["item"] == item:
                inventory.append(item)
                del rooms[current_room]["item"]
                print("You picked up the", item)
            else:
                print("That item is not in this room.")  
        else: 
          print("Invalid command.")
        if current_room == "Command Center" and len(inventory) < 6:
                  print("The Zombie Commander got you. You lose!")
                  break
        if current_room == "Command Center" and len(inventory) == 6:
                  print("You collected all the items! You win!")
                  break
     
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    


if __name__ == "__main__":
    main()
